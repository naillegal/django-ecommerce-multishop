from django import forms
from django.contrib.auth.models import User
from .models import Contact,Customer,ResetPassword




class ContactForm(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=Contact
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Your name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Your email'}),
            'subject':forms.TextInput(attrs={'class':'form-control','placeholder':'Subject'}),
            'message':forms.Textarea(attrs={'class':'form-control','placeholder':'Message','rows':'8'}),
        }



class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control',}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control',}))
    email = forms.EmailField(max_length=50,widget=forms.EmailInput(attrs={'class':'form-control',}))
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control',}))
    password = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control',}))
    password2 = forms.CharField(max_length=50,label='Password again',widget=forms.PasswordInput(attrs={'class':'form-control',}))

    def clean(self):
        cleaned_data=super().clean()
        password=cleaned_data.get('password')
        password2=cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise forms.ValidationError('Sifreler eyni deyil!')
        
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('Bu email movcuddur!')
        return email
    
    def clean_username(self):
        username=self.cleaned_data.get('username')
        if username and User.objects.filter(username=username).exists():
            raise forms.ValidationError('Bu username movcuddur!')
        return username


    def save(self):
        cleaned_data=self.cleaned_data
        username=cleaned_data.get('username')
        first_name=cleaned_data.get('first_name')
        last_name=cleaned_data.get('last_name')
        email=cleaned_data.get('email')
        password=cleaned_data.get('password')

        new_user=User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
         )
        customer = Customer.objects.create(user=new_user)
        return customer


class PasswordResetForm(forms.Form):
    token = forms.CharField(widget=forms.HiddenInput())
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    password_again = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password Again'}))


    def clean(self):
        cleaned_data = super().clean()
        token = cleaned_data['token']
        username = cleaned_data['username']
        password = cleaned_data['password']
        password_again = cleaned_data['password_again']
        rp = ResetPassword.objects.filter(token=token).first()
        user = User.objects.filter(username=username).first()
        if not user:
            raise forms.ValidationError('This username doesn\'t exist')
        if not rp or rp.user != user:
            raise forms.ValidationError('Process failed')
        
        if password and password_again and password != password_again:
            raise forms.ValidationError('Passwords are not same!')
        
        return cleaned_data
    

    def save(self):
        cleaned_data = self.cleaned_data
        username = cleaned_data['username']
        password = cleaned_data['password']
        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()
        rp = ResetPassword.objects.get(token=cleaned_data['token'])
        rp.used = True
        rp.save()
        return user