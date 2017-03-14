#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
# mp3Convert
#
# Converts audio files to mp3 using a fixed set of parameters
# - ensures that a set of mp3 (or aac) files are converted to a set mp3 profile
###############################################################################
import fire
from ffmpy import FFmpeg
import os


def convertMp3(srcDir, destDir, dryRun=False):

    conversionParams = '-acodec libmp3lame -vn -ar 44100 -ac 2 -ab 64k\
        -vol 400 -f mp3 -threads 4'

    for inputFile in os.listdir(srcDir):
        if inputFile.endswith(".mp3") or inputFile.endswith(".MP3") or \
                inputFile.endswith(".aac"):

            # We found one file to convert, ensure the output directory exists
            if not os.path.exists(destDir):
                os.makedirs(destDir)

            # Ensure the file extensiton for the target is mp3
            outputFile = os.path.splitext(inputFile)[0]+'.mp3'

            ff = FFmpeg(
                inputs={os.path.join(srcDir, inputFile): None},
                outputs={os.path.join(destDir, outputFile): conversionParams})

            print('Command line : {cmd}')\
                .format(cmd=ff.cmd)

            if dryRun is False:
                ff.run()


def main():
    # Fire exposes the input parameters to the convert method via the command
    # line
    fire.Fire(convertMp3)


if __name__ == '__main__':
    main()
