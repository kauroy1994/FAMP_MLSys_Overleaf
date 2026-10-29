"""Check the content endpoint in the compiled main paper; do not train models."""
from pathlib import Path
import re

aux = Path('main.aux').read_text(encoding='utf-8')
match = re.search(r'\\newlabel\{mainlastpage\}\{\{[^}]*\}\{(\d+)\}', aux)
if not match:
    raise SystemExit('Missing mainlastpage label; inspect the build.')
page = int(match.group(1))
print(f'Main content ends on page {page} (limit: 10). Inspect PDF floats/layout too.')
if page > 10:
    raise SystemExit('Main content exceeds the ten-page limit.')
