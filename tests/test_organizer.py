from pathlib import Path
from src.file_organizer.organizer import get_category

def test_get_category_for_image():
    assert get_category(Path("photo.jpg")) == "Images"

def test_get_category_for_document():
    assert get_category(Path("document.pdf")) == "Documents"

def test_get_category_for_unknown_extension():
    assert get_category(Path("random.xyz")) == "Other"