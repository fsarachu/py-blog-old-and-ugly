import webapp2

from handlers import *

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/newpost', NewPostHandler)
], debug=True)
