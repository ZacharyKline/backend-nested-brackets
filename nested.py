#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Working code of the nested brackets assignment for Kenzie Academy Quarter 3
"""
__author__ = "ZacharyKline"

import sys

openers = ['[', '(', '{', '<', '(*']
closers = [']', ')', '}', '>', '*)']

def arg_function(args):
    """Goes through each character and checks it again a list of openers and closers."""
    # results = []
    stack = []
    unbalanced = False
    pos = 0
    while args:
        token = args[0]
        if args[:2] == '(*' or args[:2] == '*)':
            token = args[:2]
        pos += 1

        if token in closers:
            index = closers.index(token)
            match = openers[index]
            if stack.pop() != match:
                unbalanced = True
                break #unbalanced

        if token  in openers:
            stack.append(token)
        
        args = args[len(token):]



    if stack or unbalanced:
        return 'NO' + str(pos)
    return 'YES'


def main():
    with open('input.txt', 'r') as f:
        with open('output.txt', 'w') as o:
            for line in f:
                read_output = arg_function(line)   
                print(read_output)
                o.write(read_output + '\n')


if __name__ == '__main__':
    main()
