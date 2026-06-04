current_comparison = {}


def save_comparison_context(
    metadata_a,
    metadata_b,
    context_a,
    context_b
):

    global current_comparison

    current_comparison = {
        "metadata_a": metadata_a,
        "metadata_b": metadata_b,
        "context_a": context_a,
        "context_b": context_b
    }


def get_comparison_context():

    return current_comparison