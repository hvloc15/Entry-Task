class UserActivity(object):
    def __init__(self, likes=[], comments=[], participates=[]):
        self.likes = likes
        self.comments = comments
        self.participates = participates

    def as_json(self):
        return dict(
            likes=self.likes,
            comments=self.comments,
            participates=self.participates,
        )