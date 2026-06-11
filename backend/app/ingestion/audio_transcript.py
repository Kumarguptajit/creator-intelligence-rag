from faster_whisper import WhisperModel

model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)

def transcribe_audio(audio_path: str):

    try:

        segments, info = model.transcribe(
            audio_path,
            beam_size=1
        )

        transcript_parts = []

        for segment in segments:
            transcript_parts.append(
                segment.text.strip()
            )

        transcript = " ".join(
            transcript_parts
        ).strip()

        return transcript

    except Exception as e:

        print(f"Whisper error: {e}")

        return ""