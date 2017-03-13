# mp3Convert
Convert mp3 files

`mp3convert` is a simple wrapper around ffmpeg that will convert mp3 files found in a source directory.

* Files are found in the source directory based on extension (.mp3 or .MP3).
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
-vn -ar 44100 -ac 2 -ab 64k -vol 400 -f mp3
```
The script also uses [Fire CLI](https://github.com/google/python-fire) in order
to expose the input parameters on the command line automatically.
