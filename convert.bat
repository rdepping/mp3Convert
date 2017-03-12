---convert.bat----

set formats=*.mp3
set presets=-vn -ar 44100 -ac 2 -ab 32k -vol 400 -f mp3
set outputext=mp3new

for %%g in (%formats%) do start /b /wait "" "ffmpeg.exe" -i "%%g" %presets% "%%~ng.%outputext%" && TITLE "Converted: "%%g

--end---