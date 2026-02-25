
# 🐱 Kitty Terminal Configuration

A clean and practical `kitty.conf` example for **Kitty Terminal** on Linux, used in combination with **Oh My Zsh**.

This configuration reflects my personal workflow and includes a few visual and usability tweaks.
Feel free to use it as a starting point and adapt it to your own preferences.

---

## ✨ Features

* Optimized for Linux
* Designed to work smoothly with Oh My Zsh
* Custom `tab_bar` styling
* Modified modifier key configuration

---

## ⌨️ Modifier Key Change

The default `kitty_mod` keybinding has been changed:

```
Default:  Ctrl+Shift
Current:  Ctrl+Super
```

As a result, `Ctrl+Shift` no longer acts as the Kitty modifier key.

If you prefer the default behavior, simply revert the change in `kitty.conf`:

```conf
# Disable custom modifier
# kitty_mod ctrl+super

# Enable default modifier
kitty_mod ctrl+shift
```


