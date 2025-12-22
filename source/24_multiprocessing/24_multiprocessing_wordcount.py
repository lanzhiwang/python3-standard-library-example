#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
""" """
# end_pymotw_header
import multiprocessing
import string

from multiprocessing_mapreduce import SimpleMapReduce


def file_to_words(filename):
    """Read a file and return a sequence of
    (word, occurences) values.
    """
    STOP_WORDS = set(
        [
            "a",
            "an",
            "and",
            "are",
            "as",
            "be",
            "by",
            "for",
            "if",
            "in",
            "is",
            "it",
            "of",
            "or",
            "py",
            "rst",
            "that",
            "the",
            "to",
            "with",
        ]
    )
    TR = str.maketrans({p: " " for p in string.punctuation})

    print("{} reading {}".format(multiprocessing.current_process().name, filename))
    output = []

    with open(filename, "rt") as f:
        for line in f:
            # Skip comment lines.
            if line.lstrip().startswith(".."):
                continue
            line = line.translate(TR)  # Strip punctuation
            for word in line.split():
                word = word.lower()
                if word.isalpha() and word not in STOP_WORDS:
                    output.append((word, 1))
    return output


def count_words(item):
    """Convert the partitioned data for a word to a
    tuple containing the word and the number of occurences.
    """
    word, occurences = item
    return (word, sum(occurences))


if __name__ == "__main__":
    import operator
    import glob

    input_files = glob.glob("/python3-standard-library-example/*.rst")
    print("input_files:", input_files)

    mapper = SimpleMapReduce(file_to_words, count_words)
    word_counts = mapper(input_files)
    word_counts.sort(key=operator.itemgetter(1))
    word_counts.reverse()

    print("\nTOP 20 WORDS BY FREQUENCY\n")
    top20 = word_counts[:20]
    longest = max(len(word) for word, count in top20)
    for word, count in top20:
        print(
            "{word:<{len}}: {count:5}".format(len=longest + 1, word=word, count=count)
        )

"""
$ python 24_multiprocessing_wordcount.py
input_files: ['/python3-standard-library-example/README.rst']
ForkPoolWorker-1 reading /python3-standard-library-example/README.rst

TOP 20 WORDS BY FREQUENCY

http     :     8
pymotw   :     7
python   :     7
you      :     6
library  :     6
standard :     6
com      :     6
example  :     4
name     :     4
work     :     4
exec     :     3
find     :     3
black    :     3
code     :     3
this     :     3
license  :     3
under    :     3
org      :     3
rm       :     2
bash     :     2
$
"""
