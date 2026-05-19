import argparse
from pathlib import Path

from file_organizer.logger import setup_logging
from file_organizer.organizer import organize_folder


def main():
    print("\nFile Organizer started...")
    setup_logging()
    # Reads the terminal input
    parser = argparse.ArgumentParser(
        description="Organize files into folders by file type."
    )

    # Creates a required positional argument
    parser.add_argument("folder", help="folder to organize")

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview file moves without changing anything",
    )

    args = parser.parse_args()

    folder_path = Path(args.folder)

    results = organize_folder(folder_path, dry_run=args.dry_run)

    if not results:
        print("\nNothing to organize.\n")
        return

    if args.dry_run:
        print("\nDry Run Complete! [No files were moved]\n")

        print("\nSummary:")
        for category, count in results.items():
            print(f"{category}: {count} file(s) would be moved")

    else:
        print("\nOrganization Complete\n")

        print("\nSummary:")
        for category, count in results.items():
            print(f"{category}: {count} file(s) moved")


if __name__ == "__main__":
    main()
