def create_chunks(text: str, chunk_size: int = 1000):

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)

    return chunks #dus interval is de chuncksize waarin je de text van de pdf gaat verdelen, en je maakt dus een lijst