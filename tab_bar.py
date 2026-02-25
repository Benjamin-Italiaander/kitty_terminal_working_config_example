# pyright: reportMissingImports=false
from __future__ import annotations

import datetime

from kitty.boss import get_boss
from kitty.fast_data_types import Screen, add_timer
from kitty.rgb import Color
from kitty.tab_bar import DrawData, ExtraData, TabBarData, as_rgb, draw_title
from kitty.utils import color_as_int, log_error

# Start a repeating timer once
_TIMER_STARTED = False


def _bg(c: Color) -> int:
    return as_rgb(color_as_int(c))


def _draw_cell(screen: Screen, text: str, fg: int | None = None, bg: Color | None = None, bold: bool = False) -> None:
    ofg, obg, obold = screen.cursor.fg, screen.cursor.bg, screen.cursor.bold
    if fg is not None:
        screen.cursor.fg = fg
    if bg is not None:
        screen.cursor.bg = _bg(bg)
    screen.cursor.bold = bold
    screen.draw(text)
    screen.cursor.fg, screen.cursor.bg, screen.cursor.bold = ofg, obg, obold


def _right_align(screen: Screen, width: int) -> None:
    x = screen.columns - width
    if x > screen.cursor.x:
        screen.draw(" " * (x - screen.cursor.x))


def _tick() -> None:
    # Ask kitty to redraw the tab bar
    boss = get_boss()
    tm = getattr(boss, "active_tab_manager", None)
    if tm is not None:
        tm.mark_tab_bar_dirty()

    # Re-schedule
    add_timer(_tick, 1.0, False)


def _ensure_timer() -> None:
    global _TIMER_STARTED
    if not _TIMER_STARTED:
        _TIMER_STARTED = True
        add_timer(_tick, 1.0, False)


log_error("custom tab_bar.py loaded (ticking clock enabled)")


def draw_tab(
    draw_data: DrawData,
    screen: Screen,
    tab: TabBarData,
    before: int,
    max_title_length: int,
    index: int,
    is_last: bool,
    extra_data: ExtraData,
) -> int:
    _ensure_timer()

    # Colors
    active_bg = Color(80, 140, 220)
    inactive_bg = Color(70, 70, 70)
    chrome_bg = Color(0, 0, 0)
    clock_bg = Color(180, 145, 200)

    # Best-effort "active tab" detection across versions
    is_active = bool(getattr(tab, "is_active", False) or getattr(tab, "is_focused", False))

    tab_bg = active_bg if is_active else inactive_bg

    # Fancy pill separators (needs Nerd Font). If missing, replace with "[" and "]".
    left_sep = ""
    right_sep = ""

    if draw_data.leading_spaces:
        screen.draw(" " * draw_data.leading_spaces)

    # Left pill + index
    _draw_cell(screen, left_sep, fg=_bg(tab_bg), bg=chrome_bg)
    _draw_cell(screen, f" {index} ", fg=0, bg=tab_bg, bold=is_active)

    # Title (kitty's own formatting)
    draw_title(draw_data, screen, tab, index)

    # Ellipsize like kitty does
    trailing_spaces = min(max_title_length - 1, draw_data.trailing_spaces)
    max_title_length -= trailing_spaces
    extra = screen.cursor.x - before - max_title_length
    if extra > 0:
        screen.cursor.x -= extra + 1
        screen.draw("…")
    if trailing_spaces:
        screen.draw(" " * trailing_spaces)

    # Close pill
    _draw_cell(screen, " ", fg=0, bg=tab_bg)
    _draw_cell(screen, right_sep, fg=_bg(tab_bg), bg=chrome_bg)

    end = screen.cursor.x  # keep +new-tab click target working
    
    # Separator between tabs
    screen.cursor.bold = screen.cursor.italic = False
    screen.cursor.fg = 2  # or whatever foreground you want
    
    if not is_last:
        screen.cursor.bg = 0   # 0 = default background (transparent)
        screen.draw(draw_data.sep)
        
        screen.cursor.bg = 0

    
    return end
