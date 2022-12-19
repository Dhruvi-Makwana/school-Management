from django import forms

from .models import User


class Adduser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'mobile_number','user_type','gender']

    def __init__(self, *args, **kwargs):
        super(Adduser, self).__init__(*args, **kwargs)
        # self.fields['user_type'] = 'student'
        for fieldname in self.fields:
            self.fields[fieldname].help_text = None

    def clean_username(self):
        username_check = self.cleaned_data['username']
        if username_check.isalpha() is False:
            raise forms.ValidationError('username not contain any number')
        return username_check

    def clean_last_name(self):
        # import pdb;pdb.set_trace()
        # cleaned_data = super().clean()
        # username_check = self.cleaned_data['username']
        firstname_check = self.cleaned_data['first_name']
        lastname_check = self.cleaned_data['last_name']
        # pass_check = cleaned_data['password']
        # type_check = cleaned_data['user_type']
        # number_check = cleaned_data['mobile_number']
        # # if username_check.isdigit() is False:
        # #     raise forms.ValidationError('username not contain any number')
        if firstname_check == lastname_check:
            # print('it worked') // to check weather things go in if condition or not.
            raise forms.ValidationError('Firstname and Last name cannot be same')
        return lastname_check

    def clean_password(self):
        pass_check = self.cleaned_data['password']
        if len(pass_check) > 8:
            raise forms.ValidationError('Password is not grater than 8 character')
        return pass_check

    def clean_mobile_number(self):
        number_check = self.cleaned_data['mobile_number']
        print(number_check.isnumeric())
        if len(number_check) < 10 or number_check.isnumeric() is False:
            raise forms.ValidationError('Enter a valid phone number')
        return number_check

    def clean_user_type(self):
        type_check = self.cleaned_data['user_type']
        if type_check != 'student':
            raise forms.ValidationError(f'Must select student type')
        return type_check

