import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.render('index.html')
