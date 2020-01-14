rm(data)
#뉴스만 분석

library(ggplot2)
library(dplyr)
library(rJava)
library(memoise)
library(KoNLP)
library(stringr)
library(data.table)
#data <- fread("c:/crawl/news1.csv",header = F,encoding = "UTF-8")#UTF-8
#data <- read.csv("c:/crawl/news1.csv",header = F)
data <- fread("c:/crawl/news1.csv",header = F)
#read.csv원하는 값 이상하게 들어옴
data
head(data)

txt <- str_replace_all(data$V3,"//w","")#특수문자 제거
#txt1 <- str_replace_all(data$V3,"\\w","")#특수문자 제거->오류
txt
str(txt)

nouns <- extractNoun(txt)
nouns

wordCount <- table(unlist(nouns))
wordCount

df_word <- as.data.frame(wordCount,stringsAsFactors = F)
df_word  <- rename(df_word,word = Var1,freq =Freq)
df_word <- filter(df_word,nchar(word)>= 2)
top_20 <- df_word %>% 
    arrange(desc(freq)) %>% 
    head(20)
top_20

library(wordcloud)
library(RColorBrewer)

pal <- brewer.pal(8,"Dark2")
#pal <- brewer.pal(9,"Blues")[5:9]
#
set.seed(1201)
wordcloud(words= df_word$word, 
          freq = df_word$freq,
          min.freq = 2,
          max.words = 200,
          random.order = F,
          rot.per = .1,
          scale = c(4,0.3),
          colors = pal)
#set.seed(1202)
#set.seed(Sys.time())

wordcloud(words= df_word$word, 
          freq = df_word$freq,
          min.freq = 2,
          max.words = 200,
          random.order = F,
          rot.per = .1,
          scale = c(4,0.3),
          colors = pal)

top_20$word
data_y <- top_20$freq
names(data_y) <- top_20$word
barplot(data_y,main="word",ylab="frequency")

ggplot(data = top_20,aes(x= word,y = freq,fill=word))+geom_bar(stat = 'identity')
