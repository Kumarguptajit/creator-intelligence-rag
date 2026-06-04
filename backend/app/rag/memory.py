chat_history = []


def add_message(
    role,
    content
):

    chat_history.append(
        {
            "role": role,
            "content": content
        }
    )


def get_history():

    return chat_history


def format_history():

    return "\n".join(
        [
            f"{msg['role']}: {msg['content']}"
            for msg in chat_history
        ]
    )