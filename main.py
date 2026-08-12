# =========================
# Pfizer Externship Project
# Document Processing + OCR + RAG
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
        "sentence_count": (
            text.count(".")
            + text.count("!")
            + text.count("?")
        ),
        "sample_words": words[:10]
    }

    return summary


# -------------------------
# 7. REGEX FIELD EXTRACTION
# -------------------------

def extract_fields(text):
    """Extract key compliance fields using regex + anchor logic."""

    results = {}

    # -------------------------
    # DATES
    # -------------------------

    date_patterns = [
        r"\d{2}-[A-Za-z]{3}-\d{4}",
        r"\d{2}\s+[A-Z]{3}\s+\d{4}",
        r"\d{4}-\d{2}-\d{2}"
    ]

    dates = []

    for pattern in date_patterns:
        dates.extend(re.findall(pattern, text))

    results["dates"] = dates

    # -------------------------
    # VENDOR
    # -------------------------

    vendor_match = re.search(
        r"vendor[:\-]?\s*([a-zA-Z0-9 &.,]+)",
        text,
        re.IGNORECASE
    )

    results["vendor"] = (
        vendor_match.group(1).strip()
        if vendor_match
        else None
    )

    # -------------------------
    # DOCUMENT ID
    # -------------------------

    doc_id_match = re.search(
        r"DOC-\d{4}-\d{4}",
        text,
        re.IGNORECASE
    )

    results["document_id"] = (
        doc_id_match.group()
        if doc_id_match
        else None
    )

    # -------------------------
    # EMAILS
    # -------------------------

    results["emails"] = re.findall(
        r"[\w\.-]+@[\w\.-]+\.\w+",
        text
    )

    # -------------------------
    # PHONE NUMBERS
    # -------------------------

    results["phones"] = re.findall(
        r"\+?\d[\d\s().-]{9,}",
        text
    )

    return results


# -------------------------
# 8. IMAGE PROCESSING
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
# 9. PDF EXTRACTION CONCEPTS
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
# 10. PROJECT 4: SDF OCR EXTRACTION
# -------------------------

def extract_sdf_fields(text):
    """Extract key pharmaceutical SDF fields."""

    results = {}

    # Gamma Process Run ID
    gamma_match = re.search(
        r"gamma\s+process\s+run\s+id[:\s-]*([A-Za-z0-9-]+)",
        text,
        re.IGNORECASE
    )

    results["gamma_process_run_id"] = (
        gamma_match.group(1)
        if gamma_match
        else None
    )

    # Product Lot Number
    lot_match = re.search(
        r"(?:product\s+)?lot\s+(?:number|no\.?)[:\s-]*([A-Za-z0-9-]+)",
        text,
        re.IGNORECASE
    )

    results["product_lot_number"] = (
        lot_match.group(1)
        if lot_match
        else None
    )

    # Minimum Specified Dose
    min_specified_match = re.search(
        r"minimum\s+specified\s+dose[:\s-]*([0-9.]+)",
        text,
        re.IGNORECASE
    )

    results["minimum_specified_dose"] = (
        min_specified_match.group(1)
        if min_specified_match
        else None
    )

    # Minimum Delivered Dose
    min_delivered_match = re.search(
        r"minimum\s+delivered\s+dose[:\s-]*([0-9.]+)",
        text,
        re.IGNORECASE
    )

    results["minimum_delivered_dose"] = (
        min_delivered_match.group(1)
        if min_delivered_match
        else None
    )

    # Maximum Specified Dose
    max_specified_match = re.search(
        r"maximum\s+specified\s+dose[:\s-]*([0-9.]+)",
        text,
        re.IGNORECASE
    )

    results["maximum_specified_dose"] = (
        max_specified_match.group(1)
        if max_specified_match
        else None
    )

    # Maximum Delivered Dose
    max_delivered_match = re.search(
        r"maximum\s+delivered\s+dose[:\s-]*([0-9.]+)",
        text,
        re.IGNORECASE
    )

    results["maximum_delivered_dose"] = (
        max_delivered_match.group(1)
        if max_delivered_match
        else None
    )

    return results


def create_json_output(sdf_fields):
    """Convert extracted SDF fields into AI-ready JSON."""

    return json.dumps(
        sdf_fields,
        indent=4
    )


def create_bounding_box_data():
    """Create example OCR bounding box data."""

    bbox_data = [
        {
            "text": "CERTIFICATE",
            "bbox": [120, 100, 300, 135],
            "confidence": 0.98
        },
        {
            "text": "Product Lot Number",
            "bbox": [120, 200, 350, 230],
            "confidence": 0.95
        }
    ]

    return bbox_data


# -------------------------
# 11. PROJECT 5: OCR ENGINE COMPARISON
# -------------------------

def ocr_engine_comparison():
    """Compare Tesseract, PaddleOCR, and EasyOCR."""

    print("\n--- OCR ENGINE COMPARISON ---")

    ocr_engines = {

        "Tesseract": {
            "strength": "Simple and lightweight OCR",
            "output": "Extracted text",
            "layout": "Limited layout awareness"
        },

        "PaddleOCR": {
            "strength": "Strong performance on complex documents",
            "output": "Text, confidence scores, and bounding boxes",
            "layout": "Strong layout and position awareness"
        },

        "EasyOCR": {
            "strength": "Easy to install and use",
            "output": "Text, confidence scores, and bounding boxes",
            "layout": "Good for simple forms and scanned documents"
        }
    }

    for engine, details in ocr_engines.items():

        print(f"\n{engine}")
        print(f"Strength: {details['strength']}")
        print(f"Output: {details['output']}")
        print(f"Layout: {details['layout']}")


# =====================================================
# PROJECT 5: RAG / CHUNKING / EMBEDDINGS
# =====================================================

# These libraries are required:
#
# pip install llama-index
# pip install llama-index-embeddings-huggingface
# pip install sentence-transformers


# -------------------------
# 12. CHUNKING
# -------------------------

def create_chunks(text, chunk_size=300, chunk_overlap=50):
    """Split document text into overlapping chunks."""

    try:

        from llama_index.core import Document
        from llama_index.core.node_parser import SentenceSplitter

        document = Document(text=text)

        splitter = SentenceSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

        chunks = splitter.get_nodes_from_documents(
            [document]
        )

        print("\n--- CHUNKING ---")
        print(f"Chunk size: {chunk_size}")
        print(f"Chunk overlap: {chunk_overlap}")
        print(f"Total chunks created: {len(chunks)}")

        return chunks

    except ImportError:

        print(
            "\nLlamaIndex is not installed. "
            "Run: pip install llama-index"
        )

        return []


# -------------------------
# 13. COMPARE CHUNKING
# -------------------------

def compare_chunking(text):
    """Compare different chunking strategies."""

    try:

        from llama_index.core import Document
        from llama_index.core.node_parser import SentenceSplitter

        print("\n--- CHUNKING COMPARISON ---")

        strategies = {
            "Fixed": (300, 0),
            "Overlapping": (300, 50),
            "Smaller": (150, 25)
        }

        results = {}

        for name, (size, overlap) in strategies.items():

            document = Document(text=text)

            splitter = SentenceSplitter(
                chunk_size=size,
                chunk_overlap=overlap
            )

            chunks = splitter.get_nodes_from_documents(
                [document]
            )

            results[name] = len(chunks)

            print(
                f"{name}: {len(chunks)} chunks "
                f"(size={size}, overlap={overlap})"
            )

        return results

    except ImportError:

        print(
            "\nLlamaIndex is not installed."
        )

        return {}


# -------------------------
# 14. EMBEDDINGS
# -------------------------

def create_embeddings(chunks):
    """Generate embeddings using MiniLM."""

    try:

        from llama_index.embeddings.huggingface import (
            HuggingFaceEmbedding
        )

        embed_model = HuggingFaceEmbedding(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        print("\n--- EMBEDDINGS ---")
        print(
            "Embedding model: "
            "sentence-transformers/all-MiniLM-L6-v2"
        )

        for chunk in chunks:

            chunk.embedding = (
                embed_model.get_text_embedding(
                    chunk.text
                )
            )

        print("Embeddings generated successfully.")

        return embed_model

    except ImportError:

        print(
            "\nEmbedding libraries are not installed."
        )

        return None


# -------------------------
# 15. VECTOR INDEX
# -------------------------

def create_vector_index(chunks, embed_model):
    """Create a vector index for semantic retrieval."""

    try:

        from llama_index.core import VectorStoreIndex

        index = VectorStoreIndex(
            chunks,
            embed_model=embed_model
        )

        print("\n--- VECTOR INDEX ---")
        print("Vector index created successfully.")

        return index

    except ImportError:

        print(
            "\nLlamaIndex is not installed."
        )

        return None


# -------------------------
# 16. VECTOR RETRIEVAL
# -------------------------

def retrieve_documents(index, query, top_k=3):
    """Retrieve relevant chunks using semantic search."""

    if index is None:
        print("\nVector index not available.")
        return []

    retriever = index.as_retriever(
        similarity_top_k=top_k
    )

    results = retriever.retrieve(query)

    print("\n--- VECTOR RETRIEVAL ---")
    print(f"Query: {query}")

    for i, node in enumerate(results, 1):

        print(f"\nResult {i}")

        print(
            node.get_content()[:300]
        )

    return results


# -------------------------
# 17. RAG PIPELINE SUMMARY
# -------------------------

def rag_pipeline_summary():
    """Display the main RAG pipeline stages."""

    print("\n--- RAG PIPELINE ---")

    steps = [
        "1. PDF/Text extraction",
        "2. Text cleaning",
        "3. Document chunking",
        "4. Embedding generation",
        "5. Vector indexing",
        "6. Semantic retrieval",
        "7. Relevant context selection",
        "8. LLM response generation"
    ]

    for step in steps:
        print(step)


# -------------------------
# 18. RAG QUERY EXAMPLES
# -------------------------

def rag_query_examples():
    """Display example pharmaceutical RAG questions."""

    print("\n--- RAG QUERY EXAMPLES ---")

    questions = [
        "What test methods were used for quality control?",
        "What are the storage conditions specified in the certificate?",
        "What is the product lot number?",
        "What is the expiration date?",
        "Who is the vendor?"
    ]

    for question in questions:
        print(f"- {question}")


# -------------------------
# 19. MAIN PIPELINE
# -------------------------

def main():

    file_path = "sample_output.txt"

    # -------------------------
    # LOAD + CLEAN
    # -------------------------

    text = load_document(file_path)
    cleaned_text = clean_text(text)

    # -------------------------
    # CORE ANALYSIS
    # -------------------------

    simple_analysis(cleaned_text)

    document_statistics(cleaned_text)

    top_words(cleaned_text)

    # -------------------------
    # STRUCTURED SUMMARY
    # -------------------------

    summary = build_summary(
        cleaned_text
    )

    print("\n--- STRUCTURED SUMMARY ---")
    print(summary)

    # -------------------------
    # FIELD EXTRACTION
    # -------------------------

    print(
        "\n--- STEP 2: FIELD EXTRACTION ---"
    )

    fields = extract_fields(
        cleaned_text
    )

    print(fields)

    # -------------------------
    # IMAGE PROCESSING
    # -------------------------

    image_processing_summary()

    image_preprocessing_pipeline()

    # -------------------------
    # PDF EXTRACTION
    # -------------------------

    pdf_extraction_summary()

    bounding_box_demo()

    # -------------------------
    # PROJECT 4:
    # SDF EXTRACTION
    # -------------------------

    print(
        "\n--- PHARMACEUTICAL SDF EXTRACTION ---"
    )

    sdf_fields = extract_sdf_fields(
        cleaned_text
    )

    print(sdf_fields)

    # -------------------------
    # AI READY JSON
    # -------------------------

    print(
        "\n--- AI READY JSON OUTPUT ---"
    )

    json_output = create_json_output(
        sdf_fields
    )

    print(json_output)

    # -------------------------
    # OCR BOUNDING BOX DATA
    # -------------------------

    print(
        "\n--- OCR BOUNDING BOX DATA ---"
    )

    bbox_data = create_bounding_box_data()

    print(
        json.dumps(
            bbox_data,
            indent=4
        )
    )

    # -------------------------
    # PROJECT 5:
    # OCR COMPARISON
    # -------------------------

    ocr_engine_comparison()

    # =================================================
    # PROJECT 5: RAG
    # =================================================

    print(
        "\n========================================"
    )

    print(
        "PROJECT 5: RAG PIPELINE"
    )

    print(
        "========================================"
    )

    # -------------------------
    # CHUNKING COMPARISON
    # -------------------------

    compare_chunking(
        cleaned_text
    )

    # -------------------------
    # CREATE OVERLAPPING CHUNKS
    # -------------------------

    chunks = create_chunks(
        cleaned_text,
        chunk_size=300,
        chunk_overlap=50
    )

    # -------------------------
    # EMBEDDINGS
    # -------------------------

    if chunks:

        embed_model = create_embeddings(
            chunks
        )

        # -------------------------
        # VECTOR INDEX
        # -------------------------

        if embed_model:

            index = create_vector_index(
                chunks,
                embed_model
            )

            # -------------------------
            # SEMANTIC RETRIEVAL
            # -------------------------

            retrieve_documents(
                index,
                "What are the quality control requirements?",
                top_k=3
            )

    # -------------------------
    # RAG PIPELINE SUMMARY
    # -------------------------

    rag_pipeline_summary()

    # -------------------------
    # RAG QUERY EXAMPLES
    # -------------------------

    rag_query_examples()


# -------------------------
# RUN PROGRAM
# -------------------------

if __name__ == "__main__":
    main()
