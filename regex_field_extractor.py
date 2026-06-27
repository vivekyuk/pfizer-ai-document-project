# =========================
# STEP 2: FIELD EXTRACTION (REGEX + ANCHORS)
# =========================

def extract_fields(text):
    """Extract key compliance fields from SDF text using regex patterns."""

    import re

    results = {}

    # -------------------------
    # DATES (multiple formats)
    # -------------------------
    date_patterns = [
        r"\d{2}-[A-Za-z]{3}-\d{4}",   # 03-Jun-2025
        r"\d{2}\s+[A-Z]{3}\s+\d{4}",  # 21 MAR 2025
        r"\d{4}-\d{2}-\d{2}"          # 2025-06-03
    ]

    dates = []
    for pattern in date_patterns:
        dates.extend(re.findall(pattern, text))

    results["dates"] = dates

    # -------------------------
    # VENDOR NAME (anchor-based)
    # -------------------------
    vendor_match = re.search(r"vendor[:\-]?\s*([A-Za-z0-9 &.,]+)", text, re.IGNORECASE)
    results["vendor"] = vendor_match.group(1).strip() if vendor_match else None

    # -------------------------
    # DOCUMENT ID
    # -------------------------
    doc_id_match = re.search(r"DOC-\d{4}-\d{4}", text)
    results["document_id"] = doc_id_match.group() if doc_id_match else None

    # -------------------------
    # EMAILS (if present)
    # -------------------------
    results["emails"] = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", text)

    # -------------------------
    # PHONE NUMBERS
    # -------------------------
    results["phones"] = re.findall(r"\+?\d[\d\s().-]{9,}", text)

    return results
