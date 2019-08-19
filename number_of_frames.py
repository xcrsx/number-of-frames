import gi
import sys
import os
gi.require_version("Gst", "1.0")
gi.require_version('GstPbutils', '1.0')
from gi.repository import GstPbutils
from gi.repository import Gst
from gi.repository import GLib

Gst.init("")


class TotalNumberOfFrames:
    def __init__(self, arg, uri=os.path.dirname(os.path.abspath(__file__))):
        self.arg = arg
        self.uri = uri
        stream = GstPbutils.Discoverer()
        path_1 = f'file://{self.arg}'
        path_2 = f'file://{uri}{self.arg}'
        try:
            self._info = stream.discover_uri(path_1)
        except GLib.Error:
            self._info = stream.discover_uri(path_2)

    def get_duration(self):
        duration = self._info.get_duration()
        # the method .get_duration() returns value in nanoseconds
        # we transform it in the seconds
        duration *= 10**-9
        return duration

    def get_fps(self):
        stream_info = self._info.get_video_streams()
        fps_num = stream_info[0].get_framerate_num()
        fps_denom = stream_info[0].get_framerate_denom()
        fps = round(fps_num / fps_denom)
        return fps

    def get_total_frames(self):
        duration = self.get_duration()
        fps = self.get_fps()
        total_frames = int(duration) * fps
        return total_frames


if __name__ == "__main__":
    try:
        frames_total = TotalNumberOfFrames(sys.argv[1])
        print(f'The number of frames in the file {sys.argv[1]}: '
              f'{frames_total.get_total_frames()}')
    except GLib.Error:
        print('File not found or invalid path')
