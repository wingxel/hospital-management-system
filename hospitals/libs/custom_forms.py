from django import forms
from typing import Any
from hospitals.models import Note

class Util:
    @staticmethod
    def add_prop(visible_field: Any) -> None:
        visible_field.field.widget.attrs["class"] = "form-control db-form"
        visible_field.field.widget.attrs["placeholder"] = f"{visible_field.field.label}"


class AddNote(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddNote, self).__init__(*args, **kwargs)
        for visible_field in self.visible_fields():
            Util.add_prop(visible_field)
    
    class Meta:
        model = Note
        fields = ["title", "note", "priority"]
