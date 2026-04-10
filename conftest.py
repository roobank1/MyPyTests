from __future__ import annotations

import pytest

from utils.steps import build_steps_html


# =========================
# 📊 Attach to HTML report
# =========================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":
        try:
            import pytest_html
            extra = list(getattr(rep, "extra", []))
            steps = getattr(item, "step_results", [])

            if steps:
                extra.append(
                    pytest_html.extras.html(build_steps_html(steps))
                )

            rep.extra = extra

        except ImportError:
            pass