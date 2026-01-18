"""Module main.py tests.

make test T=test_main.py
"""
import json
from . import TestBase


class TestMain(TestBase):
    """Module main.py."""

    def test_main(self):
        """Check main function."""
        import main

        options = main.PARSER.parse_args([
            self.fixture('short.mp3'),
            self.build('short.json'),
        ])
        decode = main.decode

        def mock_decode(mp3, device, language=None):
            """Mock decode function."""
            print(mp3, device, language)
            return json.load(open(self.fixture('short.json'), 'r', encoding='utf-8'))

        main.decode = mock_decode

        assert main.main(options) == 0
        options.language = 'auto'
        assert main.main(options) == 0

        main.decode = decode
