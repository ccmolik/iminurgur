# What is this?

Using stegnography, inject text into all imgur requests by proxying. It stores the contents in redis for performance (why bother re-stegging for a bunch of clients?)

This is an inline script for mitmproxy. 
# Requirements
Trying to get mitmproxy working in a virtualenv is annoying because lxml (among others) is goofy to compile. So yes, I'm a bad person.

* mitmproxy
* pillow
* stepic

** Note that you're going to want libjpeg-devel and libpng-devel installed before you install pillow, otherwise you're going to have a bad time
* redis
** redis server listening on localhost

# Usage
Bring your redis server up, and run
> mitmproxy -s mitminject.py

# TODO
* Track state of injected text (change text to be injected)
* Embed verification (hashing, signing, etc.)
* Squash random exceptions it throws 
* un-fuck code style
