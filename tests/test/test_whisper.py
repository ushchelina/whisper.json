"""Module whisper.py tests.

make test T=test_whisper.py
"""
from datetime import datetime
from . import TestBase, mock_whisper


class TestWhisper(TestBase):
    """Module whisper.py."""

    def test_decode(self):
        """Check decode function."""
        import whisper

        faster_whisper = whisper.faster_whisper
        segments_to_json = whisper.segments_to_json

        whisper.faster_whisper = mock_whisper
        whisper.segments_to_json = lambda segments, duration, progress_bar, now: ['xxx']
        assert whisper.decode(self.fixture('short.mp3')) == ['xxx']

        whisper.faster_whisper = faster_whisper
        whisper.segments_to_json = segments_to_json

    def test_segments_to_json(self):
        """Check segments_to_json function."""
        from whisper import segments_to_json, progress_bar

        segments = [
          mock_whisper.Segment(
            0, 50, "xxx yyy",
            [
              mock_whisper.Word(0, 20, "xxx"),
              mock_whisper.Word(20, 50, "yyy"),
            ]
          ),
          mock_whisper.Segment(
            50, 100, "zzz www",
            [
              mock_whisper.Word(50, 80, "zzz"),
              mock_whisper.Word(80, 100, "www"),
            ]
          ),
        ]

        data = segments_to_json(segments, 100, progress_bar, datetime.utcnow())
        assert len(data) == 2
