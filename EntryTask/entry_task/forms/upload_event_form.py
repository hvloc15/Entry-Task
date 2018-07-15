from django import forms
from django.conf import settings
from entry_task.helpers import datetime_helpers


class UploadEventInfoForm(forms.Form):
    title = forms.CharField(required=True, label="Title")
    TYPE_LIST = (('type1','type1'), ('type2','type2'), ('type3','type3'))
    type = forms.ChoiceField(choices=TYPE_LIST, label="Type")
    location = forms.CharField(required=True)
    description = forms.CharField(widget=forms.Textarea(), initial="", label="Description")
    date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,
                           label="Date",
                           required=True,
                           widget=forms.DateInput(attrs={'placeholder': 'DD-MM-YYYY'}),
                           )

    def get_tile(self):
        return self["title"].value()

    def get_event_info_values(self):
        return dict(
            title = self['title'].value(),
            type = self['type'].value(),
            location= self['location'].value(),
            description = self['description'].value(),
            date = datetime_helpers.string_to_timestamp(self['date'].value()),
        )




