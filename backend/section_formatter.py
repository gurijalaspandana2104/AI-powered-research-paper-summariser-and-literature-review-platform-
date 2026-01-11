def format_literature_review(summaries, contributors=None):

    formatted_text = ""

    # 🔹 Section 1: Overall Summary
    formatted_text += "1. OVERALL PAPER SUMMARY\n"
    formatted_text += "-" * 30 + "\n"
    formatted_text += summaries[0] + "\n\n"

    # 🔹 Section 2: Key Contributions
    formatted_text += "2. KEY CONTRIBUTIONS\n"
    formatted_text += "-" * 30 + "\n"
    for s in summaries[1:]:
        formatted_text += "- " + s.split(".")[0] + ".\n"
    formatted_text += "\n"

    # 🔹 Section 3: Methodology Overview
    formatted_text += "3. METHODOLOGY OVERVIEW\n"
    formatted_text += "-" * 30 + "\n"
    formatted_text += summaries[1] + "\n\n"

    # 🔹 Section 4: Findings and Results
    formatted_text += "4. FINDINGS AND RESULTS\n"
    formatted_text += "-" * 30 + "\n"
    formatted_text += summaries[2] + "\n\n"

    # 🔹 Section 5: Research Gaps & Future Scope
    formatted_text += "5. RESEARCH GAPS & FUTURE SCOPE\n"
    formatted_text += "-" * 30 + "\n"
    formatted_text += (
        "The study highlights important findings; however, future research can focus on "
        "broader datasets, alternative methodologies, and real-world validation.\n\n"
    )

    # 🔹 Section 6: Contributors (LAST)
    formatted_text += "6. CONTRIBUTORS\n"
    formatted_text += "-" * 30 + "\n"

    if contributors:
        for c in contributors:
            formatted_text += f"- {c}\n"
    else:
        formatted_text += "Not available\n"

    return formatted_text
