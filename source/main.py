"""App main.

import subprocess
# ffmpeg -i xxx.m4a -vn output.mp3
print("ffmpeg", options.audio_file, "->", mp3)
ret = subprocess.run([
  "ffmpeg",
  "-y",
  "-i",
  options.audio_file,
  "-vn",
  mp3,
], check=True)
print("done with code:", ret)
"""
import json
import argparse
from whisper import decode as decode_whisper

PARSER = argparse.ArgumentParser(description='Voice to text with Whisper and Nemo.')
PARSER.add_argument(
  "mp3_file",
  help="Mp3 file for processing."
)
PARSER.add_argument(
  "json_file",
  help="Output json file."
)


def main(options):
    """Entry point."""
    print("Decode {} -> {}...".format(options.mp3_file, options.json_file))
    json_data = decode_whisper(options.mp3_file, language='ru')
    with open(options.json_file, "wt", encoding="utf8") as out:
        out.write(json.dumps(json_data, indent=4, ensure_ascii=False).encode('utf8').decode())

    return 0


if __name__ == '__main__':  # pragma: no cover
    main(PARSER.parse_args())
