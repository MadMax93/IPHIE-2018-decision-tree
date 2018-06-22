df <- read.csv(file="./IPHIE-2018-decision-tree/dataset_diabetes/dataset_diabetes/diabetic_data.csv", header=TRUE, sep=",")

head(df)

library(party)
library(rpart)
library(rpart.plot)
library(readr)
library(dplyr)
set.seed(100)

df$readmitted = factor(df$readmitted)

rtree_fit <- rpart(readmitted ~ ., data = df) 

rpart.plot(rtree_fit)
