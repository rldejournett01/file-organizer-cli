from pathlib import Path
from .config import FILE_CATEGORIES

def get_category(file_path: Path) -> str:
    extension = file_path.suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category
        
    return "Other"