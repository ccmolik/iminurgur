# Usage: mitmdump -s mitminject.py
from libmproxy.protocol.http import decoded
from libmproxy.script import concurrent
import redis
import cStringIO
import hashlib
import stepic
from PIL import Image
# connect to redis server
r = redis.StrictRedis(host="localhost", port=6379, db=0)
@concurrent
def response(context, flow):
    global db
    if flow.response.headers.get_first("content-type", "").startswith("image") and flow.request.pretty_host(hostheader=True).endswith("i.imgur.com"):
        with decoded(flow.response):  # automatically decode gzipped responses.
            try:
                # Hash returned content for a key in redis
                content_hash = hashlib.md5(flow.response.content).hexdigest()
                # And check redis for said hash
                redis_response = r.get(content_hash)
                if redis_response == None:
                    # Looks like we haven't served this image yet.
                    # Inject us some data
                    # Load image via PIL and cStringIO hackery
                    imghandler = cStringIO.StringIO(flow.response.content)
                    pillowbiter = Image.open(imghandler)
                    # Inject text - you'll change this.
                    s = stepic.encode(pillowbiter, "Image processing in Python is annoying.")
                    # Create a cStringIO handler for stepic output
                    resphandler = cStringIO.StringIO()
                    # Write to it...
                    s.save(resphandler, "png")
                    # "Cache" the steg'd image in Redis
                    r.set(content_hash, resphandler.getvalue())
                # Now we're sure that this image exists in redis, return content
                flow.response.content = r.get(content_hash)
                flow.response.headers["content-type"] = ["image/png"]
            except Exception, e:  # Unknown image types etc.
                pass
 
