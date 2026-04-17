# 🐱 Kitty Terminal Cheatsheet

Quick reference for commonly used shortcuts in Kitty.

---

## Window & Tab Management

| Shortcut      | Action                 |
| ------------- | ---------------------- |
| `mod + Enter` | Open new window        |
| `mod + T`     | Open new tab           |
| `mod + ← / →` | Switch between tabs    |
| `mod + [ / ]` | Switch between windows |
| `mod + F11`   | Toggle fullscreen      |
| `mod + W`     | Resize windows         |
| `mod + L`     | Re-arrange windows     |

---

## Navigation & Output

| Shortcut            | Action                   |
| ------------------- | ------------------------ |
| `mod + G`           | Open last command output |
| `mod + Mouse Click` | Open output from command |

---

## Panel / Window Selection

| Shortcut         | Action                    |
| ---------------- | ------------------------- |
| `mod + F7`       | Show panel/window numbers |
| `mod + <number>` | Jump to selected panel    |

---

## Kitty Shell & Broadcasting

| Shortcut    | Action           |
| ----------- | ---------------- |
| `mod + Esc` | Open Kitty shell |

Start broadcasting commands to all windows:

```bash
launch --allow-remote-control kitty +kitten broadcast
```

---

## Scrollback Navigation

| Shortcut         | Action                      |
| ---------------- | --------------------------- |
| `mod + ↑`        | Line up                     |
| `mod + ↓`        | Line down                   |
| `mod + PageUp`   | Page up                     |
| `mod + PageDown` | Page down                   |
| `mod + Home`     | Top                         |
| `mod + End`      | Bottom                      |
| `mod + Z`        | Previous shell prompt       |
| `mod + X`        | Next shell prompt           |
| `mod + H`        | Browse scrollback in `less` |
| `mod + G`        | Browse last command output  |
| `mod + /`        | Search scrollback           |

 These only work in the **main screen**, not inside full-screen apps like `vim`.

---

## Tabs

| Shortcut        | Action            |
| --------------- | ----------------- |
| `mod + T`       | New tab           |
| `mod + Q`       | Close tab         |
| `mod + →`       | Next tab          |
| `mod + ←`       | Previous tab      |
| `mod + L`       | Next layout       |
| `mod + .`       | Move tab forward  |
| `mod + ,`       | Move tab backward |
| `mod + Alt + T` | Set tab title     |

---

## Windows

| Shortcut      | Action                |
| ------------- | --------------------- |
| `mod + Enter` | New window            |
| `mod + N`     | New OS window         |
| `mod + W`     | Close window          |
| `mod + R`     | Resize window         |
| `mod + ]`     | Next window           |
| `mod + [`     | Previous window       |
| `mod + F`     | Move window forward   |
| `mod + B`     | Move window backward  |
| `mod + ``     | Move window to top    |
| `mod + F7`    | Visually focus window |
| `mod + F8`    | Visually swap window  |
| `mod + 1..0`  | Focus specific window |

---

## Advanced Window Mapping (kitty.conf)

```conf
map ctrl+left neighboring_window left
map shift+left move_window right
map ctrl+down neighboring_window down
map shift+down move_window up

# Previous window
map ctrl+p nth_window -1

# Detach window
map ctrl+f2 detach_window
map ctrl+f3 detach_window new-tab
map ctrl+f4 detach_window ask

# Detach tab
map ctrl+f2 detach_tab
map ctrl+f4 detach_tab ask

# Close all except current
map f9 close_other_windows_in_tab
```

---

## General Shortcuts

| Shortcut          | Action                    |
| ----------------- | ------------------------- |
| `mod + F1`        | Show help                 |
| `mod + C`         | Copy                      |
| `mod + V`         | Paste                     |
| `mod + S`         | Paste from selection      |
| `mod + O`         | Pass selection to program |
| `mod + =`         | Increase font size        |
| `mod + -`         | Decrease font size        |
| `mod + Backspace` | Reset font size           |
| `mod + F11`       | Toggle fullscreen         |
| `mod + F10`       | Toggle maximized          |
| `mod + U`         | Input Unicode character   |
| `mod + E`         | Open URL                  |
| `mod + Delete`    | Reset terminal            |
| `mod + F2`        | Edit config               |
| `mod + F5`        | Reload config             |
| `mod + F6`        | Debug config              |
| `mod + Esc`       | Open Kitty shell          |

---

## Background Opacity

| Shortcut      | Action           |
| ------------- | ---------------- |
| `mod + A > M` | Increase opacity |
| `mod + A > L` | Decrease opacity |
| `mod + A > 1` | Full opacity     |
| `mod + A > D` | Reset opacity    |
