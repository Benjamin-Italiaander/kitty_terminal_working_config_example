
---


title: "Kitty Terminal"
description: "A clean and practical `kitty.conf` example for **Kitty Terminal** on Linux, designed to work seamlessly with **Oh My Zsh**."
author: "benjamin-italiaander"
date: 2023

---

Original source of this document you can find [here](https://github.com/Benjamin-Italiaander/kitty_terminal_working_config_example)



# 🐱 Kitty Terminal Configuration

A clean and practical `kitty.conf` example for **Kitty Terminal** on Linux, designed to work seamlessly with **Oh My Zsh**.

This repository reflects my personal workflow and includes visual and usability enhancements.
Use it as a solid starting point and adapt it to your own preferences.

---

## 🚀 Installation

### 1️⃣ Install Kitty (Recommended Method)

Install Kitty using the official installer provided by the author:

```bash
curl -L https://sw.kovidgoyal.net/kitty/installer.sh | sh /dev/stdin
```

This ensures you are running the latest official binary directly from the source.

Official documentation:
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

## ⌨️ Modifier Key Change

Because I use the **MATE desktop environment**, I changed the default modifier key.

In this configuration:

```
Default:  Ctrl+Shift
Current:  Ctrl+Super
```

If you prefer the default behavior, edit `kitty.conf` and revert the change:

```conf
# Disable custom modifier
# kitty_mod ctrl+super

# Enable default modifier
kitty_mod ctrl+shift
```

---

## 🔗 Recommended Shell Alias

For improved file navigation, I recommend enabling hyperlink support in `ls`.

In many setups, an `ls` alias already exists. I recommend modifying it by adding `--hyperlink=auto` to the existing alias.

### For Zsh

Add or modify in `~/.zshrc`:

```bash
alias ls='ls --hyperlink=auto --color=auto'
```

### For Bash

Add or modify in `~/.bashrc`:

```bash
alias ls='ls --hyperlink=auto --color=auto'
```

Reload your shell after updating:

```bash
source ~/.zshrc
# or
source ~/.bashrc
```

This enables clickable file paths in supported terminals (including Kitty), making navigation more efficient when working with directories, logs, and build outputs.
