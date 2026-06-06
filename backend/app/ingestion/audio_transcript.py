from faster_whisper import WhisperModel


def transcribe_audio(audio_path: str):

    try:

        model = WhisperModel(
            "base",
            device="cpu",
            compute_type="int8"
        )

        segments, info = model.transcribe(
            audio_path,
            beam_size=5
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