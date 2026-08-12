## Understanding AI Limitations

* Explored common limitations of Generative AI when working with real-world information.
* Learned how AI models can produce confident but incorrect information, known as **hallucinations**.
* Explored how AI can also be affected by:

  * Bias and fairness issues.
  * Limited ability to continuously learn from interactions.
  * Difficulties with complex reasoning.
  * Lack of interpretability and transparency.
* Learned why human oversight is especially important when using AI in high-stakes areas such as healthcare, finance, and pharmaceutical compliance.

## Retrieval-Augmented Generation (RAG)

* Learned how **Retrieval-Augmented Generation (RAG)** can reduce AI hallucinations by retrieving relevant information before generating an answer.
* Studied the three main stages of RAG:

  * **Retrieval** — searches a trusted database for relevant documents.
  * **Augmentation** — adds the retrieved information to the AI's context.
  * **Generation** — uses the retrieved information to generate a response.
* Learned how RAG can ground AI responses in actual pharmaceutical documents instead of relying only on pre-trained knowledge.
* Explored how RAG can be used for pharmaceutical compliance, research, and document-based question answering.

## RAG Pipeline

* Learned the main stages involved in building a RAG system:

  * Loading documents.
  * Indexing and organizing information.
  * Storing searchable information.
  * Retrieving relevant content.
  * Generating and evaluating responses.
* Learned how documents can be broken into smaller sections or **chunks** to make relevant information easier to retrieve.
* Explored how vector databases allow systems to search based on meaning rather than exact keyword matches.

## LlamaIndex

* Explored **LlamaIndex** as a framework for connecting LLMs with external data sources.
* Learned how LlamaIndex can help AI systems:

  * Load documents such as pharmaceutical SDFs.
  * Organize documents into searchable chunks.
  * Retrieve relevant information.
  * Generate responses based on retrieved content.
* Studied the main components of a LlamaIndex RAG pipeline:

  * **Data Loaders** — extract information from documents and other data sources.
  * **Indexing** — organizes information into searchable chunks and embeddings.
  * **Retrievers** — find relevant information based on a user's question.
  * **Query Engine** — uses the retrieved information to generate an answer.

## LLMs and Embeddings

* Learned the difference between **LLMs** and **embedding models** in a RAG system.
* Used **Google Gemini** as the LLM for generating responses.
* Used Hugging Face `all-MiniLM-L6-v2` as the embedding model for document retrieval.
* Learned that embedding models convert text into numerical representations that allow documents to be searched based on semantic meaning.
* Used embeddings to help identify relevant information even when the user's question doesn't use the exact wording found in the document.

## Pharmaceutical Document Retrieval

* Applied RAG concepts to pharmaceutical SDFs and compliance documents.
* Focused on retrieving information directly from source documents instead of relying on general AI knowledge.
* Explored how RAG can help answer questions about:

  * Product information.
  * Quality certificates.
  * Testing procedures.
  * Batch information.
  * Compliance requirements.
* Learned how grounding AI responses in source documents can make document-based AI systems more reliable and useful.

## Key Takeaways

* AI models can hallucinate and produce incorrect information even when the response sounds confident.
* RAG helps reduce hallucinations by retrieving relevant information from trusted documents before generating an answer.
* LlamaIndex provides tools for loading, organizing, retrieving, and querying external documents.
* **LLMs** generate responses, while **embedding models** help find relevant information.
* RAG is especially useful for pharmaceutical workflows where answers need to be grounded in specific documents and accurate source information.

Understanding Chunking

Estimated Time to Read: 20 minutes
notion image
 
In the last module, you learned about embeddings—how AI maps the meaning of words and ideas into numbers, making search smarter and more accurate.
But before AI can even create embeddings, it faces another big challenge: How do you feed a huge document into the AI without overwhelming it?
That’s the job for chunking.
 
In this module, you’ll learn how to break down long documents into smaller, meaningful pieces. You’ll explore different chunking strategies, why chunk size matters, and how smart chunking helps AI find exactly what it needs, without getting lost in a sea of text. 
notion image
Let’s begin!
 
Chunking: The Key to Handling Long Documents
Chunking is exactly what it sounds like—breaking a long document into smaller, more manageable pieces. 
Instead of treating the document as one giant block of text, chunking ensures that AI can process it in bite-sized sections and retrieve only the most relevant parts.
Source
Source
Here’s why chunking is important:
If AI retrieves huge blocks of text, you have to dig through a bunch of irrelevant information.
If AI retrieves only the most relevant sections, you get precise, useful answers.
 
Example of Chunking:
Imagine you have a 1,000-word article on hiking gear. Instead of feeding the whole article into an AI model, it gets split into smaller "chunks," like this:
Chunk 1 (Intro to Hiking Gear, 150 words)
Chunk 2 (Backpacks & Features, 200 words)
Chunk 3 (Hiking Boots & Materials, 250 words)
Chunk 4 (Rain Gear & Weather Considerations, 180 words)
If you ask, "What’s the best hiking boot material?", AI searches the hiking boots chunk rather than the whole document.
 
Trade-offs in Chunking: Finding the Right Balance
Choosing the right chunk size (pieces of text) is a trade-off between context retention and retrieval precision. Here’s how different sizes impact AI performance:
Chunk Size
Pros
Cons
Small Chunks (50-200 tokens)
Precise, faster retrieval, avoids irrelevant data
May lose important context, leading to incomplete answers
Medium Chunks (200-500 tokens)
Best balance of precision & context retention
Requires careful tuning for best results
Large Chunks (500+ tokens)
Preserves more context, reducing loss of meaning
Slower retrieval, may contain too much irrelevant text
Different document types and AI applications need different chunk sizes.
Legal and medical documents → Larger chunks to retain meaning.
Quick Q&A chatbots → Smaller chunks for fast, focused answers.
In short:
Small chunks = precise but might lack context.
Big chunks = more context, but slower and messier.
Medium chunks = usually the best trade-off, but still requires tuning.
 
OPTIONAL READ: Here is a quick guide by LlamaIndex on this topic - 
 
Different Ways to Chunk a Document
Not all chunking strategies are created equal! The right method depends on your data type and how AI will retrieve information.
Source
Source
 
1. Fixed-Size Chunking
This method just splits the text into equal-sized pieces, no matter where sentences or topics start and end.
Divides text into equal-sized chunks (e.g., every 300 tokens), regardless of meaning.
✅ Pros
❌ Cons
Easy to implement → No extra processing needed
May cut off sentences mid-way
Works well for structured text
Context is not preserved naturally
📢 Best for: News articles, structured documents with uniform text flow.
 
2. Overlapping Chunking
Instead of clean breaks, this method overlaps chunks slightly to make sure important context isn’t lost.
✅ Pros
❌ Cons
Helps AI retain context
Uses more storage (some text gets indexed twice)
Improves accuracy for retrieving relevant text
Needs fine-tuning to get the overlap right
Example: If chunk 1 ends at sentence 10, chunk 2 might start from sentence 9, ensuring continuity.
Why This Helps
Without overlap, an AI might miss key context when responding to queries.
Without overlap: "The new policy applies to..." → AI doesn’t retrieve the earlier part of the rule.
With overlap: "The new policy applies to all employees starting next quarter." → AI gets the full context.
📢 Best for: Legal contracts, research papers, policy documents.
 
3. Semantic Chunking (The Smartest Method)
Instead of using word count, this method identifies natural topic breaks using embeddings.
Think of it like a book’s table of contents—it splits text where the topic naturally changes instead of after an exact number of words.
✅ Pros
❌ Cons
Preserves full meaning
Takes more processing power
Best for unstructured text (like research papers, legal docs, or books)
Requires AI to analyze content before splitting
📢 Best for: Long-form text like books, Wikipedia pages, and technical manuals.
 
4. Recursive Chunking (For Structured Documents)
How It Works
First, split the text by headings (H1, H2, etc.).
Then, break down each section into smaller chunks for better retrieval.
Think of it like organizing a report:
First, divide it into chapters (big sections).
Then, split those into paragraphs (smaller, focused chunks).
✅ Pros:
❌ Cons:
Keeps the document’s structure intact, making retrieval more precise
Requires clear headings or metadata to work
Works well for contracts, reports, and research papers
Not ideal for unstructured text
📢 Best for: Business reports, legal documents and research papers.
 
Choosing the Right Chunk Size & Strategy
Why Does Chunk Size Matter? Imagine trying to search a dictionary that only gives you one word at a time vs. one that gives you entire pages of related words. The right balance makes retrieval accurate & efficient.
How to Determine the Best Chunking Approach?
Document Type
Best Chunking Strategy
Reason
News Articles
Fixed-Length Chunking
Consistent structure, no need for deep context preservation
Legal Contracts
Semantic Chunking
Requires logical section breaks to preserve legal clauses
Research Papers
Overlapping Chunking
Ensures key points aren’t split across chunks
PDF Reports
Recursive Chunking
Maintains structure by using headings before chunking
Key Takeaway: The right chunking approach depends on the document type—structured text benefits from simple chunking, while complex documents need advanced strategies.
 
Why This Matters for AI-Powered Search
Let's say a pharmaceutical company is using AI to answer quality questions about their products.
A quality analyst asks: "What test method was used for sterilization?"
If the document isn't chunked properly, AI might return an entire page of technical data—forcing the analyst to dig through it.
With smart chunking, AI can grab just the one paragraph that actually answers the question.
This makes AI-powered tools way more efficient in pharmaceuticals, healthcare, compliance, and any field where documents are long and complex.
 
🔑
Quick Recap:
Why AI Struggles with Long Documents
AI models have a fixed memory window and forget earlier parts of long documents.
Too much text → AI includes irrelevant details, making responses vague.
Too little text → AI misses key details, leading to incomplete answers.
Keyword search limitations → AI finds exact matches but may miss related concepts.
How to Fix It: Embeddings & Chunking
Embeddings → AI understands meaning, not just keywords (e.g., "sterilization" ≈ "autoclave processing").
Chunking → Splits long documents into smaller, searchable sections, ensuring AI retrieves only relevant parts.
Best Chunking Methods for Different Documents
Fixed-Length Chunking → Simple but may break context.
Overlapping Chunking → Retains more context but uses extra storage.
Semantic Chunking → Best for meaning but requires processing.
Recursive Chunking → Maintains document structure (great for legal or research papers).
📌 Key Takeaway: AI-powered search works best when documents are properly chunked and indexed using embeddings, ensuring precise, context-aware answers!
😄
With this, you have reached the end of this module.
# Project 5 — Query Processing & Retrieval Optimization

## 1. Query Processing

### What is query processing?

Query processing helps AI understand **what the user is actually asking** before searching through documents.

A user's wording might not match the wording used in the document. Query processing helps bridge that gap by improving or rewriting the question before retrieval.

Example:

Without query processing:
"What are the storage conditions?"

The document might instead say:
"Recommended storage temperature"

With query processing:
"What are the recommended storage temperature and conditions for this product?"

This makes it easier for the RAG system to find the relevant information.

### Why query processing matters

Without query processing:
- AI might miss relevant information.
- The user's wording may not match the document.
- Search results can be too broad or unrelated.

With query processing:
- AI better understands the intent of the question.
- Queries can be rewritten using terminology from the documents.
- Retrieval becomes more accurate.

### Main Query Processing Techniques

#### Query Expansion

AI adds related words, synonyms, or additional context to the original question.

Example:

User Query:
"What is the expiration date?"

Expanded Query:
"What is the batch expiration date for this pharmaceutical product?"

Why it helps:
- Bridges terminology gaps.
- Helps when documents use terms like "shelf life" instead of "expiration date."
- Improves the chance of retrieving relevant information.

---

#### Query Rewriting

AI restructures the question so it better matches the language used in the document.

Example:

Original:
"Tell me about the test results."

Rewritten:
"What quality control test methods and results are documented in the certificate?"

Why it helps:
- Makes vague questions more specific.
- Improves matching with technical or legal documents.
- Helps retrieval focus on the right information.

---

#### Prompt Engineering

An LLM can clarify or reformulate a vague question before retrieval.

Example:

User:
"Does this batch comply?"

LLM reformulation:
"Are there GMP compliance records, quality test results, or certificates of quality for this batch?"

Why it helps:
- Breaks vague questions into more specific search terms.
- Gives the retrieval system a clearer target.
- Can improve results for complex questions.

### Key Idea

Better input → Better search → Better results

Query processing helps the RAG system search for **meaning and intent**, rather than only matching the exact words the user typed.


# 2. Retrieval Optimization

Even after improving the query, the RAG system might retrieve multiple possible answers.

The next problem is:

> Which retrieved result is actually the most useful?

This is where **reranking** and **hybrid retrieval** become important.


## 3. Retrieval Reranking

### What is reranking?

Reranking reorganizes retrieved results so that the **most useful and relevant information appears first**.

Example:

Query:
"What are the storage conditions for this product?"

Without reranking:
"Storage conditions are specified on the label."

With reranking:
"Store between 2°C and 8°C. Protect from light. Do not freeze."

The second result gives much more useful information, so it should be ranked higher.

### Why reranking matters

A retrieval system might find several relevant chunks, but they aren't all equally useful.

Reranking helps:
- Put the strongest results first.
- Remove or deprioritize irrelevant information.
- Give the LLM better context.
- Improve the accuracy of the final response.


## 4. Reranking Methods

### Embedding Similarity Reranking

Results are sorted based on how close their embeddings are to the query.

Best for:
- Simple semantic similarity.
- Fast retrieval ranking.

### Hybrid Reranking

Combines:
- Vector similarity
- Keyword matching

Best for:
- Situations where both exact terms and related meanings matter.

### LLM-Assisted Reranking

An LLM evaluates retrieved text and scores it based on how useful it would be for answering the question.

Best for:
- Contextually complex questions.
- Selecting results based on answer quality.
- Filtering out irrelevant information.

### Reranking Summary

| Method | How It Works | Best Use |
|---|---|---|
| Embedding Similarity | Ranks by vector similarity | Semantic matching |
| Hybrid Reranking | Combines keyword + vector similarity | Exact terms + meaning |
| LLM-Assisted | LLM scores the usefulness of results | Complex/contextual questions |


# 5. Hybrid Retrieval

### What is hybrid retrieval?

Hybrid retrieval combines **keyword search** and **vector search**.

Keyword search is good at finding exact terms, while vector search is better at finding related concepts.

Using both gives the RAG system the benefits of each approach.

### Keyword Search

Keyword search looks for exact words or phrases.

Example:

Query:
"What test results are in the certificate?"

Keyword search might find a section titled:

"Test Results"

### Vector Search

Vector search uses embeddings to find conceptually similar information.

It might find a paragraph about:

"Quality compliance records and certificates"

Even though the exact phrase "test results" might not appear, the content is still related.

### Hybrid Search

Hybrid search combines both results.

```text
User Query
     ↓
Keyword Search
     ↓
Exact Matches
     +
Vector Search
     ↓
Conceptually Similar Results
     ↓
Merge Results
     ↓
Rerank
     ↓
Best Relevant Results
     ↓
LLM
     ↓
Final Answer
