"""Mocked Whisper."""


class Word:
    """Mocked Whisper decoded word."""

    def __init__(self, start, end, word):
        """Return mocked Segment."""
        self.start = start
        self.end = end
        self.word = word


class Segment:
    """Mocked Whisper decoded segment."""

    def __init__(self, start, end, text, words):
        """Return mocked Segment."""
        self.start = start
        self.end = end
        self.text = text
        self.words = words


class Info:
    """Mocked Whisper transcribe Info class."""

    def __init__(self, waveform):
        """Return mocked Info."""
        self.waveform = waveform
        self.duration_after_vad = 100


class WhisperModel:
    """Mocked WhisperModel."""

    def __init__(self, size, device=None, compute_type=None):
        """Return mocked model."""
        self.size = size
        self.device = device
        self.compute_type = compute_type

        self.language = None
        self.suppress_tokens = None
        self.vad_filter = True
        self.word_timestamps = True

    def transcribe(self, waveform, language, suppress_tokens=None, vad_filter=True, word_timestamps=True):
        """Mock transcribe method."""
        self.language = language
        self.suppress_tokens = suppress_tokens
        self.vad_filter = vad_filter
        self.word_timestamps = word_timestamps

        return None, Info(waveform)


def decode_audio(mp3):
    """Mock decode_audio function."""
    return mp3
