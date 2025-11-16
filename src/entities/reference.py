class Reference:
    def __init__(self, reference_type, name, fields=None):
        self.type = reference_type
        self.name = name
        self.fields = fields or []

    def __repr__(self):
        return f"Reference(type={self.type}, name={self.name}, fields={self.fields}"

    @property
    def reference_type(self):
        return self.type

    @property
    def name(self):
        return self.name

    @property
    def fields(self):
        return self.fields

    def get_field(self, field_name):
        fields = set(filter(lambda f: f.name == field_name, self.fields))
        return fields[0] if fields else None
