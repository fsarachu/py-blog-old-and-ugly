from Handler import Handler
from entities import *


class NewPostHandler(Handler):
    def get(self):
        self.render('new_post.html')

    def post(self):
        title = self.request.get('title')
        content = self.request.get('content')

        if title and content:
            new_post = Post(title=title, content=content)
            new_post.put()
            self.redirect('/')
        else:
            error = 'You must provide both title and content.'
            self.render('new_post.html', title=title, content=content, error=error)
