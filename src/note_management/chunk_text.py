from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_text(text: str) -> list[str]:
    text_splitter = RecursiveCharacterTextSplitter(
        separators=None, # default: ["\n\n", "\n", " ", ""]
        chunk_size=500, 
        chunk_overlap=0,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.split_text(text)

