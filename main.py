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
# 7. STEP 2: REGEX FIELD EXTRACTION (NEW)
# -------------------------
def extract_fields(text):
    """Extract key compliance fields using regex + anchor logic."""

    results = {}

    # -------------------------
    # DATES (multiple formats)
    # -------------------------
    date_patterns = [
        r"\d{2}-[A-Za-z]{3}-\d{4}",   # 03-Jun-2025
        r"\d{2}\s+[A-Z]{3}\s+\d{4}",  # 21 MAR 2025
        r"\d{4}-\d{2}-\d{2}"          # 2025-06-03
    ]

    dates = []
    for pattern in date_patterns:
        dates.extend(re.findall(pattern, text))

    results["dates"] = dates

    # -------------------------
    # VENDOR (ANCHOR-BASED)
    # -------------------------
    vendor_match = re.search(r"vendor[:\-]?\s*([a-zA-Z0-9 &.,]+)", text)
    results["vendor"] = vendor_match.group(1).strip() if vendor_match else None

    # -------------------------
    # DOCUMENT ID
    # -------------------------
    doc_id_match = re.search(r"DOC-\d{4}-\d{4}", text)
    results["document_id"] = doc_id_match.group() if doc_id_match else None

    # -------------------------
    # EMAILS
    # -------------------------
    results["emails"] = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", text)

    # -------------------------
    # PHONE NUMBERS
    # -------------------------
    results["phones"] = re.findall(r"\+?\d[\d\s().-]{9,}", text)

    return results


# -------------------------
# 8. STEP 3: IMAGE PROCESSING
# -------------------------
def image_processing_summary():
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

    for i, step in enumerate(steps, 1):
        print(f"Step {i}: {step}")


# -------------------------
# 9. STEP 4: PDF EXTRACTION CONCEPTS
# -------------------------
def pdf_extraction_summary():
    print("\n--- PDF EXTRACTION LIBRARIES ---")

    libraries = {
        "PyPDF2": "Basic PDF text extraction",
        "pdfplumber": "Table and structured extraction",
        "PyMuPDF": "Text + bounding box extraction"
    }

    for lib, desc in libraries.items():
        print(f"{lib}: {desc}")


def bounding_box_demo():
    print("\n--- BOUNDING BOX EXAMPLE ---")

    sample = {
        "text": "Effective Date: 03-Jun-2025",
        "bbox": [120, 200, 350, 230]
    }

    print(sample)


# -------------------------
# 10. MAIN PIPELINE (UPDATED)
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

    # Structured summary
    summary = build_summary(cleaned_text)

    print("\n--- STRUCTURED SUMMARY ---")
    print(summary)

    # -------------------------
    # STEP 2 OUTPUT (NEW)
    # -------------------------
    print("\n--- STEP 2: FIELD EXTRACTION (REGEX) ---")
    fields = extract_fields(cleaned_text)
    print(fields)

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
