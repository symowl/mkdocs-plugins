# Symowl MkDocs Plugins

## Install this package

``` sh
pip install git+https://github.com/symowl/mkdocs-plugins.git@1.9.2
```

> If getting this package from GitHub is slow. You can try this command to get.

``` sh
pip install git+https://gitee.com/symowl/mkdocs-plugins.git@1.9.2
```

## How to use

``` yml
# mkdocs.yml
markdown_extensions:
  - smp.toc:
      slugify: ascii | crc | crc32 | num | number | pinyin | sha1 | unicode # default: ascii
```
