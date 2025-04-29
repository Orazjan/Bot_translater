import io
import tempfile
from pydub import AudioSegment
from faster_whisper import WhisperModel

model = WhisperModel("base", compute_type="int8")
ALLOWED_LANGUAGES = {"ky", "ru", "en"}


def transcribe_voice_bytes(voice_bytes: bytes) -> str | None:
    audio = AudioSegment.from_file(io.BytesIO(voice_bytes))

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp_wav:
        tmp_wav_path = tmp_wav.name

    audio.export(tmp_wav_path, format="wav")

    segments, info = model.transcribe(tmp_wav_path, language=None)

    if info.language not in ALLOWED_LANGUAGES:
        return None

    text = " ".join(segment.text for segment in segments)
    return text.strip()
