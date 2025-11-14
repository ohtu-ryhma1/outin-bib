class Reference:
    def __init__(self, id, title, author, year):
        self.id = id
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"<reference_id={self.id} title={self.title}>"
