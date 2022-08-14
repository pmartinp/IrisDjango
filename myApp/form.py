from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationform(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email", )