from __future__ import annotations

from pathlib import Path
import os
import webbrowser


def _safe_write_line(config, message: str) -> None:
    terminal_reporter = config.pluginmanager.get_plugin("terminalreporter")
    if terminal_reporter is not None:
        terminal_reporter.write_line(message)


def pytest_sessionfinish(session, exitstatus):
    config = session.config
    html_path = getattr(config.option, "htmlpath", None)

    if not html_path:
        _safe_write_line(
            config,
            "HTML report is not enabled. Use: pytest --html=test-results/report.html --self-contained-html",
        )
        return

    report_path = Path(html_path).resolve()
    report_cmd = f'Start-Process "{report_path}"'

    _safe_write_line(config, f"HTML report path: {report_path}")
    _safe_write_line(config, f"Open report command (PowerShell): {report_cmd}")
    _safe_write_line(config, "Open report command (CMD): start \"\" \"%CD%\\test-results\\report.html\"")

    # Avoid auto-opening in CI to keep automated runs non-interactive.
    if os.environ.get("CI"):
        return

    if report_path.exists():
        try:
            webbrowser.open_new_tab(report_path.as_uri())
            _safe_write_line(config, "Opened HTML report in your default browser.")
        except Exception as exc:
            _safe_write_line(config, f"Could not auto-open report: {exc}")
