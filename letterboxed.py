#! /usr/bin/env python3
# -*- coding: UTF8 -*-

import argparse
import os
import re
import sys
import networkx as nx

from itertools import permutations
from pathlib import Path

def legal_words(me, letters, word_list):
    ''' "Illegal" regexes. If any match then the word is not usable.
         `tooshort` is less than 3 characters.
         `badletters` is any letter not on the puzzle board.
         `badsequence` means a repeated letter on the same side of the board.
        Eliminating `badletters` before `badsequence` keeps the sequence regex sane.
        'sides' = 'abcdefhijklm' -- a string of 3 letters * 4
    '''
    letters = letters.lower() # Using only lc eliminates many "illegal" words from /usr/.../dict.
    sides = [letters[i:i+3] for i in range(0, len(letters), 3)]
    tooshort = r'^.{1,2}$'
    badletters = '[^' + ''.join(set(''.join(sides))) + ']'
    badsequences = '|'.join(['[' + side + '](?=[' + side + '])' for side in sides])
    regex = re.compile('|'.join([tooshort, badletters, badsequences]))
    return [word for word in Path(word_list).read_text().split()
            if not regex.search(word)]

def find_graphs(me, letters, maxlength, words):
    ''' Create a graph of all combos of words where the last letter of the first
        is the first letter of the seconds, like "gamma" -> "alpha".
        I found the logic part online. Link?
    '''
    sletters = set(letters)
    letters_len = len(sletters)
    letters = ''.join(sorted(sletters))
    # Create a graph with all words that end/start with the same char tip to tail.
    G = nx.DiGraph()
    [G.add_edge(u,v) for u,v in permutations(words, 2) if u[-1] == v[0]]
    for u,v in permutations(G.nodes, 2):
        for path in nx.all_simple_paths(G, u, v, 3):
            if len(path) <= maxlength:
                if len(sletters - set(''.join(path))) == 0:
                    path_len = len(path)
                    char_len = len(''.join(path))
                    extra_chars = char_len - letters_len
                    print(f'{path_len}:{char_len}:{extra_chars} {"->".join(path)}')


if __name__ == "__main__":
    me = os.path.basename(sys.argv[0])
    p = argparse.ArgumentParser(
            description='Somebody do something.',
            epilog='Ouput:\n'
                '    Number of words in the path (shorter is "better").\n'
                '    Total number of characters in the path.\n'
                '    Number of repeated (extra) characters (smaller is "bettter").\n'
                '    Path as "word1->word2..."',
            formatter_class=argparse.RawDescriptionHelpFormatter,
        )
    p.add_argument('--verbose', action='store_true', help='Verbose')
    p.add_argument('--maxlength', type=int, default=3, help='Show chains at least this long.')
    p.add_argument('letters', help='Allowed letters as one list: "abcdefg.."')
    args = p.parse_args()
    word_list = '/usr/share/dict/words'
    good_words = legal_words(me, args.letters, word_list)
    find_graphs(me, args.letters, args.maxlength, good_words)
