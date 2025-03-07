"""Hostname."""
# -*- coding: utf-8 -*-

# standard
from functools import lru_cache
import re

# local
from .ip_address import ipv4, ipv6
from .utils import validator
from .domain import domain


@lru_cache
def _port_regex():
    """Port validation regex."""
    return re.compile(
        r"^\:(6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|"
        + r"6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{0,3})$",
    )


@lru_cache
def _simple_hostname_regex():
    """Simple hostname validation regex."""
    return re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9-]{0,61}[a-zA-Z0-9]$")


def _port_validator(value: str):
    """Returns host segment if port is valid."""
    if value.count("]:") == 1:
        # with ipv6
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg.lstrip("[").rstrip("]")

    if value.count(":") == 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg


@validator
def hostname(
    value: str,
    /,
    *,
    may_have_port: bool = True,
    skip_ip_addr: bool = False,
    maybe_simple: bool = True,
    rfc_1034: bool = False,
    rfc_2782: bool = False,
):
    """Return whether or not given value is a valid hostname.

    Examples:
        >>> hostname("ubuntu-pc:443")
        # Output: True
        >>> hostname("this-pc")
        # Output: True
        >>> hostname("xn----gtbspbbmkef.xn--p1ai:65535")
        # Output: True
        >>> hostname("_example.com")
        # Output: True
        >>> hostname("123.5.77.88:31000")
        # Output: True
        >>> hostname("12.12.12.12")
        # Output: True
        >>> hostname("[::1]:22")
        # Output: True
        >>> hostname("dead:beef:0:0:0:0000:42:1")
        # Output: True
        >>> hostname("[0:0:0:0:0:ffff:1.2.3.4]:-65538")
        # Output: ValidationFailure(func=hostname, ...)
        >>> hostname("[0:&:b:c:@:e:f::]:9999")
        # Output: ValidationFailure(func=hostname, ...)

    Args:
        value:
            Hostname string to validate.
        may_have_port:
            Hostname string may contain port number.
        skip_ip_addr:
            When hostname string cannot be an IP address.
        maybe_simple:
            Hostname string maybe only hyphens and alpha-numerals.
        rfc_1034:
            Allow trailing dot in domain/host name.
            Ref: [RFC 1034](https://www.rfc-editor.org/rfc/rfc1034).
        rfc_2782:
            Domain/Host name is of type service record.
            Ref: [RFC 2782](https://www.rfc-editor.org/rfc/rfc2782).

    Returns:
        (Literal[True]):
            If `value` is a valid hostname.
        (ValidationFailure):
            If `value` is an invalid hostname.

    > *New in version 0.21.0*.
    """
    if may_have_port and (host_seg := _port_validator(value)):
        return (
            (_simple_hostname_regex().match(host_seg) if maybe_simple else False)
            or domain(host_seg, rfc_1034=rfc_1034, rfc_2782=rfc_2782)
            or (False if skip_ip_addr else ipv4(host_seg, cidr=False))
            or (False if skip_ip_addr else ipv6(host_seg, cidr=False))
        )

    return (
        (_simple_hostname_regex().match(value) if maybe_simple else False)
        or domain(value, rfc_1034=rfc_1034, rfc_2782=rfc_2782)
        or (False if skip_ip_addr else ipv4(value, cidr=False))
        or (False if skip_ip_addr else ipv6(value, cidr=False))
    )
