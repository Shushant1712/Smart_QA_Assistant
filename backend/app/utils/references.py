def format_references(raw_references: list):
    """
    Clean, deduplicate, and format document references
    coming from retrieved chunks.
    """

    formatted = []
    seen = set()

    for ref in raw_references:
        # Create a unique key to avoid duplicate references
        key = (
            ref.get("source"),
            ref.get("page"),
            ref.get("slide"),
            ref.get("sheet")
        )

        if key in seen:
            continue

        seen.add(key)

        citation = {
            "source": ref.get("source")
        }

        # Add only available location info
        if ref.get("page") is not None:
            citation["page"] = ref.get("page")

        if ref.get("slide") is not None:
            citation["slide"] = ref.get("slide")

        if ref.get("sheet") is not None:
            citation["sheet"] = ref.get("sheet")

        formatted.append(citation)

    return formatted
