from pathlib import Path

def is_hidden(path: Path) -> bool:
    return path.name[0] == '.'
    
    # TO DO: Add .notemindignore check

def get_files(dir_path: Path) -> list[Path]:
    files = []
    for child in dir_path.iterdir():
        if is_hidden(child):
            continue

        # recursively search through dirs
        if child.is_dir():
            files += get_files(dir_path / child)
        else:
            files.append(child)

    return files
