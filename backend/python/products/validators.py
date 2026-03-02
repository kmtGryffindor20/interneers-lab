from django.core.exceptions import ValidationError

def validate_positive(value):
    """
    Validator to ensure a value is positive.
    Raises a ValidationError if the value is not positive.
    """
    if value <= 0:
        raise ValidationError(f"Value must be positive. Received: {value}")