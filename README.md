# Analyze the story about David vs Goliath 

### get the biblical verses about David and Goliath using getPassage.py (1 Sam 17)

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
./getPassage.py -v 'ESV' -s '1 Sam 17' > data/DavidGoliath_ESV.txt
./getPassage.py -v 'KJV' -s '1 Sam 17' > data/DavidGoliath_KJV.txt
```
