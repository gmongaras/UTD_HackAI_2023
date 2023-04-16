# Imports
library(tidyverse)
library(ggplot2)
library(viridis)
df <- read_csv("data/summary.csv")

# Age Barplot
colnames(df)[colnames(df) == "...1"] = "Category"
df$Category = c("AgeBase", "16 - 25", "26 - 39", "40 - 64", "65+", "Age5")
ggplot(data = subset(df, !is.na(Age_Claim_Probability)), aes(x = fct_inorder(Category), y = Age_Claim_Probability, fill = Age_Claim_Probability)) + 
  ylim(0, 1) + geom_bar(stat = "identity") + scale_fill_viridis_c(trans = "log10", end = 0.6, option = 'magma') +
  labs(x = "Age")

# Income Barplot
df$Category = c("IncomeBase", "Poverty", "Working Class", "Middle Class", "Upper Class", "Income5")
ggplot(data = subset(df, !is.na(Income_Claim_Probability)), aes(x = fct_inorder(Category), y = Income_Claim_Probability, fill = Income_Claim_Probability)) + 
  ylim(0, 1) + geom_bar(stat = "identity") + scale_fill_viridis_c(trans = "log10", end = 0.6, option = 'magma') +
  labs(x = "Income_Class")

# Gender Barplot
df$Category = c("GenderBase", "Female", "Male", "Gender3", "Gender4", "Gender5")
ggplot(data = subset(df, !is.na(Gender_Claim_Probability)), aes(x = fct_inorder(Category), y = Gender_Claim_Probability, fill = Gender_Claim_Probability)) + 
  ylim(0, 1) + geom_bar(stat = "identity") + scale_fill_viridis_c(trans = "log10", end = 0.6, option = 'magma') +
  labs(x = "Gender")

# Married Barplot
df$Category = c("MarriedBase", "Not Married", "Married", "Married3", "Married4", "Married5")
ggplot(data = subset(df, !is.na(Married_Claim_Probability)), aes(x = fct_inorder(Category), y = Married_Claim_Probability, fill = Married_Claim_Probability)) + 
  ylim(0, 1) + geom_bar(stat = "identity") + scale_fill_viridis_c(trans = "log10", end = 0.6, option = 'magma') +
  labs(x = "Marrital Status")

# Education Barplot
df$Category = c("EducationBase", "No Education", "High School", "Bachelors", "Masters", "PHD")
ggplot(data = subset(df, !is.na(Education_Claim_Probability)), aes(x = fct_inorder(Category), y = Education_Claim_Probability, fill = Education_Claim_Probability)) + 
  ylim(0, 1) + geom_bar(stat = "identity") + scale_fill_viridis_c(trans = "log10", end = 0.6, option = 'magma') +
  labs(x = "Education Level")

# Past Accidents Barplot
df$Category = c("AccidentsBase", "Median", "Third Quartile", "Point: 7/15", "Maximum", "Accidents5")
ggplot(data = subset(df, !is.na(PastAccidents_Claim_Probability)), aes(x = fct_inorder(Category), y = PastAccidents_Claim_Probability, fill = PastAccidents_Claim_Probability)) + 
  ylim(0, 1) + geom_bar(stat = "identity") + scale_fill_viridis_c(trans = "log10", end = 0.6, option = 'magma') +
  labs(x = "Past Accidents")

# Has Children Barplot
df$Category = c("ChildrenBase", "No Children", "Has Children", "Children3", "Children4", "Children5")
ggplot(data = subset(df, !is.na(HasChildren_Claim_Probability)), aes(x = fct_inorder(Category), y = HasChildren_Claim_Probability, fill = HasChildren_Claim_Probability)) + 
  ylim(0, 1) + geom_bar(stat = "identity") + scale_fill_viridis_c(trans = "log10", end = 0.6, option = 'magma') +
  labs(x = "Has Children")

# Has Sports Car Barplot
df$Category = c("SportsCarBase", "No Sports Car", "Has Sports Car", "SportsCar3", "SportsCar4", "SportsCar5")
ggplot(data = subset(df, !is.na(HasSportsCar_Claim_Probability)), aes(x = fct_inorder(Category), y = HasSportsCar_Claim_Probability, fill = HasSportsCar_Claim_Probability)) + 
  ylim(0, 1) + geom_bar(stat = "identity") + scale_fill_viridis_c(trans = "log10", end = 0.6, option = 'magma') +
  labs(x = "Has Sports Car")

# Vehicle Year Barplot
df$Category = c("VehicleYearBase", "Before 2015", "After 2015", "VehicleYear3", "VehicleYear4", "VehicleYear5")
ggplot(data = subset(df, !is.na(VehicleYear_Claim_Probability)), aes(x = fct_inorder(Category), y = VehicleYear_Claim_Probability, fill = VehicleYear_Claim_Probability)) + 
  ylim(0, 1) + geom_bar(stat = "identity") + scale_fill_viridis_c(trans = "log10", end = 0.6, option = 'magma') +
  labs(x = "Car Model Year")
