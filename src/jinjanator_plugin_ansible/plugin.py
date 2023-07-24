from __future__ import annotations

from typing import cast

from ansible.plugins.filter.core import FilterModule  # type: ignore[import]
from ansible.plugins.test.core import TestModule  # type: ignore[import]
from jinjanator_plugins import (
    Filters,
    Tests,
    plugin_filters_hook,
    plugin_tests_hook,
)


@plugin_filters_hook
def plugin_filters() -> Filters:
    return cast(Filters, FilterModule().filters())


@plugin_tests_hook
def plugin_tests() -> Tests:
    return cast(Tests, TestModule().tests())
