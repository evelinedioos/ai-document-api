def cosine_similarity(vector_a, vector_b):

    dot_product = sum(a * b for a, b in zip(vector_a, vector_b))

    magnitude_a = sum(a * a for a in vector_a) ** 0.5
    magnitude_b = sum(b * b for b in vector_b) ** 0.5

    return dot_product / (magnitude_a * magnitude_b)

def find_most_relevant_chunks(question_embedding, chunks, top_k=3):

    scored_chunks = []

    for chunk in chunks:

        similarity = cosine_similarity(
            question_embedding,
            chunk["embedding"]
        )

        scored_chunks.append({
            "text": chunk["text"],
            "similarity": similarity
        })

    scored_chunks.sort(
        key=lambda x: x["similarity"], #lambda
        reverse=True
    )

    return scored_chunks[:top_k]