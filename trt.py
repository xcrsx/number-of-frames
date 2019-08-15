import gi
import sys
import os
gi.require_version("Gst", "1.0")
gi.require_version('GstPbutils', '1.0')
from gi.repository import GstPbutils
from gi.repository import Gst


Gst.init("")


class Stream:
    def __init__(self):
        self.stream = GstPbutils.Discoverer()
        self.uri = os.path.dirname(os.path.abspath(__file__))

    def get_duration_in_frames(self):
        try:
            info = self.stream.discover_uri('file://' + sys.argv[1])
        except:
            info = self.stream.discover_uri('file://' + self.uri + '/' + sys.argv[1])
        duration = info.get_duration()
        stream_info = info.get_video_streams()
        fps_num = stream_info[0].get_framerate_num()
        fps_denom = stream_info[0].get_framerate_denom()
        fps = round(fps_num / fps_denom)
        print(fps)
        total_frames = int(duration * 10**-9) * fps
        return total_frames


if __name__ == "__main__":
    stream = Stream()
    print(stream.get_duration_in_frames())
