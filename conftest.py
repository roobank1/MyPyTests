from __future__ import annotations

from pathlib import Path
import os


def _safe_write_line(config, message: str) -> None:
    terminal_reporter = config.pluginmanager.get_plugin("terminalreporter")
    if terminal_reporter is not None:
        terminal_reporter.write_line(message)


def pytest_sessionfinish(session, exitstatus):
    config = session.config
    md_path = getattr(config.option, "md_report_output", None)

    if not md_path:
        return

    report_path = Path(md_path).resolve()

    _safe_write_line(config, f"Text report: {report_path}")
    _safe_write_line(config, f"View locally (PowerShell): code \"{report_path}\"")
    _safe_write_line(config, "View on GitHub: push test-results/report.txt and open it in the repo")
