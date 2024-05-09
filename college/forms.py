from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from .models import User, College, Streams, Faculties, Subjects, FacultiesRoutine
from .validators import validate_logo
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset
from django.utils.text import slugify
from django.conf import settings

# Register a user
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=50,
        required=True,
        label='Enter your first name',
    )
    last_name = forms.CharField(
        max_length=50,
        required=True,
        label='Enter your last name',
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
    
        self.fields['username'].label='Enter your username'
        self.fields['username'].help_text=None

        self.fields['password1'].label='Enter your password here'
        self.fields['password1'].help_text = "Your password should not be common, should consist of alphanumerics, should have a minimum length of eight characters and should not be similar to any of your personal information."

        self.fields['password2'].label = 'Confirm your password'
        self.fields['password2'].help_text = None

        self.helper = FormHelper()
        self.helper.form_action = 'register'

        self.helper.add_input(Submit('submit', 'Submit'))
    
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        username = cleaned_data.get("username")

        checking = User.objects.filter(username=username).count()
        if checking > 0:
            raise forms.ValidationError("The username you entered already exists")

# login in a user
class LoginForm(AuthenticationForm):
    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Enter your username'
        self.fields['password'].label = 'Enter your password'

        self.helper = FormHelper()
        self.helper.form_action = 'login'

        self.helper.add_input(Submit('submit', 'Submit'))

# Edit the first name and last name of the user.
class EditAccountForm(UserChangeForm):
    password = None

    first_name = forms.CharField(
        max_length=50,
        required=True,
        label='Enter your first name',
    )
    last_name = forms.CharField(
        max_length=50,
        required=True,
        label='Enter your last name',
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(EditAccountForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_action = 'editaccount'

        self.helper.add_input(Submit('submit', 'Submit'))


# Change password of a user.
class ChangePasswForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(ChangePasswForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].label = 'Enter your new password'
        self.fields['new_password1'].widget.attrs['class'] = 'input-text'
        self.fields['new_password1'].help_text = "Your password should not be common, should consist of alphanumerics, should have a minimum length of eight characters and should not be similar to any of your personal information."
        self.fields['new_password2'].label = 'Confirm your new password'

        self.helper = FormHelper()

        self.helper.form_action = 'changepassword'

        self.helper.add_input(Submit('submit', 'Submit'))

# Form for adding or editing the College model. Ensures college name is unique per user.
class CollegeForm(forms.ModelForm):
    collegename = forms.CharField(
        required=True,
        label='Enter your College Name',
        help_text='The college name shold be unique in your account',
    )

    collegelogo = forms.ImageField(
        required=False,
        validators=[validate_logo],
    )

    class Meta:
        model = College
        fields = ['collegename','collegelogo']

    def __init__(self, *args, **kwargs):
        self.currentuser = kwargs.pop('theuser')
        self.currentstate = kwargs.pop('thestate')
        self.initialcollegename = kwargs.pop('initialcollege')
        super(CollegeForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()

        self.helper.add_input(Submit('submit', 'Submit'))

    def clean(self):
        cleaned_data = super(CollegeForm, self).clean()
        enteredcollegename = cleaned_data.get("collegename")

        # Get number of items matching collegename of current user
        checkcollegename = College.objects.filter(user__id=self.currentuser.id, collegename=enteredcollegename).count()

        # In case one is adding a college
        if self.currentstate == 'Add':
            if checkcollegename > 0:
                raise forms.ValidationError("The college name should be unique")
        # In case one is editing a college
        else:
            # Check if the entered name matches the initial one
            if enteredcollegename != self.initialcollegename:
                if checkcollegename > 0:
                    raise forms.ValidationError("The college name should be unique")

# Form for adding or editing the Streams model. Ensures stream name is unique per college.
class StreamForm(forms.ModelForm):
    streamname = forms.CharField(
        required=True,
        label='Enter your Stream Name',
        help_text='Should be unique in this college',
    )

    class Meta:
        model = Streams
        fields = ['streamname']

    def __init__(self, *args, **kwargs):
        self.currentcollege = kwargs.pop('thecollege')
        self.currentstate = kwargs.pop('thestate')
        self.initialstreamname = kwargs.pop('initialstream')
        super(StreamForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()

        self.helper.add_input(Submit('submit', 'Submit'))

    def clean(self):
        cleaned_data = super(StreamForm, self).clean()
        enteredstreamname = cleaned_data.get("streamname")
        slugifiedstreamname = slugify(enteredstreamname)

        # Get number of items matching stream name of current college
        checkstreamname = Streams.objects.filter(college__id=self.currentcollege.id, slug=slugifiedstreamname).count()

        # In case one is adding a stream
        if self.currentstate == 'Add':
            if checkstreamname > 0:
                raise forms.ValidationError("The stream name should be unique")
        # In case one is editing a stream
        else:
            # Check if the entered name matches the initial one
            if enteredstreamname != self.initialstreamname:
                if checkstreamname > 0:
                    raise forms.ValidationError("The stream name should be unique")

# Faculties Form
class FacultiesForm(forms.ModelForm):
    facultyname = forms.CharField(
        required=True,
        label='Enter your Faculty Name',
    )

    class Meta:
        model = Faculties
        fields = ['facultyname']

    def __init__(self, *args, **kwargs):
        super(FacultiesForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()

        # Remove the form tag
        self.helper.form_tag = False

        # Create a fieldset
        self.helper.layout = Layout(
            Fieldset('', 'facultyname')
        )

# Faculties Routine Form
class FacultiesRoutineForm(forms.ModelForm):
    day = forms.ChoiceField(
        required=True,
        label='Choose the day',
        help_text='Specify a routine for all days(Sunday to Saturday). Do not repeat the same day twice.',
        choices=settings.DAYS,
    )
    starttime = forms.TimeField(
        required=True,
        label='Enter the start time of this day',
        widget=forms.TimeInput(
            attrs={
                'type': 'time',
                'required':'required',
                'value':settings.DEFAULT_FACULTY_START_TIME,
            }
        ),
    )
    endtime = forms.TimeField(
        required=True,
        label='Enter the end time of this day',
        widget=forms.TimeInput(
            attrs={
                'type': 'time',
                'required':'required',
                'value':settings.DEFAULT_FACULTY_END_TIME,
            }
        ),
    )

    class Meta:
        model = FacultiesRoutine
        fields = ['day', 'starttime', 'endtime']

class FacultiesRoutineFormHelper(FormHelper):

    def __init__(self, *args, **kwargs):
        super(FacultiesRoutineFormHelper, self).__init__(*args, **kwargs)

        # Do not show the form tag
        self.form_tag = False

        self.layout = Layout(
            Fieldset("Faculty Routine", 'day', 'starttime', 'endtime', css_class="form-title"),
        )

# Validate All Faculties Routine
class FacultyRoutine_FormSet(forms.BaseInlineFormSet):
    def clean(self):
        super(FacultyRoutine_FormSet, self).clean()

        # Store the chosen days
        thechosendays = []
        # Check days to be unique
        for form in self.forms:
            chosenday = form.cleaned_data['day']
            if chosenday in thechosendays:
                raise forms.ValidationError("You have already specified a routine for this day")
            thechosendays.append(chosenday)

            starttime = form.cleaned_data["starttime"]
            endtime = form.cleaned_data["endtime"]

            if starttime >= endtime:
                raise forms.ValidationError("The start time should be less and not equal to the endtime")

# Form for adding or editing the Faculties and Facultiesroutine models. Ensures days entered is unique per faculty. Ensure entered end time is greater the entered start time.
# Ennsure the extras are seven for each day
addfacultyroutineformset = forms.models.inlineformset_factory(
    Faculties,
    FacultiesRoutine,
    form=FacultiesRoutineForm,
    formset=FacultyRoutine_FormSet,
    extra=7,
    can_delete=False,
)
# Ensure there are no extras
editfacultyroutineformset = forms.models.inlineformset_factory(
    Faculties,
    FacultiesRoutine,
    form=FacultiesRoutineForm,
    formset=FacultyRoutine_FormSet,
    extra=0,
    can_delete=False,
)

# Form for adding or editing the Subject model. Ensures subject name is unique per college.
class SubjectsForm(forms.ModelForm):
    subjectname = forms.CharField(
        required=True,
        label='Enter your Subject Name',
        help_text='Should be unique in this college',
    )

    class Meta:
        model = Subjects
        fields = ['subjectname']

    def __init__(self, *args, **kwargs):
        self.currentcollege = kwargs.pop('thecollege')
        self.currentstate = kwargs.pop('thestate')
        self.initialsubjectname = kwargs.pop('subjectname')
        super(SubjectsForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()

        self.helper.add_input(Submit('submit', 'Submit'))

    def clean(self):
        cleaned_data = super(SubjectsForm, self).clean()
        enteredsubjectname = cleaned_data.get("subjectname")
        slugifiedsubjectname = slugify(enteredsubjectname)

        # Get number of items matching subject name of current college
        checksubjectname = Subjects.objects.filter(college__id=self.currentcollege.id, slug=slugifiedsubjectname).count()

        # In case one is adding a subject
        if self.currentstate == 'Add':
            if checksubjectname > 0:
                raise forms.ValidationError("The subject name should be unique")
        # In case one is editing a subject
        else:
            # Check if the entered name matches the initial one
            if enteredsubjectname != self.initialsubjectname:
                if checksubjectname > 0:
                    raise forms.ValidationError("The subject name should be unique")