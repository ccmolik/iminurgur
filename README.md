# What is this?

Using stegnography, inject text into all imgur image requests by proxying. It stores the contents in redis for performance (why bother re-stegging for a bunch of clients?)

This is an inline script for mitmproxy. 
# Requirements

** This requires python 2.7 to my knowledge. `mitmproxy` seems to need python 2.7 to correctly `pip install`. **

It's possible I'm wrong, but 1AM me couldn't get this working in CentOS 6 with py2.6

Tested on Fedora 21. Should work in CentOS7, Ubuntu-recent, and anything with python2.7 or higher with relevant image-devel libraries installed.

Doesn't seeem to work on CentOS 6.


## Python modules
Note the `requirements.txt`:

> pip install -r ./requirements.txt

The list of modules:

* mitmproxy
* pillow
* stepic
    * Note that you're going to want libjpeg-devel and libpng-devel installed before you install pillow, otherwise you're going to have a bad time
* redis
## Other

* redis server listening on localhost

# Usage
Bring your redis server up, and run
> mitmproxy -s mitminject.py

# TODO
* Track state of injected text (change text to be injected)
* Embed verification (hashing, signing, etc.)
* Squash random exceptions it throws 
* un-fuck code style
* Pick a solid state of module versions for requirements.txt (aka get this up in a venv)

# Credits
* https://saxenarajat99.wordpress.com/2014/01/17/hiding-image-in-image-in-python-using-steganography/ for stepic shenanigans
* [fitblip](https://github.com/fitblip) for the idea of using stegnography with imgur images
