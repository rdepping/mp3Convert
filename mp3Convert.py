#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fire
from ffmpy import FFmpeg
import os


def convertMp3(srcDir, destDir, dryRun=False):

    conversionParams = '-vn -ar 44100 -ac 2 -ab 64k -vol 400 -f mp3'

    for inputMp3 in os.listdir(srcDir):
        if inputMp3.endswith(".mp3") or inputMp3.endswith(".MP3"):
            if not os.path.exists(destDir):
                os.makedirs(destDir)
            ff = FFmpeg(
                inputs={os.path.join(srcDir, inputMp3): None},
                outputs={os.path.join(destDir, inputMp3): conversionParams})

            print('Command line : {cmd}')\
                .format(cmd=ff.cmd)
            if dryRun is False:
                ff.run()


def main():
    fire.Fire(convertMp3)


if __name__ == '__main__':
    main()
