from django.contrib.auth.forms import UserCreationForm


class PortalUserCreationForm(UserCreationForm):

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_portal_user = True
        user.is_active = True
        if commit:
            user.save()
        return user


class AdminUserCreationForm(UserCreationForm):

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_superuser = True
        user.is_active = True
        if commit:
            user.save()
        return user
