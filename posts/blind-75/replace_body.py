with open('index.html', 'r') as f:

    index = ''.join(f.readlines())

with open('sidebar.html', 'r') as s:

    sidebar = ''.join(s.readlines())

print(index.replace('<body>', sidebar))