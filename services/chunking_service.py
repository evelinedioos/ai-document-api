def create_chunks(text: str, chunk_size: int = 1000, overlap: int = 100):
    """
    Splits text into chunks on paragraph/sentence boundaries.
    overlap: aantal karakters dat herhaald wordt tussen chunks,
    zodat context niet verloren gaat aan de randen.
    """
    # Splits eerst op paragrafen
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]

    chunks = []
    current_chunk = ""

    for paragraph in paragraphs:
        # Past de paragraaf nog in de huidige chunk?
        if len(current_chunk) + len(paragraph) <= chunk_size:
            current_chunk += paragraph + "\n\n"
        else:
            # Sla huidige chunk op als die niet leeg is
            if current_chunk:
                chunks.append(current_chunk.strip())

            # Is de paragraaf zelf te lang? Splits op zinnen.
            if len(paragraph) > chunk_size:
                sentences = paragraph.replace(". ", ".|").split("|")
                current_chunk = ""
                for sentence in sentences:
                    if len(current_chunk) + len(sentence) <= chunk_size:
                        current_chunk += sentence + " "
                    else:
                        if current_chunk:
                            chunks.append(current_chunk.strip())
                        current_chunk = sentence + " "
            else:
                current_chunk = paragraph + "\n\n"

    # Vergeet de laatste chunk niet
    if current_chunk:
        chunks.append(current_chunk.strip())

    # Voeg overlap toe: begin elke chunk met einde van vorige
    if overlap > 0 and len(chunks) > 1:
        overlapped = [chunks[0]]
        for i in range(1, len(chunks)):
            previous_tail = chunks[i - 1][-overlap:]
            overlapped.append(previous_tail + " " + chunks[i])
        return overlapped

    return chunks