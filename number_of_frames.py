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
    def __init__(self):
        self.stream = GstPbutils.Discoverer()
        self.uri = os.path.dirname(os.path.abspath(__file__))
        self.path_1 = f'file://{sys.argv[1]}'
        self.path_2 = f'file://{self.uri}{sys.argv[1]}'

    def get_number_of_frames(self):
        try:
            path = self.path_1
            info = self.stream.discover_uri(path)
        except GLib.Error:
            path = self.path_2
            info = self.stream.discover_uri(path)
        duration = info.get_duration()
        stream_info = info.get_video_streams()
        fps_num = stream_info[0].get_framerate_num()
        fps_denom = stream_info[0].get_framerate_denom()
        fps = round(fps_num / fps_denom)
        total_frames = int(duration * 10**-9) * fps
        return total_frames


if __name__ == "__main__":
    try:
        stream = TotalNumberOfFrames()
        print(f'Количество фреймов в файле {sys.argv[1]}: {stream.get_number_of_frames()}')
    except GLib.Error:
        print('File not found or invalid path')
