from __future__ import annotations

from jinjanator_plugin_ansible import plugin


def test_plugin_identity() -> None:
    result = plugin.plugin_identities()
    assert result.startswith("ansible")
    assert "ansible-core" in result


def test_plugin_filters() -> None:
    result = plugin.plugin_filters()
    assert "to_uuid" in result
    assert "union" in result
    assert "urldecode" in result
    assert "urlsplit" in result


def test_plugin_tests() -> None:
    result = plugin.plugin_tests()
    assert "version_compare" in result
    assert "is_same_file" in result
    assert "contains" in result
    assert "uri" in result
