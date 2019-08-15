import sys
import gi
import cv2

gi.require_version("Gst", "1.0")
gi.require_version('GstPbutils', '1.0')
from gi.repository import GstPbutils
from gi.repository import Gst as gst
from gi.repository import GObject as gobject


class Framerate:

    gst.init("")
    gobject.threads_init()

    def __init__(self):
        self.pipeline = gst.parse_launch('filesrc name=source ! decodebin name=decodebin ! fpsdisplaysink name=sink')
        self.source = self.pipeline.get_by_name("source")
        self.source.set_property("location", sys.argv[1])
        self.sink = self.pipeline.get_by_name('sink')
        self.sink.set_property('signal-fps-measurements', 1)

    def get_duration(self):
        self.pipeline.set_state(gst.State.PLAYING)
        self.pipeline.get_state(gst.CLOCK_TIME_NONE)
        fps = self.sink.get_property('')
        format_ = gst.Format.TIME
        duration = self.pipeline.query_duration(format_)[1]
        return (int(duration * 10**-9), fps)


if __name__ == '__main__':
    frames = Framerate()
    print(frames.get_duration())

