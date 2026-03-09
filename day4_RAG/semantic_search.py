import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


DOCUMENTS_FILE = "documents.txt"
QUERIES_FILE = "queries.txt"
RESULTS_FILE = "results.txt"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
TOP_K = 3


def load_lines(filepath: str) -> list[str]:
    with open(filepath, "r") as f:
        return [line.strip() for line in f if line.strip()]


def retrieve_top_k(
    query_embedding: np.ndarray,
    document_embeddings: np.ndarray,
    documents: list[str],
    k: int = TOP_K,
) -> list[tuple[str, float]]:
    similarity_scores = cosine_similarity(query_embedding, document_embeddings)[0]
    top_indices = np.argsort(similarity_scores)[::-1][:k]
    return [(documents[i], round(float(similarity_scores[i]), 4)) for i in top_indices]


def format_results(query: str, results: list[tuple[str, float]]) -> str:
    lines = [f"Query: {query}"]
    for rank, (document, score) in enumerate(results, start=1):
        lines.append(f"  {rank}. {document} ({score})")
    lines.append("-" * 60)
    return "\n".join(lines)


def main() -> None:
    documents = load_lines(DOCUMENTS_FILE)
    queries = load_lines(QUERIES_FILE)

    model = SentenceTransformer(EMBEDDING_MODEL)

    document_embeddings = model.encode(documents)

    all_results = []

    for query in queries:
        query_embedding = model.encode([query])
        top_results = retrieve_top_k(query_embedding, document_embeddings, documents)
        result_block = format_results(query, top_results)
        all_results.append(result_block)
        print(result_block)

    with open(RESULTS_FILE, "w") as f:
        f.write("\n".join(all_results))

    print(f"\nResults saved to {RESULTS_FILE}")


if __name__ == "__main__":
    main()
