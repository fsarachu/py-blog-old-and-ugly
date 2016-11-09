from Handler import Handler
from entities import *


class NewPostHandler(Handler):
    def get(self):
        self.render('new_post.html')

    def post(self):
        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
            new_post = Post(subject=subject, content=content)
            new_post.put()
            self.redirect('/' + str(new_post.key().id()))
        else:
            error = 'You must provide both subject and content.'
            self.render('new_post.html', subject=subject, content=content, error=error)
