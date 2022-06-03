#!/bin/bash 

python3 replace_body.py > tmp.html

mv tmp.html index.html

echo "<br><br>" >> index.html