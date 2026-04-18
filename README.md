
---


title: "Kitty Terminal"
description: "A clean and practical `kitty.conf` example for **Kitty Terminal** on Linux, designed to work seamlessly with **Oh My Zsh**."
author: "benjamin-italiaander"
date: 2023-02-27T14:12:45+01:00

---

Original source of this document you can find [here](https://github.com/Benjamin-Italiaander/kitty_terminal_working_config_example)



# 🐱 Kitty Terminal Configuration

A clean and practical `kitty.conf` example for **Kitty Terminal** on Linux, designed to work seamlessly with **Oh My Zsh**.

This repository reflects my personal workflow and includes visual and usability enhancements.
Use it as a solid starting point and adapt it to your own preferences.

I have a small [cheatsheet](./cheatsheet.md) that might be handy.

---

## 🚀 Installation

### 1️⃣ Install Kitty (Recommended Method)

Install the font i use in my theme with
```bash
sudo apt install fonts-firacode
```


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

----


## Other Helpful Aliases

### SSH alias for Kitty

When using **SSH from the Kitty terminal**, tools like `vim` may not always behave correctly out of the box.  
A simple solution is to use Kitty’s built-in SSH helper.

Kitty automatically sets the environment variable:

```bash
echo $KITTY_WINDOW_ID
````

* If you are running inside **Kitty**, this variable contains a number.
* If you are **not running Kitty**, the variable is empty.

This makes it easy to create **aliases that only apply when the terminal is Kitty**, without affecting your normal terminal environment.

> ⚠️ Tip: Define your **regular aliases first**, and then add the Kitty-specific ones afterwards.
> This way you extend your configuration only for Kitty instead of changing the behavior of every terminal.

Example:

```bash
if [ -n "$KITTY_WINDOW_ID" ]; then
    alias ssh="kitty +kitten ssh"
    alias ls="ls --hyperlink=auto --color=auto"
fi
```

This ensures that:

* `ssh` automatically uses Kitty’s optimized SSH integration.
* `ls` enables clickable hyperlinks and color support when running inside Kitty.

---

## Additional Useful Kitty Aliases

Kitty provides several small utilities called **kittens** that can enhance the terminal experience.

You can expose them through convenient aliases.

```bash
if [ -n "$KITTY_WINDOW_ID" ]; then
    alias ssh="kitty +kitten ssh"
    alias ls="ls --hyperlink=auto --color=auto"

    # Display images directly in the terminal
    alias icat="kitty +kitten icat"

    # Open files in the system default application
    alias kopen="kitty +kitten open"

    # Show the current terminal colors
    alias kcolors="kitty +kitten themes"

    # Quickly view text files with syntax highlighting
    alias kless="kitty +kitten diff"

    # Copy stdin directly to the system clipboard
    alias clip="kitty +kitten clipboard"

    alias vim="vim -c 'set termguicolors'"
fi
```

### Example Usage

Show an image inside the terminal:

```bash
icat image.png
```

Copy command output to your clipboard:

```bash
cat file.txt | clip
```

Open a file with the system default application:

```bash
kopen document.pdf
```


---

# 🐱 Kitty Terminal Cheatsheet
---

## 🪟 Window & Tab Management

| Shortcut | Description |
|--------|-------------|
| `mod + Enter` | Open a new window |
| `mod + T` | Open a new tab |
| `mod + ← / →` | Switch between tabs |
| `mod + [ / ]` | Switch between windows |
| `mod + F11` | Toggle fullscreen |

---

## 🔎 Navigation & Command Output

| Shortcut | Description |
|--------|-------------|
| `mod + G` | Open last command output |
| `mod + Mouse Click` | Open output from a command |

---

## 🔢 Identify & Select Panels / Windows

| Shortcut | Description |
|--------|-------------|
| `mod + F7` | Show panel/window numbers |
| `mod + panel-number` | Jump to the selected panel |


