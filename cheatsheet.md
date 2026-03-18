# Kitty Terminal Cheatsheet

Quick reference for the shortcuts I use most while working in **Kitty terminal**.

---

# Window & Tab Management

| Shortcut | Action |
|--------|--------|
| `mod + Enter` | Open new window |
| `mod + T` | Open new tab |
| `mod + ← / →` | Switch between tabs |
| `mod + [ / ]` | Switch between windows |
| `mod + F11` | Toggle fullscreen |
| `mod + w` | Resize windows |
| `mod + l` | Re-agrange windows |


---

# Navigation & Output

| Shortcut | Action |
|--------|--------|
| `mod + G` | Open last command output |
| `mod + Mouse Click` | Open output from command |

---

# Panel / Window Selection

| Shortcut | Action |
|--------|--------|
| `mod + F7` | Show panel/window numbers |
| `mod + <panel-number>` | Jump to selected panel |

---

# Kitty Shell & Broadcasting

| Shortcut | Action |
|--------|--------|
| `mod + Esc` | Open Kitty shell |

Start broadcasting commands to all open windows:

```bash
launch --allow-remote-control kitty +kitten broadcast
```
