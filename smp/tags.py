from binascii import crc32
from os.path import exists
from typing import Dict, List, Union

from jinja2 import Environment, FileSystemLoader
from mkdocs.config.base import Config
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import File, Files
from mkdocs.utils.meta import get_data

from .meta import get_meta


class TagsPlugin(BasePlugin):
    def gen_tags_md(self, docs_dir: str, tags: Dict[str, List[str]]) -> None:
        env = Environment(loader=FileSystemLoader(docs_dir))
        template = env.get_template("tags.md.j2")
        new_data = template.render(tags=tags).encode()

        path = f"{docs_dir}/tags.md"
        if exists(path):
            with open(path, "rb") as f:
                old_data = f.read()
        else:
            old_data = b""

        if crc32(new_data) != crc32(old_data):
            with open(path, "wb") as f:
                f.write(new_data)

    def on_files(self, files: Files, config: Config) -> Files:
        docs_dir: str = config["docs_dir"]
        new_files = Files([])
        tags: Dict[str, List[str]] = {}
        for f in files:
            f: File = f
            if f.url == "tags.md.j2":
                continue
            f.url = f.url.replace("index.html", "")
            new_files.append(f)

            if not f.src_path.endswith(".md"):
                continue

            with open(f"{docs_dir}/{f.src_path}", encoding="utf-8") as f_md:
                markdown = f_md.read()
            meta: Dict[str, Union[List[str], str]] = get_meta(
                markdown,
                get_data(markdown)[1]
            )

            title = meta.get("title")
            if title is None:
                continue

            hide = meta.get("hide")
            if hide is not None:
                if "tags" in hide:
                    continue

            meta_tags = meta.get("tags")
            if meta_tags is None:
                continue

            base_uri = config["site_url"].split("/", 3)[-1]
            for tag in meta_tags:
                if tag not in tags:
                    tags[tag] = []
                tags[tag].append({
                    "title": title,
                    "uri": f"/{base_uri}{f.url}"
                })

        self.gen_tags_md(docs_dir, {tag: tags[tag] for tag in sorted(tags)})
        return new_files
