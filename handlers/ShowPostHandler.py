from Handler import Handler
from entities import *


class ShowPostHandler(Handler):
    def get(self, post_id):
        post = Post.get_by_id(int(post_id))
        self.render('post.html', post=post)
