from django.utils.deconstruct import deconstructible


@deconstructible
class Validator:
    message = None
    code = 'invalid'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        raise NotImplementedError("Subclasses should implement this!")

    def __eq__(self, other):
        return (
                isinstance(other, Validator) and
                (self.message == other.message) and
                (self.code == other.code)
        )
