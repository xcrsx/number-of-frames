import pytest
import number_of_frames

from gi.repository import GLib

class TestTotalNumberOfFrames:

    def test_invalid_path(self):
        stream = number_of_frames.TotalNumberOfFrames()
        stream.path_1 = 'invalid path'
        stream.path_2 = 'invalid path'
        with pytest.raises(GLib.Error):
            stream.get_number_of_frames()

    def test_fps(self):
        stream = number_of_frames.TotalNumberOfFrames()
        stream.path_1 = f'file://{stream.uri}/test.mp4'
        stream.path_2 = f'file://{stream.uri}/test.mp4'
        assert stream.get_number_of_frames() == 50
