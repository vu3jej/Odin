from django import forms

from .models import ApplicationInfo, Application


class DateInput(forms.DateInput):
    input_type = 'date'


class ApplicationInfoModelForm(forms.ModelForm):
    class Meta:
        model = ApplicationInfo
        fields = [
            'course',
            'start_date',
            'end_date',
            'start_interview_date',
            'end_interview_date',
            'description',
            'external_application_form'
        ]

        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
            'start_interview_date': DateInput(),
            'end_interview_date': DateInput()
        }


class ApplicationCreateForm(forms.ModelForm):
    full_name = forms.CharField()

    class Meta:
        model = Application
        fields = [
            'application_info',
            'user',
            'full_name',
            'phone',
            'skype',
            'works_at',
            'studies_at',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['phone'].required = True
        self.fields['skype'].required = True
        self.fields['works_at'].required = True
        self.fields['studies_at'].required = True


class ApplicationEditForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'phone',
            'skype',
            'works_at',
            'studies_at'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['phone'].required = True
        self.fields['skype'].required = True
        self.fields['works_at'].required = True
        self.fields['studies_at'].required = True
