input <= read.csv("Customers.csv", header=TRUE)
attach(input)

input = na.omit(input)
model_max = glm(Spending~Income + Experience + Family + Age, family=binomial, data=input)
model_min = glm(Spending~1, family=binomial, data=input)

summary(model_max)