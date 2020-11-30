class Feedback:
    def __init__(self, qos, fs, cf, recommend, suggestions, other_comment, owner, id = None):
        self.qos = qos
        self.fs = fs
        self.cf = cf
        self.recommend = recommend
        self.suggestions = suggestions
        self.other_comment = other_comment
        self.owner = owner
        self.id = id
        self.get_average = (int(self.qos) + int(self.fs) + int(self.cf) + int(self.recommend) ) / 4

  