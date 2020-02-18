#!/usr/bin/env python3

'''rocketgit.py: a script that makes sure your git messages contain a 🚀'''
__author__ = "Jack Fox"
__email__ = "jfox13@nd.edu"

import sys
import subprocess

def has_rocket(lines: str) -> bool:
    ''' confirms that a message contains a rocket '''
    return '🚀' in lines

if __name__ == '__main__':
    lines = sys.argv
    lines[0] = 'git'

    if '-m' in lines and lines.index('-m') + 1 < len(lines):
        comment_index = lines.index('-m') + 1
        if not has_rocket(lines[comment_index]):
            lines[comment_index] = '{} 🚀'.format(lines[comment_index])

    process = subprocess.Popen(lines)