

# set global chunk options
# for figures
opts_chunk$set(fig.path='figs/', fig.align='center', fig.show='hold',
               dev='CairoPDF', out.width='.4\\linewidth')
# replacing "=" into "->" to make it R thing
options(replace.assign=TRUE,width=90)
# caching chunks
opts_chunk$set(cache.extra = R.version,cache.path='cache/')
opts_chunk$set(cache.extra = rand_seed)



# from different bible versions
ESV_sentiment <- read.delim('../data/ESV_sentimentAnalysis.txt', header=FALSE)
KJV_sentiment <- read.delim('../data/KJV_sentimentAnalysis.txt', header=FALSE)
NIV_sentiment <- read.delim('../data/NIV_sentimentAnalysis.txt', header=FALSE)



# construct plot for sentiment probabilities from these three versions
library(ggplot2)
p <- ggplot(ESV_sentiment, aes(x=V1, y=V2))+
     stat_smooth(aes(color="ESV"))+
     stat_smooth(data=KJV_sentiment, aes(color="KJV"))+
     stat_smooth(data=NIV_sentiment, aes(color="NIV"))+
     labs(color="Biblical Versions") + 
     xlab('Biblical Verses') + 
     ylab('Probability') + 
     opts(title='Sentiment on David and Goliath')
ggsave(filename='../img/sentimentPlot.png', plot = p)




# insert saved figure from above
library(knitr)
f='../img/sentimentPlot'



# merge three biblical versions based on their verses
ESV_KJV <- merge(ESV_sentiment, KJV_sentiment, by.x = "V1", by.y = "V1")
ESV_KJV_NIV <- merge(ESV_KJV, NIV_sentiment, by.x = "V1", by.y = "V1")

# label this dataframe
colnames(ESV_KJV_NIV) <- c("Verse", "ESV", "KJV", "NIV")
rownames(ESV_KJV_NIV) <- ESV_KJV_NIV[, 1]
ESV_KJV_NIV <- ESV_KJV_NIV[, 2:4]

# compute the correlation using spearman
cor_tab <- cor(ESV_KJV_NIV, method="spearman")

# create table for latex
library(xtable)
print(xtable(cor_tab,caption="Correlation among Three Versions"))



print(xtable(summary(ESV_KJV_NIV), caption="Stat Overview"))

MostPositive <- apply(ESV_KJV_NIV, 2, which.max)
MostNegative <- apply(ESV_KJV_NIV, 2, which.min)
MostSentiment <- cbind(MostPositive, MostNegative)
print(xtable(MostSentiment, caption="Most Sentimented Verses"))




sessionInfo()



library(knitr)
knit("sentimentPlot.Rnw" ) # compile to tex
purl("sentimentPlot.Rnw", documentation = 0) # extract R code only
knit2pdf("sentimentPlot.Rnw")


