#!/usr/bin/env python3
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
from pathlib import Path


def mp3convert(src_dir, dest_dir, dry_run=False):

    # 44khz stereo at 64kb
    conversion_params = '-acodec libmp3lame -vn -ar 44100 -ac 2 -ab 64k -filter:a "volume=1.5" -f mp3'

    for input_file in list(Path(src_dir).rglob("*.[mMa][pPa][3c]")):

        # We found at least one file to convert, ensure the output directory exists
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # Ensure the final file extension for the target is lowercase mp3
        output_file = os.path.join(dest_dir, input_file.stem + '.mp3')
        if Path(output_file).exists():
            print(f'{output_file} already exists in destination path skipping...')
            continue

        ff = FFmpeg(
            inputs={os.path.join(src_dir, input_file): None},
            outputs={output_file: conversion_params})

        print(f'Command line : {ff.cmd}')

        if dry_run is False:
            ff.run()


def main():
    # Fire exposes the input parameters to the convert method via the command
    # line
    fire.Fire(mp3convert)


if __name__ == '__main__':
    main()
