import re
from colorama import init, Fore, Style, Back

def colored_text(message: str, one_statement=(), print_statement=True, input_statement=False):
  init(autoreset=True)

  def identify_color(s: str):
    if s.find("light") != -1:
      s += "_EX"

    if s[0] == 'f':
      color = Fore.__dict__.get(s[1:].upper(), '')
    elif s[0] == 's':
      color = Style.__dict__.get(s[1:].upper(), '')
    else:
      color = Back.__dict__.get(s[1:].upper(), '')
    return color

  if one_statement:
    text = "".join(map(lambda x: identify_color(x.replace(" ", '')), one_statement)) + message
  else:
    pattern = r'<(.*?)>'
    color_pattern = re.compile(pattern)
    # Split the message using the color tags as delimiters
    parts = color_pattern.split(message)
    text = ""
    for part in parts:
      if part.startswith('/f'):
        color = Fore.RESET
      elif part.startswith('/b'):
        color = Back.RESET
      elif part.startswith('/s'):
        color = Style.NORMAL
      else:
        color = identify_color(part.replace("-", "")) if part else None
      text += part if not color else color
  
  if input_statement:
    return input(text)

  if not print_statement:
    return text
  print(text)
