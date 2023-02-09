## Data set link
## https://www.kaggle.com/datasets/datascientistanna/customers-dataset

input = read.csv("Customers.csv", header=TRUE)
attach(input)

input = na.omit(input)

## Mapping the data
input$Gender_mapped <- ifelse(input$Gender == "Male", 0, 1)
input$Profession <- with(input, match(Profession, unique(Profession)))

model_max = glm(Spending~Income + Experience + Family + Age + Gender_mapped + Profession, family=gaussian, data=input)
model_min = glm(Spending~1, family=gaussian, data=input)

summary(model_max)

library(MASS)

print("STEP A")
step_a = stepAIC(model_max)

print("STEP F")
step_f = step(model_min, list(upper=model_max), direction="forward")

print("STEP B")
step_b = step(model_max, direction="backward")