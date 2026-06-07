import json
import redis

r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

KEY = "comparison_context"


def save_comparison_context(
    metadata_a,
    metadata_b,
    context_a,
    context_b
):

    data = {
        "metadata_a": metadata_a,
        "metadata_b": metadata_b,
        "context_a": context_a,
        "context_b": context_b
    }

    r.set(
        KEY,
        json.dumps(data)
    )


def get_comparison_context():

    data = r.get(KEY)

    if not data:
        return {}

    return json.loads(data)