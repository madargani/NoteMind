from pathlib import Path

plain_text_exts = ('.txt', '.md')

def extract_text(file_path: Path) -> str | None:
    if file_path.suffix in plain_text_exts:
        return file_path.read_text()
    if file_path.suffix == '.pdf':
        # TODO: pdf text extraction
        return ''
    return None
