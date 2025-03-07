"""Validate Anything!"""
# -*- coding: utf-8 -*-

from .between import between
from .btc_address import btc_address
from .card import amex, card_number, diners, discover, jcb, mastercard, unionpay, visa
from .domain import domain
from .email import email
from .hashes import md5, sha1, sha224, sha256, sha512
from .hostname import hostname
from .i18n import fi_business_id, fi_ssn
from .iban import iban
from .ip_address import ipv4, ipv6
from .length import length
from .mac_address import mac_address
from .slug import slug
from .url import url
from .utils import ValidationFailure, validator
from .uuid import uuid

__all__ = (
    "amex",
    "between",
    "btc_address",
    "card_number",
    "diners",
    "discover",
    "domain",
    "email",
    "fi_business_id",
    "fi_ssn",
    "hostname",
    "iban",
    "ipv4",
    "ipv6",
    "jcb",
    "length",
    "mac_address",
    "mastercard",
    "md5",
    "sha1",
    "sha224",
    "sha256",
    "sha512",
    "slug",
    "unionpay",
    "url",
    "uuid",
    "ValidationFailure",
    "validator",
    "visa",
)

__version__ = "0.20.0"
