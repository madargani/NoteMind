# Notes on Embedding Strategies

**Options explored:**
- OpenAI text-embedding-3-small (good quality, paid)
- BGE-Small (fast + open source)
- Instructor-Large (better with task-aware prompts)

**Chunking:**
- Naive: split by paragraphs
- Smart: token-aware with overlap

**Open questions:**
- Should we cache chunk metadata (e.g. parent file, chunk offset)?
- What’s the optimal chunk size for markdown vs plaintext?

