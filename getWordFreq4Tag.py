#! /usr/bin/env python
# -*- coding: utf-8 -*-

import tokenizeText 
import sys
import operator
from optparse import OptionParser

##################################
# Compute the frequency of words #
# according to a certain tag     #

def getFreq(text, label):
    # label for tags according to NLTK terms

    with open(text) as f:
        content = f.read()
    tagged = tokenizeText.tag(content)

    # select words by their tags in a list
    wordbytag = [word.lower() for (word, tag) in tagged if tag !=None and tag.startswith(label)]
    uniqueWord = set(wordbytag)

    # count the frequency and return in a list of tuples, i.e, (word, freq)
    freq = {}
    for word in uniqueWord:
        freq[word] = wordbytag.count(word)/float(len(wordbytag))
    sorted_freq = sorted(freq.iteritems(), key=operator.itemgetter(1), reverse=True)

    return sorted_freq

def parse_options():
    parser = OptionParser(
        usage="""
        Get the frequency of words according to a certain tag
        Usage: %prog [options]
        e.g:
        ./getWordFreq4Tag.py -t 'data/DavidGoliath_ESV.txt' -l 'RB' > adverb.txt
        # RB for adverb
        """
        )
    parser.add_option('-t', '--text', 
                  type = 'string', action = 'store',
                  help = 'path for the input text')
    parser.add_option('-l', '--label', 
                  type = 'string', action = 'store',         
                  help = 'tag')
    (options, args) = parser.parse_args()
    return options

def main():
    options = parse_options()
    try:
        wordfreq = getFreq(text = options.text, label = options.label)
        # write freq in wordle format, word:freq
        for (word, freq) in wordfreq:
            print('{0}:{1}'.format(word,freq))
    except Exception, e:
        print e
        sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    main()






