import csv

from django.http import HttpResponse

from apps.core import usecases


class ExportAllParticipantUseCase(usecases.BaseUseCase):

    def __init__(self, queryset):
        self._queryset = queryset

    columns = [
        "Date Time",
        "Organization Name",
        "Is First Time",
        "Category",
        "Organization Type",
        "Organization Location",
        "No. of Employees",
        "Contact Person",
        "Contact Person Number",
        "Contact Person Email",
        "Secondary Contact Person",
        "Secondary Contact Person Number",
        "Secondary Contact Person Email",
        "Member Certificate",
        "Trade License"
    ]

    def _factory(self):
        response = HttpResponse(content_type='text/csv')
        filename = 'data.csv'
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)

        # 1. write headers
        writer = csv.writer(response)
        writer.writerow(self.columns)

        for data in self._queryset:
            writer.writerow([
                data.created,
                data.organization_name,
                data.is_first_time,
                data.category_name,
                data.organization_type,
                data.organization_location,
                data.organization_number_of_employees,
                data.contact_person_name,
                data.contact_person_number,
                data.contact_person_email,
                data.secondary_contact_person_name,
                data.secondary_contact_person_number,
                data.secondary_contact_person_email,
                data.membership_certificate,
                data.trade_license
            ])
        return response
