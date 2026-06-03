from langchain_text_splitters import ( RecursiveCharacterTextSplitter )


def chunk_text(text, video_id):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=120
    )

    chunks = splitter.split_text(text)

    return [
        {
            "chunk_id": i,
            "video_id": video_id,
            "text": chunk
        }
        for i, chunk in enumerate(chunks)
    ]