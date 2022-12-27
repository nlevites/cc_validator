import sys
import re
from typing import Union


class Validator:
    def __init__(self, cc_num: str) -> None:
        self.cc_num = cc_num
        self.supported_regex = {
            "master_card": "^5[1-5][0-9]{14}|^(222[1-9]|22[3-9]\\d|2[3-6]\\d{2}|27[0-1]\\d|2720)[0-9]{12}$",
            "visa": "^4[0-9]{12}(?:[0-9]{3})?$",
            "amex": "^3[47][0-9]{13}$",
        }
        # run validation
        self.validate()

    def validate_luhn(self) -> None:
        # https://en.wikipedia.org/wiki/Luhn_algorithm
        # convert number to list
        split: list = list(map(int, self.cc_num.strip()))
        split.reverse()
        # double every other value after checksum key, if > 9, subtract 9
        for i in range(1, len(split), 2):
            doubled = split[i] * 2
            split[i] = doubled - 9 if doubled > 9 else doubled
        # check luhn'd sum is divisible by 10
        if sum(split) % 10 != 0:
            raise AssertionError("failed luhn algorithm")

    def validate_regex(self) -> None:
        # iterate through supported card regex
        for regex in self.supported_regex.values():
            if re.match(regex, self.cc_num):
                return
        # if no match, raise AssertionError (matches is None)
        raise AssertionError("regex match failed")

    def validate(self) -> None:
        # call luhn validation
        self.validate_luhn()
        # call regex validation
        self.validate_regex()


def validate(cc_num: Union[str, int]) -> None:
    try:
        # parse and validate cli arg from user
        cc_num = str(int(cc_num))
    except (TypeError, ValueError):
        exit("must supply valid credit card number")
    try:
        Validator(cc_num)
        print("valid")
    except AssertionError as err:
        exit(str(err))


if __name__ == "__main__":
    validate(*sys.argv[1:])
