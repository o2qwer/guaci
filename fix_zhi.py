import re
from pathlib import Path

p = Path(r'C:\Users\29090\Desktop\guaci\src\pages\index\index.ux')
s = p.read_text(encoding='utf-8')

def repl(m):
    return m.group(1) + m.group(2)

new = re.sub(r"(zhi:\s*')(?:(?:大|中|小)?[吉凶]，)([^']+)'", repl, s)

# Verify Chinese char counts after removal
for line in new.splitlines():
    if 'zhi:' in line and 'gua.zhi' not in line:
        part = line.split('zhi:')[1].split(',')[0].strip().strip("'")
        chars = sum(1 for c in part if '\u4e00' <= c <= '\u9fff')
        print(chars, part)

p.write_text(new, encoding='utf-8')
print('done')
