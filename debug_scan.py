from smart_file_organizer.file_handler import FileHandler
from pathlib import Path
fh = FileHandler(Path("sample_test"))
print("Scanning sample_test...")
for f in fh.scan_files():
    print("FOUND:", f, "ext:", f.suffix.lower())
