with open('index.html', 'r') as f:

    index = ''.join(f.readlines())

with open('sidebar.html', 'r') as s:

    sidebar = ''.join(s.readlines())

user_katex_js = '/usr/lib/nodejs/katex/dist/katex.min.js'
online_katex_js = 'https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.11.1/katex.min.js'

user_katex_css = '/usr/lib/nodejs/katex/dist/katex.min.css'
online_katex_css = 'https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.11.1/katex.min.css'

print(index.replace('<body>', sidebar)
           .replace(user_katex_js, online_katex_js)
           .replace(user_katex_css, online_katex_css))