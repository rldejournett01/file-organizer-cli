from file_organizer.organizer import organize_folder


def test_cli_workflow(tmp_path):
    (tmp_path / "photo.png").write_text("img")

    result = organize_folder(tmp_path)

    assert result["Images"] == 1
