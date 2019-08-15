import sys
import gi
import cv2

gi.require_version("Gst", "1.0")
from gi.repository import Gst as gst
from gi.repository import GObject as gobject

gst.init("")
gobject.threads_init()
pipeline = 'filesrc name=source ! decodebin name=decodebin ! appsink name=sink'
d = gst.parse_launch(pipeline)
source = d.get_by_name("source")
decodebin = d.get_by_name('decodebin')
sink = d.get_by_name('sink')
source.set_property("location", sys.argv[1])

d.set_state(gst.State.PLAYING)
d.get_state(gst.CLOCK_TIME_NONE)
format_ = gst.Format.TIME
duration = d.query_duration(format_)[1]
duration = int(duration * 10**-9)


print(duration)


