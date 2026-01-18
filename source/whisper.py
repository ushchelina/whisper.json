"""Whisper audio decode."""
from datetime import datetime, timedelta
import faster_whisper


class Model:
    """Whisper model to use."""

    Large = 'large'


class Device:
    """Device to use."""

    Gpu = 'cuda'
    Cpu = 'cpu'


MTYPES = {
  Device.Cpu: "int8",
  Device.Gpu: "float16"
}


def msec(sec):
    """Return int milliseconds for numpy float seconds."""
    return int(round(float(sec * 1000)))


# https://stackoverflow.com/questions/3173320/text-progress-bar-in-terminal-with-block-characters
def progress_bar(iteration, total, utc_time_start, length=100, fill='█'):
    """Call in a loop to create terminal progress bar."""
    decimals = 1
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    body = fill * filled_length + '-' * (length - filled_length)
    sec_done = int(round((datetime.utcnow() - utc_time_start).total_seconds()))
    sec_estimated = 0
    if iteration > 0:
        sec_estimated = int(round(sec_done * total / iteration))

    print("\rDecode |{}| {}% {} / {}          ".format(
      body, percent,
      timedelta(seconds=sec_done),
      timedelta(seconds=sec_estimated)
    ), end="\r")


def segments_to_json(segments, total_msec, progress, utc_time_start):
    """Decode whisper segments to json."""
    progress(0, total_msec, utc_time_start)

    data = []
    first_segment_offset = None

    for segment in segments:
        seg_data = [msec(segment.start), msec(segment.end - segment.start), segment.text.strip()]
        if first_segment_offset is None:
            first_segment_offset = seg_data[0]

        progress(seg_data[0] - first_segment_offset, total_msec, utc_time_start)

        words = []
        for word in segment.words:
            words.append([msec(word.start), msec(word.end - word.start), word.word.strip()])
        seg_data.append(words)
        data.append(seg_data)

    return data


def decode(mp3_file, language=None):
    """Return json data for decoded mp3 file."""
    print("Loading Whisper model...")
    whisper_model = faster_whisper.WhisperModel(
      Model.Large,
      device=Device.Cpu,
      compute_type=MTYPES[Device.Cpu]
    )

    print("Decode {} to wave ...".format(mp3_file))
    waveform = faster_whisper.decode_audio(mp3_file)

    print("Creating segments...")
    segments, info = whisper_model.transcribe(
      waveform, language, suppress_tokens=[-1],
      vad_filter=True,
      word_timestamps=True
    )
    duration = msec(info.duration_after_vad)
    print("Duration", duration, "msec")

    now = datetime.utcnow()
    data = segments_to_json(segments, duration, progress_bar, now)
    progress_bar(duration, duration, now)

    return data
