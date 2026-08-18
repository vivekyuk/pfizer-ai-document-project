PROJECT 7 — Document Segmentation, Classification & Metadata

Project 7 focuses on making RAG work with messy, multi-document PDFs. Pharmaceutical PDFs can contain multiple documents such as certificates, packaging specifications, cover letters, and BSE/TSE declarations without clear boundaries.

GOAL:
Build a page-level RAG system that can:
- Detect document boundaries
- Classify document types
- Add metadata to pages
- Route queries to the correct document

1. WHY DOCUMENT BOUNDARIES MATTER

When multiple documents are bundled into one PDF, RAG may:
- Retrieve the wrong document
- Miss relevant information
- Mix unrelated documents
- Produce incorrect or hallucinated answers

Key idea: Process the PDF page by page instead of treating it as one document.

2. PAGE-LEVEL DETECTION

For each page, ask:
1. Is this page part of the same document as the previous page?
2. If not, what type of document is it?

If YES → keep the same doc_id and doc_type.
If NO → create a new doc_id and classify the new document.

Example:
Page 0 → Doc 0 → Cover Letter
Page 1 → Doc 0 → Cover Letter
Page 2 → Doc 1 → Certificate of Quality
Page 3 → Doc 1 → Certificate of Quality
Page 4 → Doc 2 → Packaging Specification

3. EXTRACTING PDF PAGES

PyPDF2 can extract text page by page:

from PyPDF2 import PdfReader

reader = PdfReader("pharma-blob-sample.pdf")
pages = [page.extract_text() for page in reader.pages]
doc_pages = [{"page_num": i, "text": p} for i, p in enumerate(pages)]

4. DOCUMENT CLASSIFICATION

Possible document types:
- Cover Letter
- Certificate of Quality
- Packaging Specification
- BSE/TSE Declaration
- Material Description
- Supplier Qualification
- Chain of Custody
- Other

A fixed set of labels makes classification more consistent and easier to automate.

5. PAGE-LEVEL METADATA

Each page can be assigned:
- page number
- document ID
- document type
- source file
- chunk index

Example:

{
  "page": 0,
  "doc_id": 0,
  "doc_type": "Cover Letter"
}

This metadata tells the RAG system what each page is and where it came from.

6. PROMPT ENGINEERING

LLMs can produce unpredictable outputs, so prompts should be deterministic.

Best practices:
- Use a fixed set of labels
- Require JSON/structured output
- Include an "Other" fallback
- Tell the model not to add explanations
- Use few-shot examples when useful

Example output:

{
  "is_new_doc": "Yes",
  "doc_type": "Certificate of Quality"
}

Structured outputs make the results easier to use in downstream tasks like routing, tagging, and extraction.

7. METADATA WITH LLAMAINDEX

Metadata adds context to each chunk/page.

Example:

Document(
    text="This batch meets all quality specifications...",
    metadata={
        "doc_type": "Certificate of Quality",
        "source_file": "pharma-blob-sample.pdf",
        "page_number": 5
    }
)

Useful metadata fields:
- doc_type → document category
- page_number → original page
- source_file → source PDF
- chunk_index → chunk position

8. BUILDING THE INDEX

Load the PDF:

from llama_index.readers.file import PDFReader

loader = PDFReader()
pages = loader.load_data("pharma-blob-sample.pdf")

Add metadata:

for i, doc in enumerate(pages):
    doc.metadata = {
        "page_number": i + 1,
        "source_file": "pharma-blob-sample.pdf"
    }

Then create the vector index:

from llama_index.core import VectorStoreIndex

index = VectorStoreIndex.from_documents(
    documents,
    embed_model=embed_model
)

9. METADATA FILTERING

Metadata allows the retriever to search only relevant document types.

Example:

filtered_results = [
    r for r in all_results
    if r.metadata.get("doc_type") == "BSE/TSE Declaration"
]

This prevents irrelevant documents from being used to answer the question.

KEY TAKEAWAYS:
- Bundled PDFs can break RAG because document boundaries are unclear.
- Process PDFs page by page.
- Use an LLM to detect boundaries and classify document types.
- Add metadata to every page/chunk.
- Use deterministic prompts and structured JSON outputs.
- LlamaIndex metadata enables filtered and traceable retrieval.
- Metadata-aware retrieval helps route questions to the correct document.
