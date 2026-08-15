# Project 6 — RAG Optimization & Retrieval Tuning

## Project Overview

Project 6 focuses on **optimizing a working RAG pipeline** rather than simply building one.

The goal is to experiment with different components of the RAG system and determine which combination produces the most accurate, relevant, and trustworthy answers for pharmaceutical documents.

### Main Goals

- Compare different **embedding models**
- Tune retriever parameters such as `top_k`
- Experiment with **similarity thresholds**
- Test **reranking**
- Compare different **LLMs**
- Compare baseline vs. optimized RAG performance
- Document the results and explain which configuration works best

### Final Project Output

By the end of the project, you should have:

- A documented **baseline vs. optimized RAG pipeline**
- A comparison of at least **2 embedding models**
- A comparison of at least **2 LLMs**
- Experiments with retrieval parameters
- A short explanation of which combination worked best and why

---

# 1. Comparing Open Embedding Models

## Why Embedding Models Matter

Embeddings allow AI to search based on **meaning**, rather than only exact keywords.

The embedding model determines how effectively the system understands relationships between pieces of text.

A better embedding model can lead to:

- Better chunk matching
- More relevant retrieval
- More accurate answers
- Better performance on technical/pharmaceutical documents

### Embedding Models

| Model | Description | Size | Best For |
|---|---|---:|---|
| `sentence-transformers/all-MiniLM-L6-v2` | Small, fast baseline | ~80MB | General-purpose retrieval |
| `BAAI/bge-small-en-v1.5` | Strong retrieval performance | ~110MB | Domain-specific QA |
| `intfloat/e5-small-v2` | Instruction-focused | ~110MB | Use-case-focused search |

### Swapping the Embedding Model

```python
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
