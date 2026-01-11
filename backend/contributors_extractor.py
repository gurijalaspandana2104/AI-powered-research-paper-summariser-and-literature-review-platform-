# import re

# def extract_contributors(text):
#     """
#     Extract probable author names from research paper text.
#     Uses heuristic rules (safe & explainable).
#     """

#     # Only look at beginning of paper
#     head = text[:1500]

#     # Remove emails
#     head = re.sub(r'\S+@\S+', '', head)

#     # Common stop words
#     stop_words = [
#         "abstract", "introduction", "keywords",
#         "journal", "conference", "university",
#         "department", "received", "accepted"
#     ]

#     lines = head.split("\n")
#     candidates = []

#     for line in lines:
#         line = line.strip()

#         # Skip short or noisy lines
#         if len(line) < 5 or len(line) > 120:
#             continue

#         # Skip lines with stop words
#         if any(word in line.lower() for word in stop_words):
#             continue

#         # Heuristic: Names often contain capitalized words
#         if re.match(r'^([A-Z][a-z]+(\s[A-Z][a-z]+)+)', line):
#             candidates.append(line)

#     # Deduplicate & limit
#     contributors = list(dict.fromkeys(candidates))[:5]

#     if contributors:
#         return contributors
#     else:
#         return ["Contributors not clearly detected"]
import re

def extract_contributors(text):
    """
    Robust author extractor for research papers.
    Works across IEEE, Springer, Elsevier, arXiv.
    """

    # 1️⃣ Only first page / first section
    head = text[:3000]

    # 2️⃣ Stop at Abstract
    head = re.split(r'\bAbstract\b', head, flags=re.IGNORECASE)[0]

    # 3️⃣ Remove emails, affiliations, footnotes
    head = re.sub(r'\S+@\S+', '', head)
    head = re.sub(r'\d+', '', head)
    head = re.sub(r'\(.*?\)', '', head)

    lines = head.split("\n")
    possible_authors = []

    for line in lines:
        line = line.strip()

        # Skip noise
        if len(line) < 5 or len(line) > 150:
            continue

        # Skip affiliations / orgs
        if any(word in line.lower() for word in [
            "university", "department", "institute",
            "laboratory", "school", "college",
            "journal", "conference"
        ]):
            continue

        # Likely author line → contains commas or multiple names
        if "," in line or len(line.split()) <= 8:
            possible_authors.append(line)

    if not possible_authors:
        return ["Authors not clearly detected"]

    # 4️⃣ Split names properly
    authors = []
    for line in possible_authors:
        parts = re.split(r',| and ', line)
        for p in parts:
            name = p.strip()
            if re.match(r'^[A-Z][a-zA-Z.\- ]+$', name):
                authors.append(name)

    # 5️⃣ Deduplicate & limit
    authors = list(dict.fromkeys(authors))[:6]

    return authors if authors else ["Authors not clearly detected"]
