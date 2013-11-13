# Analyzed the story about David vs Goliath 

- Obtained the biblical verses about David and Goliath using getPassage.py (1 Sam 17)

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

- Obtained the summary
  - Summary based on the verses not sentences.

```
# Use meanAverageScore and ESV bible verses.
./getSummary.py data/DavidGoliath_ESV.txt > data/DavidGoliath_summaryESV.txt
```

- Sentiment analysis
  - Sentiment analysis per verse

```
./getSentiment.py data/DavidGoliath_ESV.txt > data/DavidGoliath_sentimentAnalysis_ESV.txt
./getSentiment.py data/DavidGoliath_NIV.txt > data/DavidGoliath_sentimentAnalysis_NIV.txt
./getSentiment.py data/DavidGoliath_KJV.txt > data/DavidGoliath_sentimentAnalysis_KJV.txt
```

  - Processed sentiment analysis 
```
# Incorporated negative into minus probability and the opposite as well.
# Parsed only no or biblical verses and their probability values. 
awk -F 't' 'BEGIN { OFS="t" } {if($3=="negative") print $1"\t""-"$4; else print $1"\t"$4}' DavidGoliath_sentimentAnalysis_ESV.txt > ESV_sentimentAnalysis.txt
awk -F 't' 'BEGIN { OFS="t" } {if($3=="negative") print $1"\t""-"$4; else print $1"\t"$4}' DavidGoliath_sentimentAnalysis_KJV.txt > KJV_sentimentAnalysis.txt
awk -F 't' 'BEGIN { OFS="t" } {if($3=="negative") print $1"\t""-"$4; else print $1"\t"$4}' DavidGoliath_sentimentAnalysis_NIV.txt > NIV_sentimentAnalysis.txt
```

