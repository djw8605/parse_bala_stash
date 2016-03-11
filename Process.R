
data = read.csv("~/tmp/stuff.csv")

library(ggplot2)
library(scales)

data$difference <- data$difference * 15

data$percent <- data$difference / sum(data$difference)

m <- ggplot(data, aes(x=difference)) +
  geom_bar(aes(y = (..count..)/sum(..count..), fill= (..count..)/sum(..count..)), binwidth=15) +
  scale_fill_gradient("Frequency", low = "green", high = "red") +
  ylab("Frequency") +
  xlab("Delay in minutes") +
  scale_y_continuous(labels=percent)
  
m

m <- ggplot(data, aes(x=difference)) + stat_ecdf()+
  ylab("Distribution") +
  xlab("Delay in minutes") +
  scale_y_continuous(labels=percent) +
  theme_bw()
m
  #scale_y_continuous(labels=percent)
#m + geom_histogram(aes(fill = ..count..), binwidth = 15) + 
#  scale_fill_gradient("Count", low = "green", high = "red")

