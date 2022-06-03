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
