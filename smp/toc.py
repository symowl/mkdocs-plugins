# Copyright (c) 2022 Symowl
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict

from markdown.extensions import Extension
from markdown.extensions.toc import TocExtension

from smp.slugify import ascii, crc32, md5, number, pinyin, sha1, unicode

MODES = {
    "ascii": ascii,
    "crc": crc32,
    "crc32": crc32,
    "md5": md5,
    "num": number,
    "number": number,
    "pinyin": pinyin,
    "sha1": sha1,
    "unicode": unicode
}


def makeExtension(**kwargs: Dict[str, Any]) -> Extension:
    mode = kwargs.get("slugify")
    if mode in MODES:
        kwargs["slugify"] = MODES[mode]
    else:
        kwargs["slugify"] = ascii
    return TocExtension(**kwargs)
