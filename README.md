# mp3Convert
Convert mp3 files to a set "profile"

`mp3convert` is a simple wrapper around ffmpeg that will convert mp3 files found in a source directory.

* Files are found in the source directory based on extension (.mp3 or .MP3).
* It will also convert files in aac with the .aac extension
* The destination directory will be created if it does not already exist.

The source and destination directories are specified on the command line
```
python mp3Convert.py src dest
```
It's possible to specify a dryRun as well by adding True
```
python mp3Convert.py src dest True
```
The conversion parameters for ffmpeg are currently hardcoded in `mp3Convert`.

```
-acodec libmp3lame -vn -ar 44100 -ac 2 -ab 64k -vol 400 -f mp3 -threads 4
```
The script also uses [Fire CLI](https://github.com/google/python-fire) in order
to expose the input parameters on the command line automatically.

The script was originally developed for converting the audio files for the [Irish Preachers Conference](http://www.irishpreachers.org) 
