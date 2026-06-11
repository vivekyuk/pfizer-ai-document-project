# Pfizer Externship Project - Simple Document Processor

def load_document(file_path):
    """Reads a text file and returns its content."""
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    return text


def clean_text(text):
    """Basic cleaning of text."""
    text = text.lower()
    text = text.replace("\n", " ")
    text = text.strip()
    return text


def simple_analysis(text):
    """Very basic analysis: word count + preview."""
    words = text.split()

    print("\n--- DOCUMENT ANALYSIS ---")
    print(f"Total words: {len(words)}")
    print(f"Preview: {' '.join(words[:30])}...")


def main():
    file_path = "sample_output.txt"  # we'll create this next

    text = load_document(file_path)
    cleaned = clean_text(text)

    simple_analysis(cleaned)


if __name__ == "__main__":
    main()
