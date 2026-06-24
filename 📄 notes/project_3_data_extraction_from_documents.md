# Project 3: Data Extraction from Documents Using Python

## Project Overview

In this project, I learned how pharmaceutical documents can be converted into AI-ready structured data using Python.

The goal is to extract important information from multi-page PDF documents such as:

- Manufacturing dates
- Effective dates
- Vendor names
- Document types
- Compliance information

This project focuses on building document extraction pipelines similar to those used in pharmaceutical compliance workflows.

---

## Why Unstructured Documents Are Challenging

Pharmaceutical SDFs (Supporting Documentation Files) are difficult to process because they contain:

- Multi-page layouts
- Mixed formatting
- Tables
- Headers and footers
- Scanned text
- Different date formats
- Noise and irrelevant information

Examples of SDF documents include:

- Quality Certificates
- Compliance Bulletins
- Chain of Custody forms

AI systems must identify important information while ignoring irrelevant text.

---

## Text Extraction and Bounding Boxes

Extracting text alone is not always enough.

AI systems also need to understand where text appears on the page.

Bounding boxes help capture:

- Text position
- Layout structure
- Relationships between labels and values

Example:

"Effective Date:" → "03-Jun-2025"

Bounding boxes help AI connect labels with the correct values.

---

## Why Bounding Boxes Matter

Bounding boxes help AI systems:

- Understand document layouts
- Process tables and columns
- Match labels with values
- Handle semi-structured documents
- Improve document understanding accuracy

Modern AI models such as LayoutLM use both:

- Text content
- Spatial positioning

---

## Python Libraries for PDF Extraction

### PyPDF2

PyPDF2 is a lightweight library for simple PDF text extraction.

Capabilities:
- Read PDFs
- Extract text
- Loop through pages

Limitations:
- No bounding box extraction
- Limited layout understanding

Example:
```python
from PyPDF2 import PdfReader

reader = PdfReader("sample.pdf")
page = reader.pages[0]

print(page.extract_text())
