from pathlib import Path

def is_hidden(path: Path) -> bool:
    return path.name[0] == '.'
    
    # TO DO: Add .notemindignore check

def get_files(dir_path: Path) -> list[Path]:
    states = []
    for child in dir_path.iterdir():
        if is_hidden(child):
            continue

        # recursively search through dirs
        if child.is_dir():
            states += get_files(dir_path / child)
        else:
            states.append(child)

    return states
