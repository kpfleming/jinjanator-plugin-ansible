# jinjanator-plugin-ansible

<a href="https://opensource.org"><img height="150" align="left" src="https://opensource.org/files/OSIApprovedCropped.png" alt="Open Source Initiative Approved License logo"></a>
[![CI](https://github.com/kpfleming/jinjanator-plugin-ansible/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/kpfleming/jinjanator-plugin-ansible/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/release/python-31019/)
[![License - Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-9400d3.svg)](https://spdx.org/licenses/Apache-2.0.html)
[![Code Style - Black](https://img.shields.io/badge/Code%20Style-Black-000000.svg)](https://github.com/psf/black)
[![Types - Mypy](https://img.shields.io/badge/Types-Mypy-blue.svg)](https://github.com/python/mypy)
[![Code Quality - Ruff](https://img.shields.io/badge/Code%20Quality-Ruff-red.svg)](https://github.com/astral-sh/ruff)
[![Project Management - Hatch](https://img.shields.io/badge/Project%20Management-Hatch-purple.svg)](https://github.com/pypa/hatch)
[![Testing - Pytest](https://img.shields.io/badge/Testing-Pytest-orange.svg)](https://github.com/pytest-dev/pytest)

This repo contains `jinjanator-plugin-ansible`, a plugin which
provides access to Ansible's filters to templates rendered using the
[jinjanator](https://github.com/kpfleming/jinjanator) tool.

Open Source software: [Apache License 2.0](https://spdx.org/licenses/Apache-2.0.html)

## &nbsp;
<!-- fancy-readme start -->

This plugin makes all of the filters and tests from the Ansible 'core'
collection available to templates being rendered using the jinjanator
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

If you'd like to chat with the jinjanator community, join us on
[Matrix](https://matrix.to/#/#jinjanator:km6g.us)!

## Credits

["Standing on the shoulders of
giants"](https://en.wikipedia.org/wiki/Standing_on_the_shoulders_of_giants)
could not be more true than it is in the Python community; this
project relies on many wonderful tools and libraries produced by the
global open source software community, in addition to Python
itself. I've listed many of them below, but if I've overlooked any
please do not be offended :-)

* [Black](https://pypi.org/project/black)
* [Hatch-Fancy-PyPI-Readme](https://pypi.org/project/hatch-fancy-pypi-readme)
* [Hatch](https://pypi.org/project/hatch)
* [Mypy](https://pypi.org/project/mypy)
* [pyproject-fmt](https://pypi.org/project/pyproject-fmt)
* [Pytest](https://pypi.org/project/pytest)
* [Ruff](https://pypi.org/project/ruff)
* [Towncrier](https://pypi.org/project/towncrier)
