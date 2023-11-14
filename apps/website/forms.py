from django import forms

from apps.participant.models import Participant


class ParticipateForm(forms.ModelForm):

    class Meta:
        model = Participant
        fields = (
            'is_first_time',
            'category_id',
            'organization_type',
            'organization_location',
            'organization_name',
            'organization_number_of_employees',
            'contact_person_name',
            'contact_person_number',
            'contact_person_email',
            'secondary_contact_person_name',
            'secondary_contact_person_number',
            'secondary_contact_person_email',
            'membership_certificate',
            'trade_license'
        )
