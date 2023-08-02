from __future__ import annotations

import importlib

from typing import cast

import ansible.plugins.filter.core as filter_core  # type: ignore[import]
import ansible.plugins.filter.mathstuff as filter_mathstuff  # type: ignore[import]
import ansible.plugins.filter.urls as filter_urls  # type: ignore[import]
import ansible.plugins.filter.urlsplit as filter_urlsplit  # type: ignore[import]
import ansible.plugins.test.core as test_core  # type: ignore[import]
import ansible.plugins.test.files as test_files  # type: ignore[import]
import ansible.plugins.test.mathstuff as test_mathstuff  # type: ignore[import]
import ansible.plugins.test.uri as test_uri  # type: ignore[import]

from jinjanator_plugins import (
    Filters,
    Identity,
    Tests,
    plugin_filters_hook,
    plugin_identity_hook,
    plugin_tests_hook,
)


@plugin_identity_hook
def plugin_identities() -> Identity:
    return f"ansible (using ansible-core {importlib.metadata.version('ansible-core')})"


@plugin_filters_hook
def plugin_filters() -> Filters:
    return cast(
        Filters,
        {
            **filter_core.FilterModule().filters(),
            **filter_mathstuff.FilterModule().filters(),
            **filter_urls.FilterModule().filters(),
            **filter_urlsplit.FilterModule().filters(),
        },
    )


@plugin_tests_hook
def plugin_tests() -> Tests:
    return cast(
        Tests,
        {
            **test_core.TestModule().tests(),
            **test_files.TestModule().tests(),
            **test_mathstuff.TestModule().tests(),
            **test_uri.TestModule().tests(),
        },
    )
