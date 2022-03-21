# mp3Convert

## About
Convert mp3 files to a set "profile"

`mp3convert` is a simple wrapper around [ffmpeg](https://www.ffmpeg.org/ffmpeg.html) that will convert mp3 files found in a source directory tree.

* Files are found in the source directory structure recursively based on specific extensions (.mp3 or .MP3 or .aac).
* The destination directory will be created if it does not already exist.

The script also uses [Fire CLI](https://github.com/google/python-fire) in order
to expose the input parameters on the command line automatically.

The script was originally developed for converting the audio files for the [Irish Preachers Conference](https://www.irishpreachers.org) and the original windows bat file is included for reference.

## Setup

I recommend setting up a virtual environment using python3 and installing the requirements as follows:

```bash
virtualenv venv -p python3
source venv/bin/activate
pip install -r requirements
```

## How To Run
Simply call the script and specify the src directory tree containing the files to convert and an output directory. Note that the source directory structure is NOT preserved (so all source filenames need to be unique).
```
python mp3Convert.py src dest
```
It's possible to specify a dryRun as well by adding True. This will print out all the conversion commands that would be run
```
python mp3Convert.py src dest True
```
The conversion parameters for ffmpeg are currently hardcoded in `mp3Convert` and can be set there as needed prior to running the script.

```
-acodec libmp3lame -vn -ar 44100 -ac 2 -ab 64k -filter:a "volume=1.5" -f mp3
```
