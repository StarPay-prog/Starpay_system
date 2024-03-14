from django import forms

from django.contrib.auth.models import Group, Permission
from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordResetForm


class SignupForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    # class Meta:
    #     model = NewUser
    #     fields = ('email',
    #               'first_name',
    #               'last_name',
    #               'password1',
    #               'password2',
    #             )
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


#Add User Form

class NewUserForm(forms.ModelForm):
    
    email =  forms.EmailField()
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    full_name = forms.CharField(required=True)
    
    dob = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    
    GENDER_CHOICES = (
        ('','Choose gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)


    # class Meta:
    #     model = NewUser
    #     fields = ('email',
    #               'first_name',
    #               'last_name',
    #               'gender',
    #               'avatar',
    #               'dob',
    #               'phone_number',
    #               'groups',
    #               'about',
    #               'is_active',
    #               'password1',
    #               'password2',
    #             )
    #     widgets = {
    #         'avatar': forms.FileInput(),
    #     }
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



class EditUserForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    dob = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)

    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(),required=False)
   
    GENDER_CHOICES = (
        ('','Choose gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)

    # class Meta:
    #     model = NewUser
    #     fields = ('email',
    #               'first_name',
    #               'last_name',
    #               'gender',
    #               'avatar',
    #               'dob',
    #               'phone_number',
    #               'groups',
    #               'about',
    #               'is_active',
    #             )

    #     widgets = {
    #         'avatar': forms.FileInput(),
    #     }

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save()
        return user



class UpdateMerchantForm(forms.Form):

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    business_name = forms.CharField(max_length=50)
    gst_no = forms.CharField(max_length=50)
    payin = forms.BooleanField(label="Payin", required=False)
    payout = forms.BooleanField(label="Pyaout", required=False)
    card = forms.BooleanField(label="Cards", required=False)
    cash = forms.BooleanField(label="Cash", required=False)

    def __init__(self, *args, **kwargs):
        super(UpdateMerchantForm, self).__init__(*args, **kwargs)
        merchi = kwargs["initial"]["api_data"]["data"]
        self.fields["first_name"].initial = merchi["user"]["first_name"]
        self.fields["last_name"].initial = merchi["user"]["last_name"]
        self.fields["email"].initial = merchi["user"]["email"]
        self.fields["business_name"].initial = merchi["business_name"]
        self.fields["gst_no"].initial = merchi["gst_no"]
        if "service_option" in merchi and 8008 in merchi["service_option"]:
            self.fields["cash"].initial = True
        else:
            self.fields["cash"].initial = False
        if "service_option" in merchi and 7314 in merchi["service_option"]:
            self.fields["payin"].initial = True
        else:
            self.fields["payin"].initial = False
        if "service_option" in merchi and 9819 in merchi["service_option"]:
            self.fields["payout"].initial = True
        else:
            self.fields["payout"].initial = False
        if "service_option" in merchi and 5273 in merchi["service_option"]:
            self.fields["cards"].initial = True
        else:
            self.fields["card"].initial = False



class LoginForm(forms.Form):
    email =  forms.EmailField()
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    print("cool")

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        
        return self.cleaned_data
        
    
class AdminForm(forms.Form):
    email =  forms.EmailField()
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    full_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    print("cool")

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        full_name = self.cleaned_data.get('full_name')
        phone_number = self.cleaned_data.get('phone_number')
        
        return self.cleaned_data       

class EmailValidationOnForgotPassword(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if not NewUser.objects.filter(email__iexact=email, is_active=True).exists():
            raise forms.ValidationError("There is no user registered with the specified email address!")
        return email


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name','permissions')

class PermissionsForm(forms.ModelForm):
    name = forms.CharField(label='Name', help_text="Example: Can action modelname")
    codename = forms.CharField(label='Code Name', help_text="Example: action_modelname")

    class Meta:
        model = Permission
        fields = ('name','codename','content_type')


# class UserPermissionsForm(forms.ModelForm):
#     class Meta:
#         model = NewUser
#         fields = ('user_permissions',)

class TransferMoneyForm(forms.Form):
    bank_name = forms.CharField(max_length=50)
    account_no = forms.IntegerField()
    utr_no = forms.IntegerField()
    transaction_date = forms.DateField(input_formats=['%d/%m/%Y'], required=False)
    remarks = forms.CharField(max_length=50, required=False)
    amount = forms.IntegerField(required=False)

