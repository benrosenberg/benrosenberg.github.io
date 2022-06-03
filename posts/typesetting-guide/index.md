---
title: "The Right Way to Typeset: Getting started with Pandoc Markdown"
author: "[Ben Rosenberg](https://benrosenberg.info)"
date: 3/2/2022
---

## Introduction

This guide is meant for people who have little to no experience with non-WYSIWYG (What You See Is What You Get) editing. I hope that it sheds some light on how easy it can be to use non-WYSIWYG formats and that it helps people create a setup that works for them insofar as efficient typesetting is concerned.

Rather than Microsoft Word or Pages or Google Docs or what have you, this tutorial will teach you how to use Markdown, which is a versatile form of plaintext that can be compiled into other formats (like PDFs or HTML) or used as is (as in a default GitHub README.md file). I'm not going to try to justify the use of plaintext over something like MS Word or its ilk, as there are many other opinion pieces that do as good a job as I could or better. My hope is that after reading through this guide and following along, you'll come to that realization yourself. 

We'll begin with some basics of Markdown, and then go into setting up a nice editing environment to make your life easier. After that we'll look at some more complex things that you may want to look into after you're comfortable with everything else.

# Prerequisites

In order for everything to work as intended on your machine, you'll need to install some packages. The first thing is [`pandoc`](https://pandoc.org/installing.html). 

If you don't plan on compiling to PDF, and only want to compile to HTML, then you don't need to install $\LaTeX$. But if you do want to compile to PDF (and by extension, use $\LaTeX$ in compilation) you should install [TeX Live](https://tug.org/texlive/acquire-netinstall.html), which is a bundle of $\LaTeX$ packages that work for 99% of use cases. If you aren't running Windows please see [this page](https://tug.org/texlive/quickinstall.html) instead.

# Markdown basics

All flavors of Markdown have the same basic syntax (for the most part). The specific type of Markdown we'll be looking at in this tutorial is Pandoc Markdown, described [here](https://pandoc.org/MANUAL.html#pandocs-markdown) in more depth. Here is the most relevant subset of the syntax for Pandoc Markdown:

 - If you want to make **bold text**, use double asterisks or double underscores like so: `**bold text**`, `__bold text__`
 - If you want to make *italicized text*, use single asterisks or single underscores like so: `*italicized text*`, `_italicized text_`
 - If you want to make text that is both ***bold and italicized***, use triple asterisks (*not* underscores) like so: `***bold and italicized***`
 - If you want to make text that is `monospace`, use backticks like so: `` `monospace` ``
   - If you want to make a full code block then you'll want to use triple backticks in an unindented portion of your document (i.e., not in a list). You can also specify a certain language to use syntax highlighting for; in the example below, Python is chosen.

````
```python
from functools import cache

@cache
def fib(n):
    if n <= 1: return 1
    return fib(n-1) + fib(n-2)
```
````

This produces the following:

```python
from functools import cache

@cache
def fib(n):
    if n <= 1: return 1
    return fib(n-1) + fib(n-2)
```

 - To use various headers, use hashtags (`#`). One hashtag will give you the largest header, two will give you the second largest, etc.:

```md
# Section

## Subsection

### Subsubsection

#### Subsubsubsection

##### Subsubsubsection

###### Subsubsubsubsection

...
```

 - To create a list, either use hyphens for an unordered list or numbers for a numbered list:

```md
 - This is an element of an unordered list
 - So is this
    - Indent to make sublists
    - This is also an element of the same sublist
 - Back to the original list

1. This is the first element of an ordered list
2. This is the second
```

 - To create [hyperlinks](https://en.wikipedia.org/wiki/Hyperlink), use square brackets and parentheses like so: `[link to Google](https://www.google.com)`
   - To insert an image, you can use similar syntax. Just include an exclamation point like so: `![image caption](https://image-location.tld)`
 - To add document metadata, use YAML at the top of your document:

```yaml
---
title: My Document
author: Ben Rosenberg
date: "3/2/2022"
---
```

Alternatively, if compiling to PDF, you can specify the date to be today's day using:

```yaml
date: \today
```

The `\today` command is a $\LaTeX$ command that returns the current date. More information about how $\LaTeX$ and Pandoc Markdown interact will be covered in the last section.

 - Speaking of $\LaTeX$, the last important thing to be familiar with is how to typeset math. Pandoc recognizes dollar signs as delimiters for mathematical expressions (so make sure you escape them with backslashes if you don't want to start typing in $\LaTeX$ math!). I'm not going to go over $\LaTeX$ in this guide, but you can read up on how to typeset mathematical expressions with $\LaTeX$ syntax here: [PDF](http://tug.ctan.org/info/short-math-guide/short-math-guide.pdf) 

# Setting up your environment

Now that you know all the relevant syntax, you're ready to start writing Markdown on your own. But in order to do so, you'll need a decent editor. For programmers reading this, your general code editor should be fine -- after all, Markdown is basically just another programming language (although it may not be Turing complete). But I do have two recommendations either way:

## Choosing your editor

My first recommendation is [Visual Studio Code](https://code.visualstudio.com/) (VSCode). VSCode is a reliable code editor (as the name would imply) and is great for all sorts of things, but is also really good for typesetting in Markdown. The real benefit of VSCode is the ability to use extensions to get additional features and improve your user experience. There are many extensions which make editing Markdown painless (and maybe even fun!). I offer my recommendations for some of said extensions in the next section.

The second recommendation I have is [Vim](https://www.vim.org/). Vim is a command-line editor with a notoriously [high learning curve](editor_learning_curves.png) that can be very powerful once you learn to use it. There's a handy utility that gets installed with it that helps you learn how to use the editor: type `vimtutor` in your terminal to open it. 

In my opinion it's good to learn Vim to have the ability to edit in it, as it's probably the fastest CLI editor to use (maybe Emacs is close) and its progenitor `vi` comes installed by default on basically every UNIX-like OS. If you're `ssh`-ing into a headless machine, you probably won't be able to edit using VSCode, so it's good to know your way around Vim. 

If you're not a programmer and don't plan on using the terminal at all, Vim is likely not for you. I'd stick with VSCode. Also, importantly, I do *not* recommend using Vim if you are running Windows. UNIX-like environments are where Vim shines, not within the cursed GUI Vim that is provided for Windows users.

## Getting comfortable

To make yourself comfortable in the editor of your choice, it's always a good idea to choose a color scheme and some add-ons. How this works will vary depending on what editor you chose.

### VSCode Extensions 

In VSCode, there's an extension panel that you can get to by hitting `Ctrl+Shift+X` on your keyboard (unless you've bound that to something else, in which case you probably already know what to hit instead). In the search bar at the top, try looking up "themes" and choosing one that you like. If you're going to spend hours staring at the same application, at the very least it should look good, right? (I personally use the [Gruvbox Material](https://marketplace.visualstudio.com/items?itemName=sainnhe.gruvbox-material) extension, which I find to be easy on the eyes.)

Next, there are some extensions that I specifically recommend for Markdown editing:

 - [vscode-pandoc](https://marketplace.visualstudio.com/items?itemName=DougFinke.vscode-pandoc): **this is the most important one!** After installing this extension, when working on a file, you can compile directly to PDF (or HTML) with a couple keystrokes. Save your file with `Ctrl+S`, and then hit `Ctrl+K` and then `P`. This will bring up a list of options to compile to, from which you can choose either PDF, DOCX (not recommended), or HTML. 
 - [File Utils](https://marketplace.visualstudio.com/items?itemName=sleistner.vscode-fileutils): makes certain things that should be easy but are difficult by default in VSCode, easy again. If you want to rename a file while working on it, this extension will let you do that without having to "Save As".
 - [Markdown All In One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one): this is also really useful. Hitting `Ctrl+K+V` from within a Markdown file  you're editing once you've installed this extension will pop up a preview of your file to the side. Very useful for making sure it looks good before compiling! (Note that some of the $\LaTeX$ may not render as this is an HTML preview and not a PDF preview.)
 - [Paste Image](https://marketplace.visualstudio.com/items?itemName=mushan.vscode-paste-image): this extension will allow you to paste images from your clipboard (e.g., after screenshotting with `Win+Shift+S`) into your Markdown file (with the correct syntax) using `Ctrl+Alt+V`. The extension saves the image to the current working directory so it's accessible from the file, but you can also change that setting in the Settings menu (`Ctrl+,`).
  
## Vim plugins

Much like the `vscode-pandoc` extension above, you need a way to actually compile your Markdown when working with Vim as well. There are ways to do it from within Vim itself, but I personally just made two different Python scripts that I call depending on whether I want to compile to HTML or PDF, and added aliases for both of them within my `.zshrc` (it would be `.bashrc` for people using Bash instead of Zsh). If you want to see the general syntax for calling `pandoc` from the command line, just run `man pandoc` or read the manual [here](https://pandoc.org/MANUAL.html).

Besides that, I'm not really a whiz at Vim, but I do use the following general setup:

 - [Neovim](https://neovim.io/)
 - `syntax enable` in the editor config to enable syntax highlighting (if you use Neovim this is enabled by default)
 - `set number` in the editor config to enable line numbering (if you use Neovim this is also enabled by default)
  
I also recommend that, similarly to VSCode, you make the colors of your terminal look nice. You can generally do this in your terminal settings. If you use [`st`](https://st.suckless.org/) like me, it's a little more complicated as you need to edit a config makefile manually and then recompile.

# Where to go from here

Now you should have a decent setup. All that's left is to go over some more intricate details of Pandoc Markdown.

## HTML: Custom CSS

If you're planning on compiling mainly to HTML, you'll likely want to add some custom CSS to go with your files. You can choose a custom CSS file to use in VSCode when compiling by going to the Settings menu (`Ctrl+,`) and changing the setting under Extensions $\rightarrow$ Pandoc Option Configuration $\rightarrow$ Pandoc: HTML Opt String. I personally have the following:

```m
-s -c C:\path\to\my\css\file\my_css.css -t html5 --toc --katex
```

You can do the same kind of thing on the command line (i.e., if using Vim) by prepending `pandoc <my_file_name>` to the above. 

## PDF: Using more $\LaTeX$ in your Markdown; using specific $\LaTeX$ packages

Once you really get the hang of things, you may want to get more functionality out of your files and may want to use some more $\LaTeX$ packages. The first thing to note is that Pandoc Markdown gets turned into $\LaTeX$ on the backend when you compile to PDF! This means that you can insert all sorts of $\LaTeX$ stuff in the file and it'll work as intended. For example:

```latex
$$\begin{aligned}
    \sum_{i=1}^n \frac{1}{2} &= \frac{1}{2} + \sum_{i=2}^n \frac{1}{2} \\
    &= \frac{1}{2} + \frac{1}{2} + \sum_{i=3}^n \frac{1}{2} \\
    &= \underbrace{\frac{1}{2} + \cdots + \frac{1}{2}}_{\text{$n$ times}} \\
    &= \frac{n}{2}
\end{aligned}$$
```

...will turn into the following when inserted directly into Pandoc Markdown:

$$\begin{aligned}
    \sum_{i=1}^n \frac{1}{2} &= \frac{1}{2} + \sum_{i=2}^n \frac{1}{2} \\
    &= \frac{1}{2} + \frac{1}{2} + \sum_{i=3}^n \frac{1}{2} \\
    &= \frac{1}{2} + \frac{1}{2} + \frac{1}{2} + \sum_{i=4}^n \frac{1}{2} \\
    &= \underbrace{\frac{1}{2} + \cdots + \frac{1}{2}}_{\text{$n$ times}} \\
    &= \frac{n}{2}
\end{aligned}$$

Note that while all environments that would usually work in $\LaTeX$ are functional when you compile to PDF, the same cannot be said for $\KaTeX$. For instance, while the `aligned` environment works for $\KaTeX$, the `align*` environment does not.

If you want to use packages in your document like you would in normal $\LaTeX$, the `\usepackage{...}` syntax is the same. The only difference is that you declare all the stuff you want to use in the YAML header like so:

```yaml
---
header-includes: |
    \usepackage{A}
    \usepackage{B}
    ...
    \usepackage{C}
---
```

This way, you lose basically no functionality when going from $\LaTeX$ to Markdown. Markdown is just easier syntax with all the same features of $\LaTeX$!

---

And that's the end. I hope you enjoyed reading this guide (and maybe following along as well). I wish you the best of luck in your typesetting endeavors!