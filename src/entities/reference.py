class Reference:
    def __init__(self, reference_type, name, fields=None):
        self._type = reference_type
        self._name = name
        self._fields = fields or []

    def __repr__(self):
        return f"Reference(type={self.type}, name={self.name}, fields={self.fields}"

    @property
    def reference_type(self):
        return self._type

    @property
    def name(self):
        return self._name

    @property
    def fields(self):
        return self._fields

    def get_field(self, field_name):
        fields = [f for f in self.fields if f.name == field_name]
        return fields[0] if fields else None
