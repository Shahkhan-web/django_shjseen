from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models

from apps.core.models import BaseModel
from apps.participant import utils
from apps.participant.utils import upload_membership_certificate_to, upload_trade_license_to


class Category(BaseModel):
    name = models.CharField(max_length=255)

    def clean(self):
        # check if name is duplicate
        if Category.objects.filter(
                is_archived=False,
                name__iexact=self.name
        ).exists():
            raise ValidationError({
                'name': _('Category with this name already exists.')
            })

    def __str__(self):
        return self.name


class Participant(BaseModel):
    ORGANIZATION_TYPE_CHOICES = (
        ('private', 'Private'),
        ('government', 'Government')
    )
    ORGANIZATION_LOCATION_CHOICES = (
        ('abu_dhabi', 'Abu Dhabi'),
        ('dubai', 'Dubai'),
        ('sharjah', 'Sharjah'),
        ('ajman', 'Ajman'),
        ('umm_al_quwain', 'Umm Al Quwain'),
        ('ras_al_khaimah', 'Ras Al Khaimah'),
        ('fujairah', 'Fujairah'),
        ('oman', 'Oman'),
        ('saudi_arabia', 'Saudi Arabia'),
        ('qatar', 'qatar'),
        ('kuwait', 'Kuwait'),
        ('bahrain', 'Bahrain')
    )
    is_first_time = models.BooleanField(
        default=False,
        help_text=_('Is this first time participating in Sharjah Excellence Award ?.')
    )
    category_id = models.BigIntegerField(db_index=True)
    category_name = models.CharField(max_length=255, db_index=True)
    organization_type = models.CharField(
        max_length=10,
        choices=ORGANIZATION_TYPE_CHOICES,
        db_index=True
    )
    organization_location = models.CharField(
        max_length=14,
        choices=ORGANIZATION_LOCATION_CHOICES,
        db_index=True
    )
    organization_name = models.CharField(max_length=255)
    organization_number_of_employees = models.BigIntegerField()

    contact_person_name = models.CharField(max_length=255)
    contact_person_number = models.CharField(max_length=255)
    contact_person_email = models.EmailField()

    secondary_contact_person_name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    secondary_contact_person_number = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    secondary_contact_person_email = models.EmailField(
        null=True,
        blank=True
    )
    membership_certificate = models.FileField(
        upload_to=upload_membership_certificate_to,
        null=True,
        blank=True,
        max_length=255
    )
    trade_license = models.FileField(
        upload_to=upload_trade_license_to,
        max_length=255,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.organization_name

    def clean(self):
        # check category_id is valid
        if not Category.objects.filter(id=self.category_id).exists():
            raise ValidationError({
                'category_id': _('Category doesn\'t exists.')
            })

    def save(self, *args, **kwargs):
        self.category_name = Category.objects.get(pk=self.category_id).name
        super(Participant, self).save(*args, **kwargs)