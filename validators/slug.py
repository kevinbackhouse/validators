"""Slug."""
# -*- coding: utf-8 -*-

# standard
import re

# local
from .utils import validator


@validator
def slug(value: str, /):
    """Validate whether or not given value is valid slug.

    Valid slug can contain only lowercase alphanumeric characters and hyphens.
    It starts and ends with these lowercase alphanumeric characters.

    Examples:
        >>> slug('my-slug-2134')
        # Output: True
        >>> slug('my.slug')
        # Output: ValidationFailure(func=slug, args={'value': 'my.slug'})

    Args:
        value:
            Slug string to validate.

    Returns:
        (Literal[True]):
            If `value` is a valid slug.
        (ValidationFailure):
            If `value` is an invalid slug.

    > *New in version 0.6.0*.
    """
    return re.match(r"^[a-z0-9]+(?:-[a-z0-9]+)*$", value)
