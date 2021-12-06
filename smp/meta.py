# Copyright (c) 2021 Symowl
# SPDX-License-Identifier: MIT

from typing import Dict, List, Union

from mkdocs.config.base import Config
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page


class MetaPlugin(BasePlugin):
    def on_page_markdown(self, markdown: str, page: Page, config: Config, files: Files) -> None:
        page.meta = get_meta(markdown, page.meta)


def get_meta(markdown: str, yaml_meta: Dict[str, str]) -> Dict[str, Union[List[str], str]]:
    meta: Dict[str, Union[List[str], str]] = {}

    for k, v in yaml_meta.items():
        if k in ["hide", "tags"]:
            meta[k] = [vv.strip() for vv in v.split(",")]
        else:
            meta[k] = v

    for v in markdown.replace('\r\n', '\n').replace('\r', '\n').split('\n'):
        if v[:2] == "# ":
            meta["title"] = v[2:].strip()

    return meta
