# Copyright (c) 2022 Symowl
# SPDX-License-Identifier: Apache-2.0

from binascii import crc32 as _crc32
from hashlib import md5 as _md5
from hashlib import sha1 as _sha1

from markdown.extensions.toc import slugify
from pypinyin import lazy_pinyin


def ascii(value: str, separator: str = "-") -> str:
    return slugify(value, separator)


def crc32(value: str, separator: str = "-") -> str:
    return hex(_crc32(value.encode()))[2:].zfill(8)


def md5(value: str, separator: str = "-") -> str:
    return _md5(value.encode()).hexdigest()


def number(value: str, separator: str = "-") -> str:
    return "_0"


def pinyin(value: str, separator: str = "-") -> str:
    return separator.join(lazy_pinyin(slugify(value, separator, True))).replace(separator*2, separator).lower()


def sha1(value: str, separator: str = "-") -> str:
    return _sha1(value.encode()).hexdigest()


def unicode(value: str, separator: str = "-") -> str:
    return slugify(value, separator, True)
