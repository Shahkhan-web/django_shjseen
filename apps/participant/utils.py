from django.utils.text import slugify

from apps.core.utils import generate_filename


def upload_membership_certificate_to(instance, filename):
    """
    Returns path to upload to
    :param instance: instance of model
    :param filename: original filename
    :return: path
    """
    return 'membership-certificate/{}'.format(
        generate_filename(
            filename=filename,
            keyword=slugify(instance.organization_name)
        )
    )


def upload_trade_license_to(instance, filename):
    """
    Returns path to upload to
    :param instance: instance of model
    :param filename: original filename
    :return: path
    """
    return 'trade-license/{}'.format(
        generate_filename(
            filename=filename,
            keyword=slugify(instance.organization_name)
        )
    )
