from django.contrib.auth.forms import UserCreationForm
from . models import User

class SignUpForm(UserCreationForm):
    # def __init__(self, *args, **kwargs):
    #     super(SignUpForm, self).__init__(*args, **kwargs)
    #     for visiable in self.visible_fields():
    #         visiable.field.widget.attrs['class'] = 'form-control'
            
    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'date_of_birth',
            'gender',
            'photo',
        ]