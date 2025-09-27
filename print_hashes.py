import hashlib
from pathlib import Path
p = Path("sample_test")
for f in sorted(p.iterdir()):
    if f.is_file():
        h = hashlib.sha256()
        with open(f, "rb") as fh:
            for chunk in iter(lambda: fh.read(8192), b""):
                h.update(chunk)
        print(f.name, h.hexdigest())
