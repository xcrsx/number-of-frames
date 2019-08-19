import pytest
from number_of_frames import TotalNumberOfFrames

from gi.repository import GLib


class TestTotalNumberOfFrames:

    def test_invalid_path(self):
        with pytest.raises(GLib.Error):
            TotalNumberOfFrames('invalid path', 'invalid path')

    def test_duration(self):
        stream = TotalNumberOfFrames('/SPAM.mp4')
        assert stream.get_duration() == 2.0

    def test_fps(self):
        stream = TotalNumberOfFrames('/SPAM.mp4')
        assert stream.get_fps() == 25

    def test_total_frames(self):
        stream = TotalNumberOfFrames('/SPAM.mp4')
        assert stream.get_total_frames() == 50
