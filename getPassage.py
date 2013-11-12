#! /usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import sys
from pyquery import PyQuery
import scriptures
from optparse import OptionParser


def getPassage(scripture_inp, version='KJV'):
    
    # check if the scripture is valid
    scripture = scriptures.extract(scripture_inp)
    # [(book, startBook, startVerse, endBook, endVerse ]

    if scripture == []:
        print("Your input is invalid, check please")
    else:
        script_str = scriptures.reference_to_string(*scripture[0])
        url_open = urllib.quote(script_str.encode("utf-8"))
        url = "http://mobile.biblegateway.com/passage/?search="+url_open+\
              "&version="+version+"\&interface=print"
        passage_raw = PyQuery(url)
        passage = passage_raw(".passage").remove("h3").find('[class^="text"]').\
                  remove(".chapternum").\
                  remove(".crossrefs").remove(".footnote")
        passage = passage.text().encode("utf-8")
        return passage


def parse_options():
    parser = OptionParser(usage="""\
         Get passage from biblegateway.com
         Usage: %prog [options] 
         e.g: 
         ./getPassage.py -v 'ESV' -s 'John 3' > john3_ESV.txt
         """)
    parser.add_option('-v', '--version', 
                      type = 'string', action = 'store',
                      default = 'KJV',
                      help = 'Bible version')
    parser.add_option('-s', '--scripture', 
                      type = 'string', action = 'store',
                      help = 'Bible scripture')
    (options, args) = parser.parse_args()
    return options

def main():
    options = parse_options()
    try:
        passage = getPassage(version= options.version,
                             scripture_inp = options.scripture)
        print('1 ' + passage)
    except Exception, e:
        print e
        sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == "__main__":
    main()
