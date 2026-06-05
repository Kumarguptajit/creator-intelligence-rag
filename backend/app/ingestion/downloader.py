import os
import tempfile

from yt_dlp import YoutubeDL


def download_audio(url: str):

    temp_dir = tempfile.mkdtemp()

    output_template = os.path.join(
        temp_dir,
        "%(id)s.%(ext)s"
    )

    opts = {
        "format": "bestaudio/best",
        "outtmpl": output_template,
        "quiet": True,
        "noplaylist": True
    }

    with YoutubeDL(opts) as ydl:

        info = ydl.extract_info(
            url,
            download=True
        )

        audio_file = ydl.prepare_filename(
            info
        )

    return audio_file