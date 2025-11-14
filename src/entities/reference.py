class Reference:
    def __init__(self, entry_id, type_name, fields=None):
        self.entry_id = entry_id
        self.type_name = type_name
        self.fields = fields or []

    def get(self, field_name):
        for f in self.fields:
            if f.name == field_name:
                return f.value
        return None

    def __repr__(self):
        return f"<Reference id={self.entry_id} type={self.type_name} fields={len(self.fields)}>"

    @property
    def title(self):
        return self.get("title")

    @property
    def author(self):
        return self.get("author")

    @property
    def year(self):
        return self.get("year")
