# number_of_frames

The script takes the path to the video file as an argument of the command line and returns the quantity of the frames in the file into stdout. GStreamer was used as a multimedia framework.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
$ pip install -r requirements.txt
```
To install GStreamer type these commands on the command line:
```bash
$ apt-get install libgstreamer1.0-0 gstreamer1.0-plugins-base 
gstreamer1.0-plugins-good gstreamer1.0-plugins-bad
gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-doc
gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-
gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio
``` 
## Usage
To run the script run the following command in the command line
```bash
$ python number_of_frames.py /home/usr/Videos/SPAM.mp4
```
You'll see
```bash
The number of frames in the file /home/usr/Videos/SPAM.mp4: 50
```
## Running the tests
Pytest library was used for tests. These tests test if the exception rise when the path is invalid also the correct duration, fps, and the number of frames in the testing example SPAM.mp4.
To run the tests cd in the directory of the project type this command on the command line: 
```bash
$ py-test -v
```
You'll see something like this:
```bash
============================= test session starts ==============================
platform linux -- Python 3.6.8, pytest-5.1.0, py-1.8.0, pluggy-0.12.0 --
/home/usr/projects/number_of_frames/env/bin/python3
cachedir: .pytest_cache
rootdir: /home/usr/projects/number_of_frames
collected 4 items                                                              

test_number_of_frames.py::TestTotalNumberOfFrames::test_invalid_path PASSED [ 25%]
test_number_of_frames.py::TestTotalNumberOfFrames::test_duration PASSED  [ 50%]
test_number_of_frames.py::TestTotalNumberOfFrames::test_fps PASSED       [ 75%]
test_number_of_frames.py::TestTotalNumberOfFrames::test_total_frames PASSED [100%]

============================== 4 passed in 0.17s ===============================
```
