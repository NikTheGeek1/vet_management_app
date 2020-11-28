class Feedback:
    def __init__(self, qos, fs, cf, recommend, suggestions, other_comment, owner_id, id = None):
        self.qos = qos
        self.fs = fs
        self.cf = cf
        self.recommend = recommend
        self.suggestions = suggestions
        self.other_comment = other_comment
        self.owner_id = owner_id
        self.id = id

    def get_average(self):
        return ( int(self.qos) + int(self.fs) + int(self.cf) + int(self.recommend) ) / 4
        