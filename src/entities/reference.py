class Reference:
    def __init__(self, entry_id, title, author, year):
        self.entry_id = entry_id
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"<reference_id={self.entry_id} title={self.title}>"
