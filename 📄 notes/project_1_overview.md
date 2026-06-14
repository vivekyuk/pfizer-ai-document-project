# Project 1: Understanding AI Document Processing in Pharma

## Summary
Learned how pharmaceutical companies like Pfizer use AI to process large volumes of compliance and clinical documents.

## Key Ideas
- Pharmaceutical workflows rely heavily on document verification and compliance
- Manual document review creates delays and inefficiencies
- AI can help extract, classify, and flag important information from unstructured documents

## Goal of System
Build an AI-powered pipeline that can:
- Extract text from PDFs
- Identify important fields (dates, compliance info, etc.)
- Classify document types
- Enable fast search across large document sets

## Relevance
This connects to real-world supply chain and healthcare operations where speed and accuracy in documentation directly impact patient outcomes.

## AI Foundations

### Artificial Intelligence (AI)

Artificial Intelligence refers to systems that can perform tasks that normally require human intelligence, such as recognizing patterns, making predictions, and processing information.

### Machine Learning (ML)

Machine Learning is a subset of AI that learns from data rather than relying solely on explicitly programmed rules.

### Deep Learning

Deep Learning uses neural networks with multiple layers to identify complex patterns in large datasets and power many modern AI applications.

### Large Language Models (LLMs)

LLMs are trained on massive amounts of text and can summarize information, answer questions, generate content, and support document analysis.

### Natural Language Processing (NLP)

NLP allows computers to understand, interpret, and generate human language. It is a key component of document intelligence systems.

## Connection to This Project

The final Pfizer document intelligence system will combine multiple AI technologies:

* OCR to convert scanned documents into machine-readable text
* NLP to analyze document content
* LLMs to answer questions about documents
* Machine Learning techniques to classify and organize files

These technologies help reduce manual review time, improve accuracy, and support faster decision-making in pharmaceutical operations.

## Machine Learning, Deep Learning, and Generative AI

### Machine Learning

Machine Learning (ML) is a subset of Artificial Intelligence that learns patterns from data rather than relying entirely on explicitly programmed rules. ML models improve performance by training on large datasets and identifying relationships within the data.

Example:

* Email spam detection
* Fraud detection
* Recommendation systems

### Deep Learning

Deep Learning is a specialized branch of Machine Learning that uses artificial neural networks inspired by the structure of the human brain.

Neural networks consist of:

* Input layer
* Hidden layers
* Output layer

Deep learning can automatically identify complex patterns without requiring extensive manual feature engineering.

Applications include:

* Image recognition
* Speech recognition
* Language understanding

### Transformers and Attention

Transformer models, introduced in 2017, improved AI's ability to understand context within language.

A key innovation is the attention mechanism, which allows models to focus on the most relevant words in a sentence instead of processing information strictly in sequence.

This advancement enabled major breakthroughs in natural language processing.

### Generative AI

Generative AI is a subset of deep learning that creates new content based on patterns learned from large datasets.

Examples:

* Text generation
* Image generation
* Code generation
* Chatbots

Popular examples include ChatGPT, Gemini, and other large language models.

### Relevance to the Pfizer Project

The document intelligence system developed during this externship will combine multiple AI technologies:

* OCR to convert document images into text
* NLP to understand document content
* Transformer-based language models to answer questions
* Machine learning techniques to classify and organize pharmaceutical documents

Together, these technologies can help reduce manual document review and improve operational efficiency in pharmaceutical supply chains.

## Machine Learning, LLMs, and NLP (Extended Foundation)

### Machine Learning (ML)

Machine Learning is a subset of AI where systems learn patterns from data instead of being explicitly programmed. It improves as it is exposed to more data.

### Deep Learning

Deep Learning uses neural networks with multiple layers to automatically learn complex patterns from large datasets.

### Large Language Models (LLMs)

LLMs generate text by predicting the next word in a sequence based on patterns learned from massive datasets. They are trained on large amounts of text and refined through fine-tuning and human feedback.

### Natural Language Processing (NLP)

NLP helps computers understand and process human language by converting unstructured text into structured data.

Common NLP tasks include:

* Tokenization (splitting text into words)
* Named Entity Recognition (extracting key information like dates, organizations, products)
* Sentiment analysis (detecting emotion or tone)

### How Everything Connects

* AI = the overall system
* Machine Learning = systems learning from data
* Deep Learning = advanced ML using neural networks
* NLP = how AI understands language
* LLMs = systems that generate language using deep learning + NLP

### Why This Matters for Pfizer Externship

Pharmaceutical documents are unstructured and complex. NLP and LLMs help:

* Extract key information from compliance documents
* Classify document types automatically
* Identify important dates, products, and organizations
* Reduce manual review time in healthcare workflows

## Computer Vision and OCR

### Computer Vision (CV)

Computer Vision is a field of AI that allows computers to “see” and interpret images and videos. Instead of eyes, computers use algorithms to analyze visual data and identify patterns.

Common applications:

* Self-driving cars (detecting pedestrians and road signs)
* Healthcare (analyzing medical scans)
* Document processing (reading scanned forms and reports)

### Optical Character Recognition (OCR)

OCR is a subset of Computer Vision that focuses on extracting text from images or scanned documents and converting it into machine-readable text.

Example:

* Turning a scanned PDF or image of a document into editable text

### How OCR is Used in Real Life

In industries like pharmaceuticals, OCR is used to:

* Extract information from compliance documents
* Read quality certificates and technical reports
* Reduce manual document processing

### How CV and OCR Fit into AI

* AI → the overall system
* Machine Learning → learns patterns from data
* Deep Learning → powers modern vision systems (especially CNNs)
* Computer Vision → allows AI to interpret images
* OCR → extracts text from images (a key CV application)

### Relevance to Pfizer Externship

This is a core part of the project because pharmaceutical companies deal with:

* Scanned compliance documents
* Vendor certificates
* Technical PDFs and reports

OCR will later be used to convert these documents into usable text so AI models can analyze and classify them.

## Pharmaceutical Industry Basics

The pharmaceutical industry discovers, develops, manufactures, and distributes medicines.

Drug development process:
- Discovery
- Preclinical Testing
- Clinical Trials
- FDA Review
- Manufacturing & Distribution

Key fact:
- Drug development typically takes 10–15 years.
- Only a small percentage of discovered compounds become approved medicines.

### Three Main Areas of Pharma

1. Research & Development (R&D)
   - Drug discovery and clinical research

2. Manufacturing
   - Producing medicines under GMP standards

3. Clinical Supply & Operations
   - Managing materials, documentation, and clinical trial support

## Pharmaceutical Compliance

Pharmaceutical companies must maintain documentation proving components are safe, compliant, and traceable.

Documentation should generally be reviewed every 3–4 years because:
- Regulations change
- Manufacturing processes change
- Testing standards evolve

Poor documentation management can lead to:
- FDA citations
- Product recalls
- Delayed drug approvals

## Vendor Documentation Files

Vendor files often contain multiple document types in one PDF:

- Quality Certificates
- Compliance Bulletins
- Technical Support Bulletins
- Formulation Characteristics
- Engineering Drawings
- Certificates of Analysis (COA)

A single file may contain documents spanning many years.

## Date Extraction Challenges

Documents contain multiple date formats:
- 21 MAR 2025
- 03-Jun-2025
- 23 Nov 2009

Common date types:
- Manufacturing Date
- Effective Date
- Signature Date
- Revision Date
- Issue Date

Different dates serve different compliance purposes.

## Relevance to Project

The AI document intelligence system will:
- Use OCR to extract text from documents
- Classify document types
- Extract important dates and compliance information
- Flag outdated documentation
- Reduce manual review work
