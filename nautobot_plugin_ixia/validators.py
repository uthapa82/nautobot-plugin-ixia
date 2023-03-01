"""validators.py"""

from django.core.validators import RegexValidator


NTMValidator = RegexValidator(
    regex='NTM[1-3]\sM([0-9]|10)\sP([0-9][0-6]|[0-9])',
    message="Invalid Format, NTM[1-3]<space>M[0-10]<space>P[1-96]",
    code="invalid",
)