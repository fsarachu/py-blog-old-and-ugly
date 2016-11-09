from Handler import Handler
from entities import Post


class MainHandler(Handler):
    def get(self):
        posts = Post.all().order('-created')
        self.render('index.html', posts=posts)
