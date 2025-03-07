"""Card."""
# -*- coding: utf-8 -*-

# standard
import re

# local
from .utils import validator


@validator
def card_number(value: str, /):
    """Return whether or not given value is a valid generic card number.

    This validator is based on [Luhn's algorithm][1].

    [1]: https://github.com/mmcloughlin/luhn

    Examples:
        >>> card_number('4242424242424242')
        # Output: True
        >>> card_number('4242424242424241')
        # Output: ValidationFailure(func=card_number, args={'value': '4242424242424241'})

    Args:
        value:
            Generic card number string to validate

    Returns:
        (Literal[True]):
            If `value` is a valid generic card number.
        (ValidationFailure):
            If `value` is an invalid generic card number.

    > *New in version 0.15.0*.
    """
    try:
        digits = list(map(int, value))
        odd_sum = sum(digits[-1::-2])
        even_sum = sum(sum(divmod(2 * d, 10)) for d in digits[-2::-2])
        return (odd_sum + even_sum) % 10 == 0
    except ValueError:
        return False


@validator
def visa(value: str, /):
    """Return whether or not given value is a valid Visa card number.

    Examples:
        >>> visa('4242424242424242')
        # Output: True
        >>> visa('2223003122003222')
        # Output: ValidationFailure(func=visa, args={'value': '2223003122003222'})

    Args:
        value:
            Visa card number string to validate

    Returns:
        (Literal[True]):
            If `value` is a valid Visa card number.
        (ValidationFailure):
            If `value` is an invalid Visa card number.

    > *New in version 0.15.0*.
    """
    pattern = re.compile(r"^4")
    return card_number(value) and len(value) == 16 and pattern.match(value)


@validator
def mastercard(value: str, /):
    """Return whether or not given value is a valid Mastercard card number.

    Examples:
        >>> mastercard('5555555555554444')
        # Output: True
        >>> mastercard('4242424242424242')
        # Output: ValidationFailure(func=mastercard, args={'value': '4242424242424242'})

    Args:
        value:
            Mastercard card number string to validate

    Returns:
        (Literal[True]):
            If `value` is a valid Mastercard card number.
        (ValidationFailure):
            If `value` is an invalid Mastercard card number.

    > *New in version 0.15.0*.
    """
    pattern = re.compile(r"^(51|52|53|54|55|22|23|24|25|26|27)")
    return card_number(value) and len(value) == 16 and pattern.match(value)


@validator
def amex(value: str, /):
    """Return whether or not given value is a valid American Express card number.

    Examples:
        >>> amex('378282246310005')
        # Output: True
        >>> amex('4242424242424242')
        # Output: ValidationFailure(func=amex, args={'value': '4242424242424242'})

    Args:
        value:
            American Express card number string to validate

    Returns:
        (Literal[True]):
            If `value` is a valid American Express card number.
        (ValidationFailure):
            If `value` is an invalid American Express card number.

    > *New in version 0.15.0*.
    """
    pattern = re.compile(r"^(34|37)")
    return card_number(value) and len(value) == 15 and pattern.match(value)


@validator
def unionpay(value: str, /):
    """Return whether or not given value is a valid UnionPay card number.

    Examples:
        >>> unionpay('6200000000000005')
        # Output: True
        >>> unionpay('4242424242424242')
        # Output: ValidationFailure(func=unionpay, args={'value': '4242424242424242'})

    Args:
        value:
            UnionPay card number string to validate

    Returns:
        (Literal[True]):
            If `value` is a valid UnionPay card number.
        (ValidationFailure):
            If `value` is an invalid UnionPay card number.

    > *New in version 0.15.0*.
    """
    pattern = re.compile(r"^62")
    return card_number(value) and len(value) == 16 and pattern.match(value)


@validator
def diners(value: str, /):
    """Return whether or not given value is a valid Diners Club card number.

    Examples:
        >>> diners('3056930009020004')
        # Output: True
        >>> diners('4242424242424242')
        # Output: ValidationFailure(func=diners, args={'value': '4242424242424242'})

    Args:
        value:
            Diners Club card number string to validate

    Returns:
        (Literal[True]):
            If `value` is a valid Diners Club card number.
        (ValidationFailure):
            If `value` is an invalid Diners Club card number.

    > *New in version 0.15.0*.
    """
    pattern = re.compile(r"^(30|36|38|39)")
    return card_number(value) and len(value) in {14, 16} and pattern.match(value)


@validator
def jcb(value: str, /):
    """Return whether or not given value is a valid JCB card number.

    Examples:
        >>> jcb('3566002020360505')
        # Output: True
        >>> jcb('4242424242424242')
        # Output: ValidationFailure(func=jcb, args={'value': '4242424242424242'})

    Args:
        value:
            JCB card number string to validate

    Returns:
        (Literal[True]):
            If `value` is a valid JCB card number.
        (ValidationFailure):
            If `value` is an invalid JCB card number.

    > *New in version 0.15.0*.
    """
    pattern = re.compile(r"^35")
    return card_number(value) and len(value) == 16 and pattern.match(value)


@validator
def discover(value: str, /):
    """Return whether or not given value is a valid Discover card number.

    Examples:
        >>> discover('6011111111111117')
        # Output: True
        >>> discover('4242424242424242')
        # Output: ValidationFailure(func=discover, args={'value': '4242424242424242'})

    Args:
        value:
            Discover card number string to validate

    Returns:
        (Literal[True]):
            If `value` is a valid Discover card number.
        (ValidationFailure):
            If `value` is an invalid Discover card number.

    > *New in version 0.15.0*.
    """
    pattern = re.compile(r"^(60|64|65)")
    return card_number(value) and len(value) == 16 and pattern.match(value)
