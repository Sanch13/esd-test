from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django import forms

from users.models import User


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите фамилию'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя '
                                                                            'пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Введите адрес эл. '
                                                                          'почты'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите '
                                                                                 'пароль'}))
    tab_number = forms.IntegerField(min_value=0,
                                    max_value=100000,
                                    widget=forms.NumberInput(attrs={
                                        'placeholder': 'Введите табельный номер'}),
                                    required=False)

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'tab_number')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field_name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control'


class UserLoginForm(AuthenticationForm):  # Унаследовали форму от Джанго
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя '
                                                                            'пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
    # переопределяем username, password из стандартной формы Джанго

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control'
