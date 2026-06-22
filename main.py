# =========================

# Pfizer Externship Project

# Simple Document Processor

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

```
print("\n--- DOCUMENT ANALYSIS ---")
print(f"Total words: {len(words)}")
print(f"Preview: {' '.join(words[:30])}...")
```

# -------------------------

# 4. DOCUMENT STATISTICS

# -------------------------

def document_statistics(text):
"""Calculate basic document statistics."""
words = text.split()
characters = len(text)
sentences = text.count(".") + text.count("!") + text.count("?")

```
print("\n--- DOCUMENT STATISTICS ---")
print(f"Word count: {len(words)}")
print(f"Character count: {characters}")
print(f"Sentence count: {sentences}")
```

# -------------------------

# 5. TOP WORDS

# -------------------------

def top_words(text, n=5):
"""Find the most common words."""
words = text.split()

```
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
```

# -------------------------

# 6. STRUCTURED SUMMARY

# -------------------------

def build_summary(text):
"""Creates a structured summary for AI-ready document processing."""

```
words = text.split()

summary = {
    "word_count": len(words),
    "character_count": len(text),
    "sentence_count": text.count(".") + text.count("!") + text.count("?"),
    "sample_words": words[:10]
}

return summary
```

# -------------------------

# 7. STEP 2 DEMOS (PANDAS + JSON + TEXT CLEANING)

# -------------------------

def pandas_demo():
"""Demonstrates basic Pandas data cleaning."""

```
data = {
    "Name": ["Alice", "Bob", None, "David"],
    "Age": [25, None, 30, 22],
    "Score": [85, 90, 88, None]
}

df = pd.DataFrame(data)

print("\n--- PANDAS DEMO ---")
print(df)

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Score"] = df["Score"].fillna(df["Score"].mean())

print("\nAfter Cleaning:")
print(df)
```

def json_demo():
"""Demonstrates basic JSON handling."""

```
json_str = '{"patient": "John", "age": 45, "drug": "DrugA"}'
data = json.loads(json_str)

print("\n--- JSON DEMO ---")
print("Patient:", data["patient"])
print("Drug:", data["drug"])
```

def text_cleaning_demo():
"""Demonstrates simple text cleaning techniques."""

```
text = "  HELLO!!! Patient ID: PT001 @@ needs review...   "

text = text.lower()
text = re.sub(r'\s+', ' ', text).strip()
text = re.sub(r'[@#]', '', text)

print("\n--- TEXT CLEANING DEMO ---")
print(text)
```

# -------------------------

# 8. IMAGE PROCESSING SUMMARY

# -------------------------

def image_processing_summary():
"""Displays image preprocessing concepts used in AI systems."""

```
print("\n--- IMAGE PROCESSING CONCEPTS ---")

concepts = [
    "Grayscale conversion",
    "Image resizing",
    "Noise reduction",
    "Contrast enhancement",
    "Thresholding for OCR",
    "Document alignment correction"
]

for concept in concepts:
    print(f"- {concept}")
```

# -------------------------

# 9. MAIN PIPELINE

# -------------------------

def main():
file_path = "sample_output.txt"

```
# Load + clean
text = load_document(file_path)
cleaned_text = clean_text(text)

# Core analysis
simple_analysis(cleaned_text)
document_statistics(cleaned_text)
top_words(cleaned_text)

# Structured output
summary = build_summary(cleaned_text)

print("\n--- STRUCTURED SUMMARY ---")
print(summary)

# Step 2 demos
pandas_demo()
json_demo()
text_cleaning_demo()

# Step 3 concepts
image_processing_summary()
```

# -------------------------

# RUN PROGRAM

# -------------------------

if **name** == "**main**":
main()

