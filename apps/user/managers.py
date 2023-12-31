from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, email, password=None, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        if not password:
            raise ValueError('Superusers must have a password.')

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class PortalUserManager(BaseUserManager):
    def get_queryset(self):
        return super(PortalUserManager, self).get_queryset().filter(
            is_staff=False,
            is_superuser=False,
            is_portal_user=True,
        )

    def create(self, email, password, **kwargs):
        kwargs.update({
            'is_staff': False,
            'is_superuser': False,
            'is_portal_user': True
        })
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user


class AdminUserManager(BaseUserManager):
    def get_queryset(self):
        return super(AdminUserManager, self).get_queryset().filter(
            is_superuser=True,
            is_portal_user=False,
        )

    def create(self, email, password, **kwargs):
        kwargs.update({
            'is_staff': False,
            'is_superuser': True,
            'is_portal_user': False
        })
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
