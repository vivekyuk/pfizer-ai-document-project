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
# Project 3: Data Extraction from Documents Using Python (Step 1)

## Goal of This Step
In this step, I learned how to extract text and layout information from PDF documents using Python libraries. The focus was on understanding how unstructured pharmaceutical documents can be converted into machine-readable formats.

---

## Why PDF Extraction Matters in Pharma

Pharmaceutical compliance documents (SDFs) often contain:
- Manufacturing dates
- Vendor names
- Revision dates
- Compliance information

These are often hidden across multi-page PDFs, making manual extraction slow and error-prone. Python helps automate this process.

---

## Libraries Used

### PyPDF2
- Simple text extraction
- No layout or position data
- Best for basic PDFs

### pdfplumber
- Better structured text extraction
- Strong table detection
- Useful for semi-structured documents

### PyMuPDF (fitz)
- Most powerful tool in this step
- Extracts:
  - Text
  - Word positions (bounding boxes)
  - Block-level structure
- Best for AI-driven document processing

---

## Key Concept: Bounding Boxes

Bounding boxes represent the position of each word on a page using coordinates:
(x0, y0, x1, y1)

This allows AI systems to:
- Understand document layout
- Match labels with values (e.g., "Effective Date → 03-Jun-2025")
- Work with multi-column or complex PDFs

---

## Key Takeaways

- PDFs are not just text—they are structured layouts
- PyMuPDF is the most powerful library for spatial text extraction
- Bounding boxes are essential for AI document understanding
- Different libraries serve different purposes depending on document complexity

---

## Why This Matters for AI Systems

This step builds the foundation for:
- Automated document extraction pipelines
- Pharmaceutical compliance checks
- AI-powered data structuring
- Field extraction using regex and heuristics

---

## Next Step Preview

In Step 2, I will:
- Extract specific fields using regex
- Identify dates, vendor names, and document types
- Build rule-based extraction logic for SDF documents
Step 2: Identifying Fields Using Regex and Anchor Phrases

In this step, the goal is to convert raw extracted PDF text into structured fields such as vendor names, dates, document IDs, emails, and phone numbers. Instead of manually reading documents, pattern-based extraction is used to automatically identify important compliance information.

Why Regex Matters in Pharmaceutical Documents

Pharmaceutical SDFs are often messy and inconsistent:

Dates appear in multiple formats (03-Jun-2025, 21 MAR 2025)
Labels are not standardized (Vendor:, VENDOR -, etc.)
Important information may be buried in paragraphs or tables

Regex solves this by focusing on patterns instead of formatting, making it effective for real-world document extraction.

Anchor Phrase Strategy

Anchor phrases are fixed labels used to locate important values in text.

Example:
Vendor: West Pharmaceutical Services

Here:

Vendor: is the anchor phrase
West Pharmaceutical Services is the extracted value

This improves accuracy when document layouts vary.

What is Parsing

Parsing is the process of converting unstructured text into structured data.

Before:
West Pharma, document dated 21 MAR 2025, revision 11

After:
{
"vendor": "West Pharma",
"date": "21 MAR 2025",
"revision": "11"
}

This structured format is used in compliance systems for automation and analysis.

Key Challenges in Step 2
Multiple date formats in the same document
Broken text across lines in PDFs
Overmatching or incorrect regex patterns
Missing or inconsistent anchor phrases
Noise from headers, footers, and scanned content
Real-World Use Case (Pfizer Context)

This step is used in pharmaceutical compliance workflows to:

Extract vendor metadata automatically
Identify manufacturing, effective, and revision dates
Flag outdated documents older than 3–4 years
Reduce manual document review time
Enable scalable compliance processing pipelines
Key Takeaway

Regex combined with anchor phrases allows unstructured pharmaceutical documents to be converted into structured, machine-readable data that can be validated and used in automation systems.
