import argparse
import json
import logging
import sys

import os
import re

from gSed.lib import gSwap

logger = logging.getLogger("gswap")
logger.setLevel(logging.ERROR)
handler_stderr = logging.StreamHandler(sys.stderr)
logger.addHandler(handler_stderr)


def check_arg(args=None):
    """
    Check the arguments passed
    """
    parser = argparse.ArgumentParser(
        description='Script to swap gendered language')
    parser.add_argument('-i', '--input',
                        help='Input File instead of STDIN',
                        default='',
                        required=False)
    parser.add_argument('-o', '--output',
                        help='Output File instead of STDOUT',
                        default=None,
                        required=False)
    parser.add_argument('-r', '--results',
                        help='Filename to store swap results in',
                        default='swaps.json',
                        required=False)
    parser.add_argument('-c', '--context',
                        help='Filename to store context swap results in',
                        default='',
                        required=False)

    results = parser.parse_args(args)
    return results.input, results.output, results.results, results.context

def scan(input, output, results, context):

    surgeon = gSwap.gSwap()

    try:
        if input and not output:
            ext = os.path.splitext(input)[-1]
            output = input.replace(ext, ".gswap{ext}".format(ext=ext))

        # Set Output Stream
        if input and output:
            with open(input, 'r') as input_file:
                content = input_file.readlines()
            with open(output, 'w') as output_file:
                for line in content:
                    output_file.writelines(surgeon.swap(line))
        else:
            for line in iter(sys.stdin.readline, b''):
                sys.stdout.writelines(surgeon.swap(line))
    except KeyboardInterrupt:
        sys.stdout.flush()
        pass
    except Exception as ex:
        logging.error(ex)
        return 1

    if results:
        with open(results, 'a') as results_file:
            results_file.write(surgeon.swaps_perfomed())
    if context:
        with open(context, 'a') as context_file:
            context_file.write(surgeon.contexts_performed())

    return 0


if __name__ == '__main__':
    exit(scan(*check_arg()))
