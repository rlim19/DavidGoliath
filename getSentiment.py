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
    print ('{0}\t{1}\t{2}'.format(text, mood, prob))

if __name__ == '__main__':
    ApiKey = "JnhIZpQkff7fc3AwqCB"
    data = open(sys.argv[1], 'r').read().rstrip().decode("utf-8")
    # taking care of encoding of quotes
    data = data.translate(dict.fromkeys([0x201c, 0x201d, 0x2018, 0x2019]))
    list_text = nltk.tokenize.sent_tokenize(data)
    for text in list_text:
        getSentiment(text, apikey= ApiKey)
