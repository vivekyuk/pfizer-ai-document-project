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

PROJECT 7 — DOCUMENT SEGMENTATION & QUERY ROUTING

Goal:
Build a page-level RAG system that can split multi-document PDFs into logical documents, classify pages, add metadata, and route queries to the correct document before retrieval.

KEY CONCEPTS:
- Large PDFs can contain multiple unrelated documents bundled together.
- Unstructured bundles cause wrong retrieval, hallucinations, and poor extraction.
- Page-level classification identifies document boundaries and document types.
- Metadata gives each page/chunk context such as doc_type, page number, doc_id, and source file.
- Query routing narrows down which document(s) to search before doing expensive semantic retrieval.

PAGE-LEVEL DETECTION:
For each page:
1. Decide whether it belongs to the same document as the previous page.
2. If it is a new document, classify its type.
3. Assign a document ID and metadata.

Example metadata:
{"page": 0, "doc_id": 0, "doc_type": "Cover Letter"}
{"page": 1, "doc_id": 0, "doc_type": "Cover Letter"}
{"page": 2, "doc_id": 1, "doc_type": "BSE/TSE Declaration"}

DOCUMENT TYPES:
- Cover Letter
- Certificate of Quality
- Packaging Specification
- BSE/TSE Declaration
- Material Description
- Supplier Qualification
- Chain of Custody
- Other/Unknown

PDF PAGE EXTRACTION:
- PyPDF2 can extract text page-by-page.
- PyMuPDF (fitz) can also extract PDF text.
- Each page can be stored as a dictionary containing page number and text.

PROMPT ENGINEERING:
LLMs need deterministic prompts for reliable automation.
Best practices:
- Restrict outputs to a fixed set of labels.
- Use JSON/CSV for structured responses.
- Include a fallback such as "Other" or "Unknown."
- Tell the model to return ONLY the required format.
- Use few-shot examples to improve consistency.
- Test prompts with ambiguous/borderline pages.

Example structured output:
{"doc_type": "Certificate of Quality"}

METADATA TAGGING:
Metadata = data about the document/chunk.
Useful fields:
- doc_type → type of document
- page_number → original page location
- source_file → PDF filename
- doc_id → logical document identifier
- chunk_index → chunk position
- page_start/page_end → page range

Metadata allows the system to:
- Filter retrieval
- Route queries
- Track where answers came from
- Improve accuracy
- Debug and audit results

LLAMAINDEX:
LlamaIndex Documents contain:
- text
- metadata

Metadata can be attached to pages/chunks before creating a VectorStoreIndex.

Example:
Document(
    text="...",
    metadata={
        "doc_type": "Certificate of Quality",
        "source_file": "pharma-blob-sample.pdf",
        "page_number": 5
    }
)

QUERY ROUTING:
Routing is a layer that decides WHERE to search before searching the actual chunks.

Workflow:
1. User asks a question.
2. A small LLM examines the query + document metadata/descriptions.
3. It predicts the relevant document type/file.
4. Metadata filters narrow the search.
5. Embeddings/vector search retrieves the best chunks from the narrowed set.
6. The LLM generates the final answer.

Why route first?
- Faster retrieval
- Lower compute/cost
- Less irrelevant context
- Fewer retrieval errors
- Reduced hallucination risk

METADATA + EMBEDDINGS:
Do not always search every chunk with embeddings.
Use:
- Metadata filters → structured/targeted queries
- Embeddings → vague/semantic queries
- Both → filter to relevant documents first, then perform semantic search

LOGICAL DOCUMENT GROUPING:
Pages can be reconstructed into logical documents using:
- is_new_doc
- doc_type
- page number

If a page starts a new document, create a new logical document.
If not, append the page to the current document.

CHUNKING:
After reconstructing logical documents, chunk each document separately.
Use RecursiveCharacterTextSplitter with:
- chunk_size
- chunk_overlap

IMPORTANT:
Never allow chunks to cross document boundaries.

VECTOR INDEX:
Chunks can be converted into LlamaIndex Documents with metadata and stored in a VectorStoreIndex using an embedding model such as BAAI/bge-small-en-v1.5.

RETRIEVAL:
Predict the query's doc_type first, then filter the vector index:
- doc_type
- page number
- source file
- other metadata

COMMON PITFALLS:
- Incorrect/missing doc_type labels
- No fallback for uncertain classifications
- Poor query classifier performance
- Searching the entire bundle instead of routing first
- Letting chunks combine different documents

PROJECT 7 TAKEAWAY:
Project 7 turns messy multi-document PDFs into structured, searchable information. The pipeline first detects document boundaries, classifies pages, attaches metadata, reconstructs logical documents, chunks them, and then routes user queries to the correct document before semantic retrieval.
