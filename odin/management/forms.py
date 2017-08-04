from django import forms

from odin.users.models import BaseUser

from odin.education.models import Student, Course, Teacher


class ManagementAddUserForm(forms.ModelForm):
    class Meta:
        model = BaseUser
        fields = ('email', )


class AddStudentToCourseForm(forms.Form):
    use_required_attribute = False

    student = forms.ModelChoiceField(queryset=Student.objects.all())
    course = forms.ModelChoiceField(queryset=Course.objects.all())


class AddTeacherToCourseForm(forms.Form):
    use_required_attribute = False

    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all())
    course = forms.ModelChoiceField(queryset=Course.objects.all())
