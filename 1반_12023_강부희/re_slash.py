# re_slash.py

import re

p = re.compile("\section")
p = re.compile("\\section")
m = p.match("\section python hello thanks")

print(m)

