# =========================
# Pfizer Externship Project
# Simple Document Processor
# =========================


# -------------------------
# 1. LOAD DOCUMENT
# -------------------------
def load_document(file_path):
    """Reads a text file and returns its content."""
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    return text


# -------------------------
# 2. CLEAN TEXT
# -------------------------
def clean_text(text):
    """Basic cleaning of text."""
    text = text.lower()
    text = text.replace("\n", " ")
    text = text.strip()
    return text


# -------------------------
# 3. ANALYSIS
# -------------------------
def simple_analysis(text):
    """Basic analysis: word count + preview."""
    words = text.split()

    print("\n--- DOCUMENT ANALYSIS ---")
    print(f"Total words: {len(words)}")
    print(f"Preview: {' '.join(words[:30])}...")

# -------------------------
# 4. DOCUMENT STATISTICS
# -------------------------
def document_statistics(text):
    """Calculate basic document statistics."""
    words = text.split()
    characters = len(text)
    sentences = text.count(".") + text.count("!") + text.count("?")

    print("\n--- DOCUMENT STATISTICS ---")
    print(f"Word count: {len(words)}")
    print(f"Character count: {characters}")
    print(f"Sentence count: {sentences}")


# -------------------------
# 5. MAIN PIPELINE
# -------------------------
def main():
    file_path = "sample_output.txt"

    text = load_document(file_path)
    cleaned_text = clean_text(text)

    simple_analysis(cleaned_text)
    document_statistics(cleaned_text)
if __name__ == "__main__":
    main()
