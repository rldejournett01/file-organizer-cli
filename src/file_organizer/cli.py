from pathlib import Path
import argparse

from file_organizer.organizer import organize_folder

def main():
    #Reads the terminal input
    parser = argparse.ArgumentParser(description="Organize files into folders by file type.")

    #Creates a required positional argument
    parser.add_argument(
        "folder",
        help="folder to organize"
    )

    args = parser.parse_args()

    folder_path = Path(args.folder)

    results = organize_folder(folder_path)

    print("\nOrganization Complete\n")

    for category, count in results.items():
        print(f"{category}: {count} files moved")

if __name__ == "__main__":
    main()