# jinjanator-plugin-ansible

<a href="https://opensource.org"><img height="150" align="left" src="https://opensource.org/files/OSIApprovedCropped.png" alt="Open Source Initiative Approved License logo"></a>
[![CI](https://github.com/kpfleming/jinjanator-plugin-ansible/workflows/CI%20checks/badge.svg)](https://github.com/kpfleming/jinjanator-plugin-ansible/actions?query=workflow%3ACI%20checks)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-3912/)
[![License - Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-9400d3.svg)](https://spdx.org/licenses/Apache-2.0.html)
[![Code Style - Black](https://img.shields.io/badge/Code%20Style-Black-000000.svg)](https://github.com/psf/black)
[![Types - Mypy](https://img.shields.io/badge/Types-Mypy-blue.svg)](https://github.com/python/mypy)
[![Code Quality - Ruff](https://img.shields.io/badge/Code%20Quality-Ruff-red.svg)](https://github.com/astral-sh/ruff)
[![Project Management - Hatch](https://img.shields.io/badge/Project%20Management-Hatch-purple.svg)](https://github.com/pypa/hatch)
[![Testing - Pytest](https://img.shields.io/badge/Testing-Pytest-orange.svg)](https://github.com/pytest-dev/pytest)

This repo contains `jinjanator-plugin-ansible`, a plugin which
provides access to Ansible's filters to templates rendered using the
[Jinjanator](https://github.com/kpfleming/jinjanator) tool.

Open Source software: [Apache License 2.0](https://spdx.org/licenses/Apache-2.0.html)

## &nbsp;
<!-- fancy-readme start -->

This plugin makes all of the filters and tests from the Ansible 'core'
collection available to templates being rendered using the Jinjanator
tool.

## Installation

```
pip install jinjanator-plugin-ansible
```

## Usage

The Ansible filters and tests can be used in templates using the same
names that would be used if the template was rendered by Ansible
itself.
<!-- fancy-readme end -->

## Chat

If you'd like to chat with the Jinjanator community, join us on
[Matrix](https://matrix.to/#/#jinjanator:km6g.us)!

## Credits

["Standing on the shoulders of
giants"](https://en.wikipedia.org/wiki/Standing_on_the_shoulders_of_giants)
could not be more true than it is in the Python community; this
project relies on many wonderful tools and libraries produced by the
global open source software community, in addition to Python
itself. I've listed many of them below, but if I've overlooked any
please do not be offended :-)

* [Black](https://github.com/psf/black)
* [Hatch-Fancy-PyPI-Readme](https://github.com/hynek/hatch-fancy-pypi-readme)
* [Hatch](https://github.com/pypa/hatch)
* [Mypy](https://github.com/python/mypy)
* [Pytest](https://github.com/pytest-dev/pytest)
* [Ruff](https://github.com/astral-sh/ruff)
* [Towncrier](https://github.com/twisted/towncrier)
