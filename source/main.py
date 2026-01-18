"""App main."""
import json
import argparse
from whisper import decode

PARSER = argparse.ArgumentParser(description='Voice to json text with Whisper.')
PARSER.add_argument(
  "mp3_file",
  help="Mp3 file name for processing."
)
PARSER.add_argument(
  "json_file",
  help="Output json file name."
)


def main(options):
    """Entry point."""
    print("Decode {} -> {}...".format(options.mp3_file, options.json_file))
    json_data = decode(options.mp3_file, language='ru')
    with open(options.json_file, "wt", encoding="utf8") as out:
        out.write(json.dumps(json_data, indent=4, ensure_ascii=False).encode('utf8').decode())

    return 0


if __name__ == '__main__':  # pragma: no cover
    main(PARSER.parse_args())
