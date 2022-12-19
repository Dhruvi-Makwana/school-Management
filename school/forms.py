from django import forms

from .models import Subject, Standards


class Subject1(forms.ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(Subject1, self).__init__(*args, **kwargs)
        for fieldname in self.fields:
            self.fields[fieldname].help_text = None


class Standard1(forms.ModelForm):
    # class_teacher = forms.ModelChoiceField(queryset=Standards.objects.filter(class_teacher__user_type='faculty'),empty_label=None)
    class Meta:
        model = Standards
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Standard1, self).__init__(*args, **kwargs)
        # self.fields['class_teacher'].queryset = Standards.objects.filter(class_teacher__user_type='faculty')
        for fieldname in self.fields:
            self.fields[fieldname].help_text = None

    def clean(self):
        # import pdb;pdb.set_trace()
        # print('it worked')
        cleaned_data = super().clean()
        name_check = cleaned_data['name']
        if Standards.objects.filter(name=name_check).exists():
            # print('it worked') // to check weather things go in if condition or not.
            raise forms.ValidationError(f'Standard already registered.')
        return self.cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
