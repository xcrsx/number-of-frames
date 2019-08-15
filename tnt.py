import sys
import gi
import cv2

gi.require_version("Gst", "1.0")
from gi.repository import Gst as gst
from gi.repository import GObject as gobject

gst.init("")
gobject.threads_init()

pipeline = gst.parse_launch('filesrc name=source ! decodebin name=decodebin ! fpsdisplaysink name=sink')
source = pipeline.get_by_name("source")
sink = pipeline.get_by_name('sink')
source.set_property("location", sys.argv[1])

pipeline.set_state(gst.State.PLAYING)
pipeline.get_state(gst.CLOCK_TIME_NONE)
format_ = gst.Format.TIME
duration = pipeline.query_duration(format_)[1]
duration = int(duration * 10**-9)


print(duration)


