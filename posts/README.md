<style>
    code{white-space: pre-wrap;}
    span.smallcaps{font-variant: small-caps;}
    span.underline{text-decoration: underline;}
    div.column{display: inline-block; vertical-align: top; width: 50%;}
    div.hanging-indent{margin-left: 1.5em; text-indent: -1.5em;}
    ul.task-list{list-style: none;}
    pre > code.sourceCode { white-space: pre; position: relative; }
    pre > code.sourceCode > span { display: inline-block; line-height: 1.25; }
    pre > code.sourceCode > span:empty { height: 1.2em; }
    .sourceCode { overflow: visible; }
    code.sourceCode > span { color: inherit; text-decoration: inherit; }
    div.sourceCode { margin: 1em 0; }
    pre.sourceCode { margin: 0; }
    @media screen {
    div.sourceCode { overflow: auto; }
    }
    @media print {
    pre > code.sourceCode { white-space: pre-wrap; }
    pre > code.sourceCode > span { text-indent: -5em; padding-left: 5em; }
    }
    pre.numberSource code
      { counter-reset: source-line 0; }
    pre.numberSource code > span
      { position: relative; left: -4em; counter-increment: source-line; }
    pre.numberSource code > span > a:first-child::before
      { content: counter(source-line);
        position: relative; left: -1em; text-align: right; vertical-align: baseline;
        border: none; display: inline-block;
        -webkit-touch-callout: none; -webkit-user-select: none;
        -khtml-user-select: none; -moz-user-select: none;
        -ms-user-select: none; user-select: none;
        padding: 0 4px; width: 4em;
      }
    pre.numberSource { margin-left: 3em;  padding-left: 4px; }
    div.sourceCode
      { color: #cccccc; background-color: #303030; }
    @media screen {
    pre > code.sourceCode > span > a:first-child::before { text-decoration: underline; }
    }
    code span.al { color: #ffcfaf; } /* Alert */
    code span.an { color: #7f9f7f; font-weight: bold; } /* Annotation */
    code span.at { } /* Attribute */
    code span.bn { color: #dca3a3; } /* BaseN */
    code span.bu { } /* BuiltIn */
    code span.cf { color: #f0dfaf; } /* ControlFlow */
    code span.ch { color: #dca3a3; } /* Char */
    code span.cn { color: #dca3a3; font-weight: bold; } /* Constant */
    code span.co { color: #7f9f7f; } /* Comment */
    code span.cv { color: #7f9f7f; font-weight: bold; } /* CommentVar */
    code span.do { color: #7f9f7f; } /* Documentation */
    code span.dt { color: #dfdfbf; } /* DataType */
    code span.dv { color: #dcdccc; } /* DecVal */
    code span.er { color: #c3bf9f; } /* Error */
    code span.ex { } /* Extension */
    code span.fl { color: #c0bed1; } /* Float */
    code span.fu { color: #efef8f; } /* Function */
    code span.im { } /* Import */
    code span.in { color: #7f9f7f; font-weight: bold; } /* Information */
    code span.kw { color: #f0dfaf; } /* Keyword */
    code span.op { color: #f0efd0; } /* Operator */
    code span.ot { color: #efef8f; } /* Other */
    code span.pp { color: #ffcfaf; font-weight: bold; } /* Preprocessor */
    code span.sc { color: #dca3a3; } /* SpecialChar */
    code span.ss { color: #cc9393; } /* SpecialString */
    code span.st { color: #cc9393; } /* String */
    code span.va { } /* Variable */
    code span.vs { color: #cc9393; } /* VerbatimString */
    code span.wa { color: #7f9f7f; font-weight: bold; } /* Warning */
  </style>

## How to generate this page (spoiler alert: just run the `update.sh`)

This information may not be completely accurate. Look at `update.sh` for more details.

1. Run `tree` as follows:

```{.bash .neutral}
tree -H '.' --dirsfirst -L 1 --noreport --charset utf-8 | sed -e '/<hr>/,+7d' > index.html
```

This command turns the directory `.` (which is `posts/`) into a HTML file `index.html`, while removing the `tree` [author's acknowledgement](#tree-license) (which itself is rather distracting).

2. Run the following `perl` and `mv` commands:[^1]

```{.bash .neutral}
perl -0777 -pe 's/<style.*?<\/style>/<link rel="stylesheet" href="https:\/\/benrosenberg.info\/style.css">/gs' index.html > tmp.html

mv tmp.html index.html
```

These commands replace all styling with a custom stylesheet and store the result back in `index.html`.

1. Run the following line using a `python3` script, and the relevant `mv` command again:

```{.bash .neutral}
python3 replace_body.py > tmp.html

mv tmp.html index.html
```

The script is as follows:

```{.python .neutral}
import re

with open('index.html', 'r') as f:

    index = ''.join(f.readlines())

with open('sidebar.html', 'r') as s:

    sidebar = ''.join(s.readlines())

viewport_str = 'head>\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">\n\t<'

out =(index.replace('Directory Tree', 'Posts')
           .replace('<body>', sidebar)
           .replace('/"', '/index.html"'))

out = re.sub('head>[^<]*<', viewport_str, out, 1)

print(out)
```

It:

  - replaces the title "Directory Tree" with "Posts" 
  - adds the sidebar
  - make it so that all links to directories go to their `index.html` files
  - add the 'viewport' tag back into the header so that the page looks good on phones

1. Run the following `pandoc` command:

```{.bash .neutral}
pandoc README.md -o README.html
```

This command turns the README file you are reading into an HTML fragment.

1. Run the following `echo`, `cat`, `rm`, and `mv` commands:

```{.bash .neutral}
echo "<hr>" > hr.html

cat index.html hr.html README.html > tmp.html

rm hr.html

mv tmp.html index.html
```

These commands:

 - create a new HTML file containing only `<hr>`, the horizontal rule
 - concatenate the three HTML files that have been generated and store them back in `index.html`
 - remove the now-useless `hr.html` file[^2]

5. Run the following `rm` command:

```{.bash .neutral}
rm README.html
```

This command removes the unneeded `README.html` file.

6. Run the following `echo` command:

```{.bash .neutral}
echo "<br><br>" >> index.html
```

This command adds some extra space at the end of the page.

All together, these commands form a bash script which can be run instead for convenience:

```{.bash .good}
#!/bin/bash 

tree -H '.' --dirsfirst -L 1 --noreport --charset utf-8 | sed -e '/<hr>/,+7d' > index.html

perl -0777 -pe 's/<style.*?<\/style>/<link rel="stylesheet" href="https:\/\/benrosenberg.info\/style.css">/gs' index.html > tmp.html

mv tmp.html index.html

python3 replace_body.py > tmp.html

mv tmp.html index.html

pandoc README.md -o README.html

echo "<hr>" > hr.html

cat index.html hr.html README.html > tmp.html

rm hr.html

mv tmp.html index.html

echo "<br><br>" >> index.html

rm README.html
```

Run this script (also present in this directory, as you can see above) with the following command:

```{.bash .good}
./update.sh
```

[^1]: For some reason, trying to pipe `stdout` into one of the files being used within the `perl` command causes the file to become empty. Not completely sure why.
[^2]: It would be nice if `cat` syntax allowed for `cat index.html "<hr>" README.html > tmp.html`.

### `tree` license

```
tree v1.8.0 © 1996 - 2018 by Steve Baker and Thomas Moore
HTML output hacked and copyleft © 1998 by Francesc Rocher
JSON output hacked and copyleft © 2014 by Florian Sesser 
Charsets / OS/2 support © 2001 by Kyosuke Tokoro
```
