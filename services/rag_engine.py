import faiss
import numpy as np
import json
from services.openai_service import get_embedding

# -------------------------------------------------------
# INDEX FILES
# -------------------------------------------------------

INDEX_PATH = "data/services_index.bin"
META_PATH = "data/services_meta.json"

# -------------------------------------------------------
# VECTOR NORMALIZATION
# -------------------------------------------------------

def normalize(vec):
    vec = np.array(vec).astype("float32")
    norm = np.linalg.norm(vec)
    if norm == 0:
        return vec
    return vec / norm

# -------------------------------------------------------
# LOAD INDEX
# -------------------------------------------------------

try:
    index = faiss.read_index(INDEX_PATH)

    with open(META_PATH, "r", encoding="utf-8") as f:
        metadata = json.load(f)

except Exception:
    index = None
    metadata = []

# -------------------------------------------------------
# CORE SEARCH
# -------------------------------------------------------

def _search(query, top_k=5):

    if index is None or not metadata:
        return []

    query_vector = normalize(get_embedding(query))
    query_vector = np.array([query_vector]).astype("float32")

    scores, indices = index.search(query_vector, top_k)

    results = []

    for score, idx in zip(scores[0], indices[0]):

        if idx >= len(metadata):
            continue

        results.append({
            "title": metadata[idx]["title"],
            "url": metadata[idx]["url"],
            "score": float(score)
        })

    return results

# -------------------------------------------------------
# MAIN RECOMMENDATION ENGINE
# -------------------------------------------------------

def retrieve_recommendations(query, *args, **kwargs):
    """
    Fully backward compatible.

    Accepts:
    - top_k
    - threshold (ignored safely)
    - min_results
    - any other legacy arguments
    """

    # Extract safe parameters
    top_k = kwargs.get("top_k", 5)
    min_results = kwargs.get("min_results", 5)

    results = _search(query, top_k=top_k)

    # Sort by similarity score
    results = sorted(results, key=lambda x: x["score"], reverse=True)

    return results[:min_results]

# -------------------------------------------------------
# BACKWARD COMPATIBILITY FUNCTIONS
# -------------------------------------------------------

def retrieve_services(query, *args, **kwargs):
    """
    Old function used in optimizer/link_mapper.
    """
    return retrieve_recommendations(query, *args, **kwargs)


def get_best_service(query, *args, **kwargs):
    """
    Old function used in link_mapper.
    """
    results = retrieve_recommendations(query, top_k=1, min_results=1)
    return results[0] if results else None
