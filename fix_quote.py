from pathlib import Path
import re

p = Path(r'C:\Users\29090\Desktop\guaci\src\pages\index\index.ux')
s = p.read_text(encoding='utf-8')

# Add missing closing quote before }, on lines that have zhi: '... (no closing quote)
new = re.sub(r"(zhi:\s*'[^'\n]+)(},)\n", r"\1'\2\n", s)

p.write_text(new, encoding='utf-8')
print('quotes fixed')
