# Analyze the story about David vs Goliath 

1. Get the biblical verses about David and Goliath using getPassage.py (1 Sam 17)

```
Usage:          Get passage from biblegateway.com
         Usage: getPassage.py [options] 
         e.g: 
         ./getPassage.py -v 'ESV' -s 'John 3' > john3_ESV.txt
         

Options:
  -h, --help            show this help message and exit
  -v VERSION, --version=VERSION
                        Bible version
  -s SCRIPTURE, --scripture=SCRIPTURE
                        Bible scripture
```

```
# Biblical verses from ESV, KJV, and NIV.
./getPassage.py -v 'ESV' -s '1 Sam 17' > data/DavidGoliath_ESV.txt
./getPassage.py -v 'KJV' -s '1 Sam 17' > data/DavidGoliath_KJV.txt
./getPassage.py -v 'NIV' -s '1 Sam 17' > data/DavidGoliath_NIV.txt
```

2. Get the summary

```
# Use meanAverageScore and ESV bible verses.
./getSummary.py data/DavidGoliath_ESV.txt > data/DavidGoliath_summaryESV.txt
```

