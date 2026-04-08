# utils/steps.py

from __future__ import annotations

import base64
from html import escape


POST_ACTION_SCREENSHOT_DELAY_MS = 400


def _settle_page_before_capture(page):
    for state in ("domcontentloaded", "networkidle"):
        try:
            page.wait_for_load_state(state, timeout=1_500)
        except Exception:
            pass

    try:
        page.wait_for_timeout(POST_ACTION_SCREENSHOT_DELAY_MS)
    except Exception:
        pass


async def _settle_page_before_capture_async(page):
    for state in ("domcontentloaded", "networkidle"):
        try:
            await page.wait_for_load_state(state, timeout=1_500)
        except Exception:
            pass

    try:
        await page.wait_for_timeout(POST_ACTION_SCREENSHOT_DELAY_MS)
    except Exception:
        pass


def _get_step_entries(request):
    if not hasattr(request.node, "step_results"):
        request.node.step_results = []
    return request.node.step_results


def _append_step_result(request, name: str, status: str, image_b64: str = "", error: str = ""):
    _get_step_entries(request).append(
        {
            "name": name,
            "status": status,
            "image_b64": image_b64,
            "error": error,
        }
    )


def _capture_step(page, request, name: str, status: str, error: str = ""):
    image_b64 = ""
    try:
        _settle_page_before_capture(page)
        image_bytes = page.screenshot(type="png")
        image_b64 = base64.b64encode(image_bytes).decode("ascii")
    except Exception as screenshot_error:
        if error:
            error = f"{error}\nScreenshot error: {screenshot_error}"
        else:
            error = f"Screenshot error: {screenshot_error}"

    _append_step_result(request, name, status, image_b64=image_b64, error=error)


async def _capture_step_async(page, request, name: str, status: str, error: str = ""):
    image_b64 = ""
    try:
        await _settle_page_before_capture_async(page)
        image_bytes = await page.screenshot(type="png")
        image_b64 = base64.b64encode(image_bytes).decode("ascii")
    except Exception as screenshot_error:
        if error:
            error = f"{error}\nScreenshot error: {screenshot_error}"
        else:
            error = f"Screenshot error: {screenshot_error}"

    _append_step_result(request, name, status, image_b64=image_b64, error=error)


def step(page, name: str, action, request):
    print(f"STEP: {name}")
    try:
        result = action()
    except Exception as exc:
        _capture_step(page, request, name, "failed", str(exc))
        raise

    _capture_step(page, request, name, "passed")
    return result


async def async_step(page, name: str, action, request):
    print(f"STEP: {name}")
    try:
        result = await action()
    except Exception as exc:
        await _capture_step_async(page, request, name, "failed", str(exc))
        raise

    await _capture_step_async(page, request, name, "passed")
    return result


def build_steps_html(steps):
    if not steps:
        return "<div>No step data recorded.</div>"

    rows = []
    for index, step_result in enumerate(steps, start=1):
        status = step_result["status"]
        badge_color = "#1f7a1f" if status == "passed" else "#b42318"
        badge_text = escape(status.upper())
        step_name = escape(step_result["name"])
        error_text = escape(step_result["error"]) if step_result["error"] else ""

        if step_result["image_b64"]:
            screenshot_html = (
                '<a href="data:image/png;base64,{0}" target="_blank">'
                '<img src="data:image/png;base64,{0}" '
                'style="max-width:260px; border:1px solid #d0d7de; border-radius:6px;" '
                'alt="{1} screenshot"></a>'
            ).format(step_result["image_b64"], step_name)
        else:
            screenshot_html = '<span style="color:#6b7280;">No screenshot</span>'

        rows.append(
            """
            <tr>
                <td style="padding:10px; border:1px solid #d0d7de; vertical-align:top;">{index}</td>
                <td style="padding:10px; border:1px solid #d0d7de; vertical-align:top;">{step_name}</td>
                <td style="padding:10px; border:1px solid #d0d7de; vertical-align:top;">
                    <span style="display:inline-block; padding:4px 10px; border-radius:999px; color:#fff; background:{badge_color}; font-weight:600;">
                        {badge_text}
                    </span>
                </td>
                <td style="padding:10px; border:1px solid #d0d7de; vertical-align:top;">{screenshot_html}</td>
                <td style="padding:10px; border:1px solid #d0d7de; vertical-align:top; white-space:pre-wrap;">{error_text}</td>
            </tr>
            """.format(
                index=index,
                step_name=step_name,
                badge_color=badge_color,
                badge_text=badge_text,
                screenshot_html=screenshot_html,
                error_text=error_text,
            )
        )

    return """
    <div style="margin-top:12px;">
        <h3 style="margin:0 0 12px;">Step Execution Report</h3>
        <table style="width:100%; border-collapse:collapse; font-size:14px;">
            <thead>
                <tr style="background:#f6f8fa; text-align:left;">
                    <th style="padding:10px; border:1px solid #d0d7de;">#</th>
                    <th style="padding:10px; border:1px solid #d0d7de;">Step</th>
                    <th style="padding:10px; border:1px solid #d0d7de;">Status</th>
                    <th style="padding:10px; border:1px solid #d0d7de;">Screenshot</th>
                    <th style="padding:10px; border:1px solid #d0d7de;">Error</th>
                </tr>
            </thead>
            <tbody>
                {rows}
            </tbody>
        </table>
    </div>
    """.format(rows="".join(rows))