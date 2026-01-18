"""App main."""
import json
import argparse
from whisper import decode, Device

PARSER = argparse.ArgumentParser(description='Voice to json text with Whisper.')
PARSER.add_argument(
  "mp3_file",
  help="Mp3 file name for processing."
)
PARSER.add_argument(
  "json_file",
  help="Output json file name."
)
PARSER.add_argument(
  "--device",
  default=Device.Cpu,
  choices=[Device.Cpu, Device.Gpu],
  help="Used device. Default: {}".format(Device.Cpu)
)
PARSER.add_argument(
  "--language",
  default='ru',
  choices=['auto', 'en', 'ru'],
  help="Speakers language. Default ru."
)


def main(options):
    """Entry point."""
    print("Decode {} -> {}...".format(options.mp3_file, options.json_file))
    language = options.language
    if language == 'auto':
        language = None
    json_data = decode(options.mp3_file, options.device, language=language)
    with open(options.json_file, "wt", encoding="utf8") as out:
        out.write(json.dumps(json_data, indent=4, ensure_ascii=False).encode('utf8').decode())

    return 0


if __name__ == '__main__':  # pragma: no cover
    main(PARSER.parse_args())
