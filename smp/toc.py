from typing import Any, Dict

from markdown.extensions import Extension
from markdown.extensions.toc import TocExtension

from .slugify import ascii, crc32, md5, number, pinyin, sha1, unicode


def makeExtension(**kwargs: Dict[str, Any]) -> Extension:
    mode = kwargs.get("slugify")
    if mode in ["crc", "crc32"]:
        kwargs["slugify"] = crc32
    elif mode == "md5":
        kwargs["slugify"] = md5
    elif mode in ["num", "number"]:
        kwargs["slugify"] = number
    elif mode == "pinyin":
        kwargs["slugify"] = pinyin
    elif mode == "sha1":
        kwargs["slugify"] = sha1
    elif mode == "unicode":
        kwargs["slugify"] = unicode
    else:
        kwargs["slugify"] = ascii
    return TocExtension(**kwargs)
