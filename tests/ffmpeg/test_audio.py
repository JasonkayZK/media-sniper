"""Test ffmpeg audio"""
import os.path

import pytest

from media_sniper.config import settings
from media_sniper.ffmpeg import audio

_audio_data_folder = os.path.join(settings.BASE_DIR, "resources")
_current_folder = os.path.dirname(os.path.abspath(__file__))

@pytest.mark.parametrize(
    ['clips', 'output_folder'],
    [
        (
            [
                os.path.join(_audio_data_folder, "sample-3s.wav"),
                os.path.join(_audio_data_folder, "sample-6s.wav"),
            ],
            os.path.join(_current_folder, 'test_output')
        ),
    ]
)
def test_merge(clips: [], output_folder: str):
    print()
    print(clips)
    print(output_folder)
    audio.merge(clips, output_folder, ".wav")
