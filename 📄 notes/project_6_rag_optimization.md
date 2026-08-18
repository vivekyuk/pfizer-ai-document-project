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
## Open-Source AI Models

### What Are Open-Source AI Models?

Open-source AI models are models whose code, architecture, weights, or other components are made available for people to use, modify, and run themselves.

Closed-source models like ChatGPT or Claude are controlled by the companies that build them. Users can access the models, but generally cannot inspect or modify the underlying system.

### Why Open-Source AI Matters

For pharmaceutical document processing, open-source models can be especially useful because they provide:

- **Privacy** → Sensitive documents can potentially be processed locally instead of being sent to an external API.
- **Cost savings** → Local models avoid per-request API costs.
- **Customization** → Models can be adapted or fine-tuned for specific tasks.
- **Control** → Organizations control the model, infrastructure, and deployment.
- **Fewer rate limits** → Local deployment allows the organization to control usage.

### Open-Source vs. Closed-Source AI

| Open-Source AI | Closed-Source AI |
|---|---|
| Can be run on your own hardware | Usually accessed through a company's service/API |
| Greater control and customization | Limited customization |
| Can keep sensitive data local | Data may need to be sent to an external provider |
| No per-request API cost when run locally | Often uses usage-based pricing |
| Requires more setup and computing resources | Usually easier to use |
| Can be fine-tuned for specific tasks | Provider controls model updates |

Closed-source models may still be preferable when you need:

- State-of-the-art reasoning
- Easy, plug-and-play access
- No local computing requirements
- Minimal setup

### Why Use Open-Source AI for Document Processing?

For pharmaceutical documents, privacy and control are especially important.

Open-source models can allow companies to:

- Process sensitive pharmaceutical or clinical documents locally.
- Reduce API costs.
- Customize models for pharmaceutical terminology and workflows.
- Avoid depending entirely on an external AI provider.
- Build specialized RAG systems for internal use.

---

## Open-Source Models Used in the Externship

The externship focuses on using open-source models to generate answers from retrieved chunks in a RAG pipeline.

### 1. Mistral-7B

**Best for:** RAG pipelines, document retrieval, and question answering.

- Provides a strong balance between performance and efficiency.
- Works well for text-based Q&A.
- Suitable for document retrieval applications.
- Requires memory optimization when running in Google Colab.

**Best choice when:** Answer quality is more important than minimizing resource usage.

### 2. Phi-2

**Best for:** Lightweight experiments and quick RAG testing.

- Smaller and faster than larger models.
- Can run on limited hardware.
- Useful for experimenting with RAG pipelines.
- Has limitations with long documents and complex tasks.

**Best choice when:** You want a lightweight model that is easy to experiment with.

### 3. TinyLlama (1.1B)

**Best for:** Extremely lightweight experiments.

- Very small compared with larger language models.
- Can run on low-end hardware.
- Requires fewer computational resources.
- Performance is lower than larger models such as Mistral-7B.

**Best choice when:** Hardware and memory are very limited.

### Model Comparison

| Model | Strength | Limitation | Best Use |
|---|---|---|---|
| **Mistral-7B** | Strong performance | Requires more memory | RAG + document Q&A |
| **Phi-2** | Fast and lightweight | Limited context/capability | Quick experiments |
| **TinyLlama 1.1B** | Extremely lightweight | Lower performance | Low-resource testing |

### Quick Decision Guide

- **Mistral-7B** → Best overall choice for document retrieval and RAG.
- **Phi-2** → Best for lightweight experimentation.
- **TinyLlama** → Best when computational resources are very limited.

---

## Key Takeaways

1. **Open-source AI** gives organizations greater control, privacy, and customization.
2. **Closed-source AI** is generally easier to use and can provide stronger state-of-the-art performance without requiring local hardware.
3. Open-source models are useful for **pharmaceutical document processing** because sensitive information can potentially remain within an organization's infrastructure.
4. **Mistral-7B** provides a strong balance of quality and efficiency for RAG.
5. **Phi-2** is useful for fast, lightweight experiments.
6. **TinyLlama** is ideal for low-resource environments but sacrifices performance.
7. Choosing a model involves balancing **accuracy, speed, memory requirements, privacy, cost, and customization**.

### Key Takeaway

**Open-source AI provides freedom, privacy, customization, and control, making it valuable for specialized applications such as pharmaceutical document assistants.**
