import markdown
import markdown_katex
import markdown_captions

with open('writeup.md', 'r') as f:
    content = f.read()

html = markdown.markdown(content, extensions=['markdown_katex', 'markdown_captions'])

with open('writeup.html', 'w') as f:
    f.write(html)