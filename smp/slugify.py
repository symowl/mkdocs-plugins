# Copyright (c) 2022 Symowl
# SPDX-License-Identifier: Apache-2.0

import binascii
import hashlib

from markdown.extensions.toc import slugify
from pypinyin import lazy_pinyin


def ascii(value: str, separator: str = "-") -> str:
    return slugify(value, separator)


def crc32(value: str, separator: str = "-") -> str:
    return hex(binascii.crc32(value.encode()))[2:].zfill(8)


def md5(value: str, separator: str = "-") -> str:
    return hashlib.md5(value.encode()).hexdigest()


def number(value: str, separator: str = "-") -> str:
    return "_0"


def pinyin(value: str, separator: str = "-") -> str:
    return separator.join(lazy_pinyin(slugify(value, separator, True))).replace(separator*2, separator).lower()


def sha1(value: str, separator: str = "-") -> str:
    return hashlib.sha1(value.encode()).hexdigest()


def unicode(value: str, separator: str = "-") -> str:
    return slugify(value, separator, True)
