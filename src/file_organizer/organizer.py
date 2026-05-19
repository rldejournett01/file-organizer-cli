import logging
import shutil
from pathlib import Path

from .config import FILE_CATEGORIES

logger = logging.getLogger(__name__)


def get_category(file_path: Path) -> str:
    extension = file_path.suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Other"


def organize_folder(folder_path: Path, dry_run: bool = False) -> dict[str, int]:
    if not folder_path.exists():
        raise FileNotFoundError(f"Folder '{folder_path}' does not exist.")

    if not folder_path.is_dir():
        raise NotADirectoryError(f"'{folder_path}' is not a directory.")

    moved_counts: dict[str, int] = {}

    for item in folder_path.iterdir():
        if item.is_dir():
            continue

        category = get_category(item)
        destination_folder = folder_path / category
        destination_path = destination_folder / item.name

        if not dry_run:
            logger.info(
                "Preparing move: %s -> %s",
                item.name,
                destination_path,
            )

            destination_folder.mkdir(exist_ok=True)
            shutil.move(str(item), str(destination_path))
            logger.info(
                "Moved file: %s -> %s",
                item.name,
                destination_folder,
            )
        else:
            logger.info(
                "Dry run only: %s would move to %s",
                item.name,
                destination_path,
            )

        moved_counts[category] = moved_counts.get(category, 0) + 1

    return moved_counts
