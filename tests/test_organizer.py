from pathlib import Path
from src.file_organizer.organizer import get_category, organize_folder

def test_get_category_for_image():
    assert get_category(Path("photo.jpg")) == "Images"

def test_get_category_for_document():
    assert get_category(Path("document.pdf")) == "Documents"

def test_get_category_for_unknown_extension():
    assert get_category(Path("random.xyz")) == "Other"

def test_organize_folder_moves_files(tmp_path):
    #Create test files
    image_file = tmp_path / "photo.jpg"
    text_file = tmp_path / "notes.txt"

    image_file.write_text("fake image")
    text_file.write_text("hello")

    result = organize_folder(tmp_path)

    assert result == {
        "Images": 1,
        "Text": 1,
    }

    assert (tmp_path / "Images" / "photo.jpg").exists()
    assert (tmp_path / "Text" / "notes.txt").exists()

def test_dry_run_does_not_move_files(tmp_path):
    image_file = tmp_path / "photo.png"
    image_file.write_text("fake image")

    result = organize_folder(tmp_path, dry_run=True)

    assert result == {"Images": 1}
    assert image_file.exists()
    assert not (tmp_path / "Images" / "photo.png").exists()