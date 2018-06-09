# pri

[`pri`](https://github.com/xiyusullos/PipRepositoryIndex) is a Pypi Repository Index manager that helps you to switch pypi repository fast.

Here's the `pri` usage:

```console
Usage:
  pri ls
  pri use <repository_name>
  pri current
  pri (-v | --version)
  pri (-h | --help)
Options:
  -h, --help                   output usage information
  -v, --version                output the version number

```

## Installation

```python
pip install pri
```

## Upgrading

```python
pip install --upgrade pri
```

## Examples

### List all repositories

```consoel
$ pri ls

repository name      repository url
-------------------------------------------------------------------------------
pypi                 https://pypi.python.org/simple/
tuna                 https://pypi.tuna.tsinghua.edu.cn/simple
douban               http://pypi.douban.com/simple/
aliyun               https://mirrors.aliyun.com/pypi/simple/
ustc                 https://mirrors.ustc.edu.cn/pypi/web/simple
```

### Use *tuna* repository

```console
$ pri use tuna

tuna(https://pypi.tuna.tsinghua.edu.cn/simple)
```

### List current repository
```console
$ pri current

tuna(https://pypi.tuna.tsinghua.edu.cn/simple)
```
