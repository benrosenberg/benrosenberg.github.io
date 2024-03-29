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