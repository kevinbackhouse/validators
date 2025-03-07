"""eMail."""
# -*- coding: utf-8 -*-

# standard
import re

# local
from .hostname import hostname
from .utils import validator


@validator
def email(
    value: str,
    /,
    *,
    simple_host: bool = False,
    ip_address: bool = False,
    rfc_1034: bool = False,
    rfc_2782: bool = False,
):
    """Validate an email address.

    This was inspired from [Django's email validator][1].
    Also ref: [RFC 1034][2], [RFC 5321][3] and [RFC 5322][4].

    [1]: https://github.com/django/django/blob/main/django/core/validators.py#L174
    [2]: https://www.rfc-editor.org/rfc/rfc1034
    [3]: https://www.rfc-editor.org/rfc/rfc5321
    [4]: https://www.rfc-editor.org/rfc/rfc5322

    Examples:
        >>> email('someone@example.com')
        # Output: True
        >>> email('bogus@@')
        # Output: ValidationFailure(email=email, args={'value': 'bogus@@'})

    Args:
        value:
            eMail string to validate.
        simple_host:
            When the domain part is a simple hostname.
        ip_address:
            When the domain part is an IP address.
        rfc_1034:
            Allow trailing dot in domain name.
            Ref: [RFC 1034](https://www.rfc-editor.org/rfc/rfc1034).
        rfc_2782:
            Domain name is of type service record.
            Ref: [RFC 2782](https://www.rfc-editor.org/rfc/rfc2782).

    Returns:
        (Literal[True]):
            If `value` is a valid eMail.
        (ValidationFailure):
            If `value` is an invalid eMail.

    > *New in version 0.1.0*.
    """
    if not value or value.count("@") != 1:
        return False

    username_part, domain_part = value.rsplit("@", 1)

    if len(username_part) > 64 or len(domain_part) > 253:
        # ref: RFC 1034 and 5231
        return False

    if ip_address:
        if domain_part.startswith("[") and domain_part.endswith("]"):
            # ref: RFC 5321
            domain_part = domain_part.lstrip("[").rstrip("]")
        else:
            return False

    return (
        bool(
            hostname(
                domain_part,
                skip_ip_addr=not ip_address,
                may_have_port=False,
                maybe_simple=simple_host,
                rfc_1034=rfc_1034,
                rfc_2782=rfc_2782,
            )
        )
        if re.match(
            # dot-atom
            r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*$"
            # quoted-string
            + r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-\011\013\014\016-\177])*"$)',
            username_part,
            re.IGNORECASE,
        )
        else False
    )
