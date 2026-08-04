from sentence_transformers import SentenceTransformer
from sentence_transformers import util

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def semantic_score(user_answer, ideal_answer):

    emb1 = model.encode(
        user_answer,
        convert_to_tensor=True
    )

    emb2 = model.encode(
        ideal_answer,
        convert_to_tensor=True
    )

    similarity = util.cos_sim(
        emb1,
        emb2
    )

    return float(similarity) * 100