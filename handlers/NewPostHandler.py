from Handler import Handler


class NewPostHandler(Handler):
    def get(self):
        self.render('new_post.html')
