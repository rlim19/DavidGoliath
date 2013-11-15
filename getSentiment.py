#! /usr/bin/env python
# -*- coding: utf-8 -*-

##################################################
# Sentiment analysis for each sentence of a text #
##################################################

import urllib
import urllib2
from xml.dom import minidom
import nltk
import sys
import re

def getSentiment(text, apikey):
    """
    use the viralheat service to get the sentiment for a text sentence
    """
    url_text = urllib.quote(text.encode("utf-8"))
    url = "https://www.viralheat.com/api/sentiment/review.xml?api_key="\
            + apikey + "&text=" + url_text
    usock = urllib2.urlopen(url)

    # parse xml
    xmldoc = minidom.parse(usock)
    mood = xmldoc.getElementsByTagName('mood')[0].firstChild.nodeValue
    prob = xmldoc.getElementsByTagName('prob')[0].firstChild.nodeValue
    #print ('{0}\t{1}\t{2}'.format(text, mood, prob))
    return text, mood, prob

if __name__ == '__main__':
    ApiKey = sys.argv[2]
    data = open(sys.argv[1], 'r').read().rstrip().decode("utf-8")
    # taking care of encoding of quotes
    data = data.translate(dict.fromkeys([0x201c, 0x201d, 0x2018, 0x2019]))
    ls_verse = re.findall("[^0-9]+", data)
    ls_verse = [i.strip().lower() for i in ls_verse]
    no = 1 
    for text in ls_verse:
        (text, mood, prob) = getSentiment(text, apikey= ApiKey)
        print ('{0}\t{1}\t{2}\t{3}'.format(no, text, mood, prob))
        no += 1
