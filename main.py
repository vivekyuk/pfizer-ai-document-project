# =========================
# Pfizer Externship Project
# Simple Document Processor
# =========================

import pandas as pd
import json
import re

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
# 5. TOP WORDS
# -------------------------
def top_words(text, n=5):
    """Find the most common words."""
    words = text.split()

    word_counts = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    sorted_words = sorted(
        word_counts.items(),
        key=lambda x: x[1],
        reverse=True
    )

    print("\n--- MOST COMMON WORDS ---")
    for word, count in sorted_words[:n]:
        print(f"{word}: {count}")


# -------------------------
# 6. STRUCTURED SUMMARY
# -------------------------
def build_summary(text):
    """Creates a structured summary for AI-ready document processing."""

    words = text.split()

    summary = {
        "word_count": len(words),
        "character_count": len(text),
        "sentence_count": text.count(".") + text.count("!") + text.count("?"),
        "sample_words": words[:10]
    }

    return summary


# -------------------------
# 7. STEP 2 DEMOS
# -------------------------
def pandas_demo():
    """Demonstrates basic Pandas data cleaning."""

    data = {
        "Name": ["Alice", "Bob", None, "David"],
        "Age": [25, None, 30, 22],
        "Score": [85, 90, 88, None]
    }

    df = pd.DataFrame(data)

    print("\n--- PANDAS DEMO ---")
    print(df)

    df["Age"] = df["Age"].fillna(df["Age"].mean())
    df["Score"] = df["Score"].fillna(df["Score"].mean())

    print("\nAfter Cleaning:")
    print(df)


def json_demo():
    """Demonstrates basic JSON handling."""

    json_str = '{"patient": "John", "age": 45, "drug": "DrugA"}'
    data = json.loads(json_str)

    print("\n--- JSON DEMO ---")
    print("Patient:", data["patient"])
    print("Drug:", data["drug"])


def text_cleaning_demo():
    """Demonstrates simple text cleaning techniques."""

    text = "  HELLO!!! Patient ID: PT001 @@ needs review...   "

    text = text.lower()
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'[@#]', '', text)

    print("\n--- TEXT CLEANING DEMO ---")
    print(text)


# -------------------------
# 8. STEP 3: IMAGE PROCESSING
# -------------------------
def image_processing_summary():
    """Displays image preprocessing concepts used in AI systems."""

    print("\n--- IMAGE PROCESSING CONCEPTS ---")

    concepts = [
        "Grayscale conversion",
        "Noise reduction (denoising)",
        "Gaussian blur for smoothing",
        "Contrast enhancement",
        "Adaptive thresholding",
        "OCR preprocessing pipelines",
        "Document image enhancement"
    ]

    for concept in concepts:
        print(f"- {concept}")


def image_preprocessing_pipeline():
    """Simulates image preprocessing workflow."""

    print("\n--- IMAGE PREPROCESSING PIPELINE ---")

    steps = [
        "Load scanned document image",
        "Convert image to grayscale",
        "Apply denoising filter",
        "Apply Gaussian blur",
        "Enhance contrast",
        "Apply adaptive thresholding",
        "Generate OCR-ready image"
    ]

    for step_number, step in enumerate(steps, start=1):
        print(f"Step {step_number}: {step}")


# -------------------------
# 9. STEP 4: PDF EXTRACTION CONCEPTS
# -------------------------
def pdf_extraction_summary():
    """Displays PDF extraction concepts."""

    print("\n--- PDF EXTRACTION LIBRARIES ---")

    libraries = {
        "PyPDF2": "Basic PDF text extraction",
        "pdfplumber": "Table and structured data extraction",
        "PyMuPDF": "Text + bounding box extraction"
    }

    for library, purpose in libraries.items():
        print(f"{library}: {purpose}")


def bounding_box_demo():
    """Demonstrates bounding box extraction concepts."""

    print("\n--- BOUNDING BOX EXTRACTION ---")

    sample_data = {
        "text": "Effective Date: 03-Jun-2025",
        "bounding_box": [120, 200, 350, 230]
    }

    print("Extracted Text:", sample_data["text"])
    print("Bounding Box Coordinates:", sample_data["bounding_box"])


# -------------------------
# 10. MAIN PIPELINE
# -------------------------
def main():
    file_path = "sample_output.txt"

    # Load + clean
    text = load_document(file_path)
    cleaned_text = clean_text(text)

    # Core analysis
    simple_analysis(cleaned_text)
    document_statistics(cleaned_text)
    top_words(cleaned_text)

    # Structured output
    summary = build_summary(cleaned_text)

    print("\n--- STRUCTURED SUMMARY ---")
    print(summary)

    # Step 2 demos
    pandas_demo()
    json_demo()
    text_cleaning_demo()

    # Step 3 demos
    image_processing_summary()
    image_preprocessing_pipeline()

    # Step 4 demos
    pdf_extraction_summary()
    bounding_box_demo()


# -------------------------
# RUN PROGRAM
# -------------------------
if __name__ == "__main__":
    main()

# -------------------------
# RUN PROGRAM
# -------------------------
if __name__ == "__main__":
    main()
