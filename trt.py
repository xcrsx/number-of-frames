CLI='filesrc location=%s ! decodebin ! appsink name=sink' % filename
    pipeline=Gst.parse_launch(CLI)
    # get sink
    appsink=pipeline.get_by_name("sink")
    # set to PAUSED to make the first frame arrive in the sink
    pipeline.set_state(Gst.State.PAUSED)
    pipeline.seek_simple(Gst.Format.BUFFERS, Gst.SeekFlags.FLUSH, frame_number)
    smp = appsink.emit('pull-preroll')
    buf = smp.get_buffer()

    data=buf.extract_dup(0, buf.get_size())[:307200] # Only 1/2 of expected RGB size
    frame = np.fromstring(data,dtype='uint8').reshape((480,640,1))
