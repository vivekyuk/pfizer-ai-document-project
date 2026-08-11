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

