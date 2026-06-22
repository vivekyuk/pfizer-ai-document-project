# Project 2: Python for AI-Powered Document Processing

## Project Goal

Learn how Python is used to clean, organize, and prepare pharmaceutical documents for AI-powered automation.

## Why Data Preparation Matters

AI systems are only as good as the data they receive. Poor-quality data, inconsistent formatting, and noisy scans can lead to inaccurate predictions and extraction errors.

## Topics Covered So Far

* Python fundamentals
* Variables and data types
* Operators and basic calculations
* The print function
* Datetime module
* Google Colab environment

## Key Takeaways

* Python acts as the "glue" connecting data processing and AI models.
* Google Colab provides an easy environment for running Python code online.
* Clean, structured data is essential before applying AI techniques such as OCR and NLP.

## Connection to the Final Project

These skills will later be used to:

* Clean extracted text
* Process pharmaceutical documents
* Standardize data formats
* Prepare data for OCR and AI-powered search systems
## Additional Python Foundations

### Google Colab
- Cloud-based Python environment
- No installation required
- Automatically saves work to Google Drive
- Supports collaboration and free GPU/TPU access

### Important Libraries
- Pandas: data analysis and tabular data
- NumPy: numerical computing and arrays
- TensorFlow: machine learning and deep learning

### Python Data Structures
- Lists: ordered and changeable collections
- Tuples: ordered and unchangeable collections
- Sets: unordered collections of unique values
- Dictionaries: key-value pairs for storing structured information

### Control Flow
- Conditional statements:
  - if
  - if-else
  - if-elif-else

- Loops:
  - for loops
  - while loops

- Jump statements:
  - break
  - continue
  - pass

## Why This Matters for Document Processing

Python data structures and control flow are essential for:
- organizing extracted document information
- looping through multiple files
- storing metadata
- cleaning and transforming text data
- automating document processing pipelines
## Python Fundamentals Continued

### Functions
Functions are reusable blocks of code that perform specific tasks.

A function can:
- Take inputs (parameters)
- Perform operations
- Return outputs

Functions help make code:
- More organized
- Easier to reuse
- Easier to maintain

### Python Concepts Practiced
- Variables and data types
- Lists, tuples, sets, and dictionaries
- Conditional statements
- Loops (for and while)
- Functions with inputs and outputs

### Practice Exercises Completed
- Convert Celsius to Fahrenheit
- Check if a number is even or odd
- Return the larger of two numbers
- Calculate factorial using a loop
- Reverse a string
- Count vowels in a string

### Why This Matters for Document Processing

These programming fundamentals will later be used to:
- Process large collections of documents
- Clean and transform extracted text
- Build reusable document-processing functions
- Automate AI workflows
---

## Step 2: Data Preparation for AI Systems

In this step, I learned how AI systems require clean, structured data in order to function correctly. Raw pharmaceutical documents are often messy, inconsistent, and unstructured, so preprocessing is essential before applying AI models.

### Key Ideas Learned

Data preparation includes:

- Cleaning data (fixing errors, missing values, duplicates)
- Transforming data (standardizing formats, encoding values)
- Integrating multiple datasets
- Splitting data into training and testing sets

---

## Structured vs Unstructured Data

- Structured Data: CSV files, tables, databases (easy to analyze)
- Unstructured Data: PDFs, scanned documents, handwritten notes (requires preprocessing and OCR)

Pharmaceutical documents often fall into unstructured data, making preprocessing critical.

---

## Pandas (Data Handling Library)

Pandas is a Python library used for working with structured data.

Key abilities:
- Load datasets (CSV, Excel, etc.)
- Clean missing values
- Filter and sort data
- Perform analysis efficiently

Example operations:
- df.head()
- df.info()
- df.fillna()
- df.dropna()

---

## JSON Data Handling

JSON is a common format used in APIs and AI systems.

Python can:
- Convert JSON → Python dictionary (json.loads)
- Convert Python → JSON (json.dumps)
- Read JSON files (json.load)
- Write JSON files (json.dump)

JSON is widely used in:
- APIs
- Databases
- Machine learning pipelines
- Document processing systems

---

## Why This Matters

These skills are essential for AI-powered document processing because:

- Real-world data is messy and inconsistent
- AI models require structured input
- Cleaning improves model accuracy
- JSON and Pandas are standard tools in industry pipelines
### Why This Matters for Document Processing

These programming fundamentals will later be used to:
- Process large collections of documents  
- Clean and transform extracted text  
- Build reusable document-processing functions  
- Automate AI workflows  

---

## Step 2: Data Preparation for AI Systems

In this step, I learned how AI systems require clean, structured data in order to function correctly. Raw pharmaceutical documents are often messy, inconsistent, and unstructured, so preprocessing is essential before applying AI models.

### Key Ideas Learned

Data preparation includes:
- Cleaning data (fixing errors, missing values, duplicates)  
- Transforming data (standardizing formats, encoding values)  
- Integrating multiple datasets  
- Splitting data into training and testing sets  

---

## Structured vs Unstructured Data

- **Structured Data:** CSV files, tables, databases (easy to analyze)  
- **Unstructured Data:** PDFs, scanned documents, handwritten notes (requires preprocessing and OCR)  

Pharmaceutical documents often fall into unstructured data, making preprocessing critical.

---

## Pandas (Data Handling Library)

Pandas is a Python library used for working with structured data.

Key abilities:
- Load datasets (CSV, Excel, JSON)
- Clean missing values
- Remove duplicates
- Filter and sort data
- Perform analysis efficiently

Example operations:
- df.head() → preview data  
- df.info() → check structure and missing values  
- df.fillna() → handle missing values  
- df.dropna() → remove missing values  
- df.drop_duplicates() → remove duplicate records  

---

## JSON Data Handling

JSON is a common format used in APIs and AI systems.

Python can:
- Convert JSON → Python dictionary (json.loads)
- Convert Python → JSON (json.dumps)
- Read JSON files (json.load)
- Write JSON files (json.dump)

JSON is widely used in:
- APIs  
- Databases  
- Machine learning pipelines  
- Document processing systems  

---

## Nested JSON (Real-World Data)

Real-world JSON is often nested (data inside data), such as patient records with multiple visits or orders.

To handle it:
- Access data using keys and indexing  
- Flatten using pd.DataFrame()  
- Use json_normalize() for complex structures  

This is important in pharmaceutical datasets where patient and trial data is often deeply nested.  

---

## Why This Matters

These skills are essential for AI-powered document processing because:

- Real-world data is messy and inconsistent  
- AI models require structured input  
- Cleaning improves model accuracy  
- Proper preprocessing ensures reliable analysis of pharmaceutical documents

Step 3: Image Processing for AI Document Analysis

In this step, I learned how AI systems process and enhance images before performing OCR (Optical Character Recognition) and document analysis.

Key Concepts Learned

Computers interpret images as numerical pixel matrices:

Grayscale images use values from 0–255
Color images use RGB/BGR channels
Images can be represented as NumPy arrays
Common Document Image Problems

Real-world scanned documents often contain:

Noise and grain
Low contrast
Blurry text
Skewed alignment
Background shadows or stains

These issues reduce OCR accuracy and AI performance.

Image Processing Libraries
OpenCV (cv2)

Used for:

Advanced image preprocessing
OCR preparation
Thresholding
Denoising
Contrast enhancement
Pillow (PIL)

Used for:

Simple image editing
Cropping
Rotating
Resizing
Saving images
NumPy

Used for:

Pixel-level image manipulation
Matrix operations
Efficient numerical processing
Basic Image Processing Operations
Resize images
Crop important regions
Rotate and align documents
Convert images to grayscale
Save processed outputs
Why This Matters for Document Processing

These techniques are important because AI systems and OCR models require clean, readable images to:

Extract text accurately
Detect structured information
Improve pharmaceutical document analysis
Reduce OCR errors caused by blurry or noisy scans

## Step 3: Image Processing for AI & OCR

In this step, I learned how computers process images as pixel matrices and how image preprocessing improves OCR (Optical Character Recognition) performance in real-world document systems.

Raw images often contain noise, blur, low contrast, and misalignment, which can reduce AI accuracy. To fix this, I applied preprocessing techniques using OpenCV.

---

## Key Techniques Learned

### 1. Grayscale Conversion
Converts images into a single intensity channel to simplify processing.

### 2. Noise Reduction
Removes random speckles and artifacts using Non-Local Means Denoising.

### 3. Blurring
Smooths the image using Gaussian Blur to reduce small imperfections.

### 4. Contrast Enhancement
Improves readability of faint text using histogram equalization.

### 5. Thresholding (Binarization)
Converts images into black-and-white format for better OCR accuracy.

---

## Why This Matters for Document Processing

These techniques are essential for AI-powered document systems because:

- Scanned documents are often noisy or blurry
- OCR models perform better on clean, high-contrast images
- Preprocessing increases text extraction accuracy
- Helps automate document digitization in real-world systems

---

## Code Used (OpenCV Pipeline)

```python
import cv2
import matplotlib.pyplot as plt

image_path = "noisy_image_sample.jpg"
image = cv2.imread(image_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

denoised = cv2.fastNlMeansDenoising(gray, None, 30, 7, 21)

blurred = cv2.GaussianBlur(denoised, (5, 5), 0)

enhanced = cv2.equalizeHist(blurred)

processed = cv2.adaptiveThreshold(
    enhanced,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11,
    2
)

cv2.imwrite("cleaned_image.png", processed)

