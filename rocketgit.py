#!/usr/bin/env python3

'''rocketgit.py: a script that makes sure your git messages contain a 🚀'''
__author__ = "Jack Fox"
__email__ = "jfox13@nd.edu"

import sys
import subprocess
import os
import tempfile

TEMPFILE = 'tempfile.tmp'
EDITOR = os.environ.get('EDITOR','vim')

def has_rocket(lines: str) -> bool:
    ''' confirms that a message contains a rocket '''
    return '🚀' in lines

def handle_message_arg(lines: list) -> None:
    ''' handles -m args '''
    comment_index = lines.index('-m') + 1
    if not has_rocket(lines[comment_index]):
        lines[comment_index] = '{} 🚀'.format(lines[comment_index])
    process = subprocess.Popen(lines)

def handle_commit_no_arg(lines: list) -> None:
    ''' handles commit with no -m '''
    subprocess.call([EDITOR,TEMPFILE])

    with open(TEMPFILE, 'r') as message_file:
        message_content = message_file.read()

    if not '🚀' in message_content:
        with open(TEMPFILE, 'a') as message_file:
            message_file.write(" 🚀")

    comment_index = lines.index('commit') + 1
    lines.insert(comment_index,TEMPFILE)
    lines.insert(comment_index,'-F')
    process = subprocess.call(lines)
    process = subprocess.call(['rm',TEMPFILE])

if __name__ == '__main__':
    lines = sys.argv
    lines[0] = 'git'

    # git commit -m
    if '-m' in lines and lines.index('-m') + 1 < len(lines):
        handle_message_arg(lines)
    # git commit
    elif "commit" in lines:
        handle_commit_no_arg(lines)
    else:
        process = subprocess.call(lines)