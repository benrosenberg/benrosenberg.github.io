import json
import markdown
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
import re
import sys

help_string = ''' 
Format: python nbconv.py <in_filename> <out_filename> [-s]

in_filename:
    The name of the IPYNB file to pass to the converter. 
out_filename:
    The name of the HTML file to which the output should be written.
-s, --standalone: 
    Whether or not to include some CSS and a HTML header, so that math can be rendered properly.
    Also includes some CSS which makes the output look nicer overall.
    Useful for checking whether the output looks decent before running with standalone=False
    and then embedding in a site.
'''

args = sys.argv[1:]
if len(args) < 2:
    print('Too few arguments.')
    print(help_string)
    sys.exit(1)
if len(args) > 3:
    print('Too many arguments.')
    print(help_string)
    sys.exit(1)
if len(args) == 2:
    standalone = False
    in_filename, out_filename = args
if len(args) == 3:
    if args[2] in ['-s', '--standalone']:
        standalone = True
    else:
        print('Unrecognized flag:', args[2])
        print(help_string)
        sys.exit(1)
    in_filename, out_filename = args[:2]

''' BEGIN SCRIPT '''

standalone_html_top = '''
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="" xml:lang="">
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
  <title>Generated with Minimal IPYNB Converter</title>
  <style>
    .wrapped-ipynb {
        margin: 4%;
        font-family: Arial, Helvetica, sans-serif; font-size: 20px;
    }
    .wrapped-code {
        margin: 1%;
    }
    .wrapped-output {
        margin: 1%;
    }
    /* Pygments default syntax highlighting */
    .highlight .hll  {  background-color: #ffffcc; }
    .highlight { background: #f8f8f8; }
    .highlight .c  {  color: #408080; font-style: italic; } /* Comment */
    .highlight .err  {  border: 1px solid #ff0000; } /* Error */
    .highlight .k  {  color: #008000; font-weight: bold; } /* Keyword */
    .highlight .o  {  color: #666666; } /* Operator */
    .highlight .ch  {  color: #408080; font-style: italic; } /* Comment.Hashbang */
    .highlight .cm  {  color: #408080; font-style: italic; } /* Comment.Multiline */
    .highlight .cp  {  color: #bc7a00; } /* Comment.Preproc */
    .highlight .cpf  {  color: #408080; font-style: italic; } /* Comment.PreprocFile */
    .highlight .c1  {  color: #408080; font-style: italic; } /* Comment.Single */
    .highlight .cs  {  color: #408080; font-style: italic; } /* Comment.Special */
    .highlight .gd  {  color: #a00000; } /* Generic.Deleted */
    .highlight .ge  {  font-style: italic; } /* Generic.Emph */
    .highlight .gr  {  color: #ff0000; } /* Generic.Error */
    .highlight .gh  {  color: #000080; font-weight: bold; } /* Generic.Heading */
    .highlight .gi  {  color: #00a000; } /* Generic.Inserted */
    .highlight .go  {  color: #888888; } /* Generic.Output */
    .highlight .gp  {  color: #000080; font-weight: bold; } /* Generic.Prompt */
    .highlight .gs  {  font-weight: bold; } /* Generic.Strong */
    .highlight .gu  {  color: #800080; font-weight: bold; } /* Generic.Subheading */
    .highlight .gt  {  color: #0044dd; } /* Generic.Traceback */
    .highlight .kc  {  color: #008000; font-weight: bold; } /* Keyword.Constant */
    .highlight .kd  {  color: #008000; font-weight: bold; } /* Keyword.Declaration */
    .highlight .kn  {  color: #008000; font-weight: bold; } /* Keyword.Namespace */
    .highlight .kp  {  color: #008000; } /* Keyword.Pseudo */
    .highlight .kr  {  color: #008000; font-weight: bold; } /* Keyword.Reserved */
    .highlight .kt  {  color: #b00040; } /* Keyword.Type */
    .highlight .m  {  color: #666666; } /* Literal.Number */
    .highlight .s  {  color: #ba2121; } /* Literal.String */
    .highlight .na  {  color: #7d9029; } /* Name.Attribute */
    .highlight .nb  {  color: #008000; } /* Name.Builtin */
    .highlight .nc  {  color: #0000ff; font-weight: bold; } /* Name.Class */
    .highlight .no  {  color: #880000; } /* Name.Constant */
    .highlight .nd  {  color: #aa22ff; } /* Name.Decorator */
    .highlight .ni  {  color: #999999; font-weight: bold; } /* Name.Entity */
    .highlight .ne  {  color: #d2413a; font-weight: bold; } /* Name.Exception */
    .highlight .nf  {  color: #0000ff; } /* Name.Function */
    .highlight .nl  {  color: #a0a000; } /* Name.Label */
    .highlight .nn  {  color: #0000ff; font-weight: bold; } /* Name.Namespace */
    .highlight .nt  {  color: #008000; font-weight: bold; } /* Name.Tag */
    .highlight .nv  {  color: #19177c; } /* Name.Variable */
    .highlight .ow  {  color: #aa22ff; font-weight: bold; } /* Operator.Word */
    .highlight .w  {  color: #bbbbbb; } /* Text.Whitespace */
    .highlight .mb  {  color: #666666; } /* Literal.Number.Bin */
    .highlight .mf  {  color: #666666; } /* Literal.Number.Float */
    .highlight .mh  {  color: #666666; } /* Literal.Number.Hex */
    .highlight .mi  {  color: #666666; } /* Literal.Number.Integer */
    .highlight .mo  {  color: #666666; } /* Literal.Number.Oct */
    .highlight .sa  {  color: #ba2121; } /* Literal.String.Affix */
    .highlight .sb  {  color: #ba2121; } /* Literal.String.Backtick */
    .highlight .sc  {  color: #ba2121; } /* Literal.String.Char */
    .highlight .dl  {  color: #ba2121; } /* Literal.String.Delimiter */
    .highlight .sd  {  color: #ba2121; font-style: italic; } /* Literal.String.Doc */
    .highlight .s2  {  color: #ba2121; } /* Literal.String.Double */
    .highlight .se  {  color: #bb6622; font-weight: bold; } /* Literal.String.Escape */
    .highlight .sh  {  color: #ba2121; } /* Literal.String.Heredoc */
    .highlight .si  {  color: #bb6688; font-weight: bold; } /* Literal.String.Interpol */
    .highlight .sx  {  color: #008000; } /* Literal.String.Other */
    .highlight .sr  {  color: #bb6688; } /* Literal.String.Regex */
    .highlight .s1  {  color: #ba2121; } /* Literal.String.Single */
    .highlight .ss  {  color: #19177c; } /* Literal.String.Symbol */
    .highlight .bp  {  color: #008000; } /* Name.Builtin.Pseudo */
    .highlight .fm  {  color: #0000ff; } /* Name.Function.Magic */
    .highlight .vc  {  color: #19177c; } /* Name.Variable.Class */
    .highlight .vg  {  color: #19177c; } /* Name.Variable.Global */
    .highlight .vi  {  color: #19177c; } /* Name.Variable.Instance */
    .highlight .vm  {  color: #19177c; } /* Name.Variable.Magic */
    .highlight .il  {  color: #666666; } /* Literal.Number.Integer.Long */
  </style>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.11.1/katex.min.js"></script>
  <script>document.addEventListener("DOMContentLoaded", function () {
   var mathElements = document.getElementsByClassName("math");
   var macros = [];
   for (var i = 0; i < mathElements.length; i++) {
    var texText = mathElements[i].firstChild;
    if (mathElements[i].tagName == "SPAN") {
     katex.render(texText.data, mathElements[i], {
      displayMode: mathElements[i].classList.contains('display'),
      throwOnError: false,
      macros: macros,
      fleqn: false
     });
  }}});
  </script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.11.1/katex.min.css" />
</head>
'''

with open(in_filename, 'r') as f:
    json_rep = json.loads(' '.join(l.strip() for l in f.readlines()))

def wrap_math(string):
    regex = r'(\${1,2})(?:(?!\1)[\s\S])*\1'
    matches = []
    last_end_index = 0
    for m in re.finditer(regex, string):
        delim = m.group(1)
        value = m.group(0)
        start = m.start()
        end   = m.end()
        before = string[last_end_index:start]
        last_end_index = end
        matches.append((before, delim, value))

    subbed = ''
    for (before, delim, value) in matches:
        subbed += before
        if delim == '$':
            math_type = 'display'
        else:
            math_type = 'inline'
        tag_start = '<span class="math {}">'.format(math_type)
        tag_end = '</span>'
        subbed += tag_start + value.replace(delim, '') + tag_end

    if last_end_index == 0:
        last_end_index -= 1
    subbed += string[last_end_index+1:]
    return subbed

def wrap_code(code):
    wrapped = '<div class="wrapped-code">\n'
    wrapped += code
    wrapped += '\n</div>'
    return wrapped

def wrap_markdown(mkdn):
    wrapped = '<div class="wrapped-markdown">\n'
    wrapped += mkdn
    wrapped += '\n</div>'
    return wrapped

def wrap_output(code):
    wrapped = '<div class="wrapped-output"><pre>\n'
    wrapped += code
    wrapped += '\n</pre></div>'
    return wrapped

def wrap_image_output(imgsource):
    wrapped = '<img src="data:image/png;base64,'
    wrapped += imgsource
    wrapped += '">'
    return wrapped

out = ''

cells = json_rep['cells']
for cell in cells:
    cell_type, source, outputs = cell['cell_type'], cell['source'], None
    if 'outputs' in cell:
        if len(cell['outputs']) == 0:
            outputs = None
            text_outputs = None
            image_outputs = None
        else:
            text_outputs = None
            image_outputs = None
            outputs = cell['outputs']
            text_outputs = [output['text'] for output in outputs if 'text' in output]
            # base64 png images from (e.g.) matplotlib
            data_outputs = [output['data'] for output in outputs if output['output_type'] == 'display_data']
            img_data_outputs = [data_output for data_output in data_outputs if 'image/png' in data_output]
            if img_data_outputs:
                image_outputs = [img_data_output['image/png'] for img_data_output in img_data_outputs]
    joined_source = ''.join(source)
    if cell_type == 'markdown':
        out += wrap_markdown(markdown.markdown(wrap_math(joined_source)))
    else:
        out += wrap_code(highlight(joined_source, PythonLexer(), HtmlFormatter()))
    if 'outputs' in cell:
        if text_outputs:
            joined_text_outs = ''.join(text_outputs[0])
            out += wrap_output(joined_text_outs)
        if image_outputs:
            for image_output in image_outputs:
                out += wrap_output(wrap_image_output(image_output))

out = '<div class="wrapped-ipynb">' + out + '</div>'

if standalone:
    out = standalone_html_top + '\n' + out

with open(out_filename, 'w') as f:
    f.write(out)