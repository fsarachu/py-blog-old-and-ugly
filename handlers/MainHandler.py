from google.appengine.ext import db

from Handler import Handler


class MainHandler(Handler):
    def get(self):
        posts = db.GqlQuery('SELECT * FROM Post ORDER BY created DESC LIMIT 10')
        self.render('index.html', posts=posts)
