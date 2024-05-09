from django import forms
from django.utils.text import slugify

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Timetablegroup

# Contain form to edit the name of a timetable group
class TimetableGroupForm(forms.ModelForm):
    timetablegroupname = forms.CharField(
        required=True,
        label='Enter your Timetable Group Name',
        help_text='Should be unique in this college',
    )

    class Meta:
        model = Timetablegroup
        fields = ['timetablegroupname']

    def __init__(self, *args, **kwargs):
        self.currentcollege = kwargs.pop('thecollege')
        self.initialname = kwargs.pop('initialname')
        super(TimetableGroupForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()

        self.helper.add_input(Submit('submit', 'Submit'))

    def clean(self):
        cleaned_data = super(TimetableGroupForm, self).clean()
        enteredname = cleaned_data.get("timetablegroupname")
        slugifiedname = slugify(enteredname)

        # Get number of items matching stream name of current college
        checkname = Timetablegroup.objects.filter(college__id=self.currentcollege.id, slug=slugifiedname).count()

        # Check if the entered name matches the initial one
        if enteredname != self.initialname:
            if checkname > 0:
                raise forms.ValidationError("The timetable group name should be unique in this college")

