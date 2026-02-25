Original source of this document can be fount [here](https://github.com/Benjamin-Italiaander/kitty_terminal_working_config_example)

# 🐱 Kitty Terminal Configuration

A clean and practical `kitty.conf` example for **Kitty Terminal** on Linux, designed to work smoothly with **Oh My Zsh**.

This repository reflects my personal workflow and includes visual and usability tweaks.
Use it as a solid starting point and adapt it to your own preferences.

---

## 🚀 Installation

### 1️⃣ Install Kitty (Recommended Method)

It is recommended to install Kitty using the official installer provided by the author:

```bash
curl -L https://sw.kovidgoyal.net/kitty/installer.sh | sh /dev/stdin
```

This method ensures you get the latest official binary directly from the source.

For more details, see the official documentation:
[https://sw.kovidgoyal.net/kitty/binary/](https://sw.kovidgoyal.net/kitty/binary/)

---

### 2️⃣ Clone This Configuration

Clone this repository directly into your Kitty configuration directory:

```bash
git clone https://github.com/Benjamin-Italiaander/kitty_terminal_working_config_example.git ~/.config/kitty
```

If the directory already exists, back it up first:

```bash
mv ~/.config/kitty ~/.config/kitty.backup
git clone https://github.com/Benjamin-Italiaander/kitty_terminal_working_config_example.git ~/.config/kitty
```

Restart Kitty after cloning to apply the configuration.

---

## ✨ Features

* Optimized for Linux
* Designed for Oh My Zsh
* Custom `tab_bar` styling
* Modified `kitty_mod` keybinding

---

## ⌨️ Modifier Key Change

The default modifier key has been changed:

```
Default:  Ctrl+Shift
Current:  Ctrl+Super
```

If you prefer the default behavior, edit `kitty.conf` and revert:

```conf
# Disable custom modifier
# kitty_mod ctrl+super

# Enable default modifier
kitty_mod ctrl+shift
```

## 🔗 Recommended Shell Alias

For improved file navigation, I recommend enabling hyperlink support in `ls`.

Add the following alias to your shell configuration file:

### For Zsh

Add to `~/.zshrc`:

```bash
alias ll='ls --hyperlink=auto'
```

### For Bash

Add to `~/.bashrc`:

```bash
alias ll='ls --hyperlink=auto'
```

After adding the alias, reload your shell:

```bash
source ~/.zshrc
# or
source ~/.bashrc
```

This enables clickable file paths in supported terminals (including Kitty), making navigation more efficient when working with directories and logs.

