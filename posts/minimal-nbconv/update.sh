#!/bin/bash

pandoc index.md -s -c "https://benrosenberg.info/style.css" --highlight-style zenburn --katex -o index.html

python3 replace_body.py > tmp.html

mv tmp.html index.html

echo "<br><br>" >> index.html