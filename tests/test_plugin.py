from __future__ import annotations

from pathlib import Path

from jinjanator.cli import render_command


def test_filter(tmp_path: Path) -> None:
    template_file = tmp_path / "template.j2"
    template_file.write_text("{{ name | to_uuid }}")
    data_file = tmp_path / "data.env"
    data_file.write_text("name=Bart")
    assert (
        render_command(
            Path.cwd(),
            {},
            None,
            ["", str(template_file), str(data_file)],
        )
        == "7acd55fd-0779-54cc-a798-cdf367486926"
    )


def test_test(tmp_path: Path) -> None:
    template_file = tmp_path / "template.j2"
    template_file.write_text("{% if ver is version('22.0', '>=') %}pass{% endif %}")
    data_file = tmp_path / "data.env"
    data_file.write_text("ver=23.2.0")
    assert (
        render_command(
            Path.cwd(),
            {},
            None,
            ["", str(template_file), str(data_file)],
        )
        == "pass"
    )
