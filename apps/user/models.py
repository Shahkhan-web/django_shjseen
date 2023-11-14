from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel
from apps.user import managers
from apps.user.managers import UserManager
from apps.user.validators import validate_username


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        _('email address'),
        unique=True
    )
    fullname = models.CharField(_('fullname'), max_length=200, null=True)
    username = models.CharField(
        _('username'),
        max_length=150,
        null=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[validate_username],
    )
    is_portal_user = models.BooleanField(
        _('portal user'),
        default=False,
        help_text=_(
            'Designates whether this user is portal user or not. '
            'Unselect this if user is not a portal user.'
        ),
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_archived = models.BooleanField(default=False)

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname']
    objects = UserManager()

    def __str__(self):
        return self.email

    def clean(self):
        django_user = bool(self.is_superuser or self.is_staff)

        if self.is_portal_user and django_user:
            raise DjangoValidationError(
                _('User can\'t be portal user and django user at once')
            )

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super(User, self).save(*args, **kwargs)

    def archive(self):
        if self.is_archived:
            raise DjangoValidationError({
                'non_field_errors': _('Failed - it is already archived.')
            })
        self.is_archived = True
        self.save(update_fields=['is_archived'])

    def restore(self):
        if not self.is_archived:
            raise DjangoValidationError({
                'non_field_errors': _('Failed - it is already restored.')
            })
        self.is_archived = False
        self.save(update_fields=['is_archived'])


class PortalUser(User):
    objects = managers.PortalUserManager()

    class Meta:
        proxy = True


class AdminUser(User):
    objects = managers.AdminUserManager()

    class Meta:
        proxy = True
