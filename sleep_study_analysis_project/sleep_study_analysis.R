getwd()
data = read.csv("Sleep_health_and_lifestyle_dataset.csv")

library(plotly)
library(tidyverse)
library(sampling)

#Adjusted BMI Category labeling for consistency. I would consider Normal Weight and Normal to be the same
data = data %>% mutate(BMI.Category = str_replace(BMI.Category, "Normal Weight", "Normal"))
#Created a new column to signify if a sleep disorder exists, rather than the specific disorder
data = data %>% mutate(Disorder.Exists = if_else(Sleep.Disorder != "None", "Yes", "No"))

glimpse(as_tibble(data))

#Frequency of gender in data
genders = as.data.frame(table(data$Gender)); genders
gender_chart = plot_ly(genders, labels = ~Var1, values = ~Freq, type = "pie")
gender_chart %>% layout(title = "Proportion of Males and Females in Dataset")

#Frequency of occupation in data
occupation = as.data.frame(table(data$Occupation)); occupation
occ_chart = plot_ly(occupation, x = ~Var1, y = ~Freq, type = "bar")
occ_chart %>% layout(title = "Frequencies of Occupation in Dataset",
                     xaxis= list(title = "Occupation"))

#Distribution of ages in data
f = fivenum(data$Age)
names(f) = c("Min", "Q1", "Median","Q3", "Max"); f
paste("The number of people younger than the median age:", sum(data$Age < f[3]))
paste("The number of people older than the median age:", sum(data$Age > f[3]))
age_chart = plot_ly(x = data$Age, type = "box")
age_chart %>% layout(title = "Distribution of Ages",
                     xaxis = list(title = "Age"))

#Comparison of BMI Category and Sleep Disorder
sleep_vs_BMI = table(data$Sleep.Disorder, data$BMI.Category); sleep_vs_BMI

df = as.data.frame(sleep_vs_BMI)
chart = plot_ly(df, x = ~Var1, y = ~Freq, color = ~Var2, type = "bar")
chart %>% layout(title = "Comparison of People with Sleep Disorders Grouped by BMI Category",
                 yaxis = list(title = "Number of People"), 
                 xaxis = list(title = "Sleep Disorder"),
                 barmode = "stack")

disorder_vs_BMI = table(data$Disorder.Exists, data$BMI.Category)
df2 = as.data.frame(disorder_vs_BMI)
chart = plot_ly(df2, x = ~Var1, y = ~Freq, color = ~Var2, type = "bar")
chart %>% layout(title = "Comparison of People with Sleep Disorders Grouped by BMI Category",
                 yaxis = list(title = "Number of People"), 
                 xaxis = list(title = "Sleep Disorder Exists"),
                 barmode = "stack")

bmi_and_dis_avgsleep = data |>
  group_by(data$Disorder.Exists, data$BMI.Category) |>
  summarise(avgsleep = mean(Sleep.Duration)); bmi_and_dis_avgsleep

#Comparison of Sleep Duration, Physical Activity and Gender

data |> group_by(data$Gender) |> summarize(avg_sleep = mean(Sleep.Duration))

age_vs_sleep = plot_ly(data = data, 
                       x = ~data$Physical.Activity.Level, 
                       y = ~data$Sleep.Duration, 
                       color = ~data$Gender,
                       colors = c("#7769f3", "#54bf49"),
                       type = "scatter",
                       mode = "markers")
age_vs_sleep %>% layout(title = "Comparison of Physical Activity Level and Sleep Duration",
                        xaxis = list(title = "Physical Activity Level"),
                        yaxis = list(title = "Sleep Duration"),
                        legend = list(title = list(text = "Gender")))

age_vs_sleep2 = plot_ly(data = data, 
                        x = ~data$Physical.Activity.Level, 
                        y = ~data$Sleep.Duration, 
                        color = ~data$Occupation,
                        type = "scatter",
                        mode = "markers")
age_vs_sleep2 %>% layout(title = "Comparison of Physical Activity Level and Sleep Duration",
                         xaxis = list(title = "Physical Activity Level"),
                         yaxis = list(title = "Sleep Duration"),
                         legend = list(title = list(text = "Occupation")))

# Distribution of physical activity level
activity_dist = plot_ly(x = ~data$Physical.Activity.Level, 
                        type = "histogram", 
                        xbins = list(size = 15))
activity_dist %>% layout(title = "Distribution of Physical Activity Level",
                         xaxis = list(title = "Minutes of Activity", range = c(20,110)),
                         yaxis = list(title = "Frequency", range = c(0,90)))

lvl = fivenum(data$Physical.Activity.Level)
names(lvl) = c("Min", "Q1", "Median","Q3", "Max"); lvl
activity_box_chart = plot_ly(x = data$Physical.Activity.Level, type = "box")
activity_box_chart %>% layout(title = "Distribution of Physical Activity Level",
                              xaxis = list(title = "Minutes of Activity"))

# Applicability of Central Limit Theorem on Sleep Duration

table(data$Sleep.Duration)
paste("The mean of the population is", round(mean(data$Sleep.Duration),3))
paste("The standard deviation of the population is", round(sd(data$Sleep.Duration),3))
sleep_dur = plot_ly(x = ~data$Sleep.Duration, 
                    type = "histogram", 
                    histnorm = "probability",
                    xbins = list(size = .3))
sleep_dur %>% layout(title = "Distribution of Sleep Duration",
                     xaxis = list(title = "Hours of Sleep", range = c(5.5,9)),
                     yaxis = list(title = "Frequency", range = c(0,.3)))
set.seed(5919)
num_samples = 1000
size1 = 25
size2 = 50
size3 = 75

xmean1 = numeric(num_samples)
for (i in 1:num_samples) {
  xmean1[i] <- mean(sample(data$Sleep.Duration, size1, replace = FALSE))
}

plot1 = plot_ly(x = xmean1, type = "histogram", histnorm = "probability")
plot1 %>% layout(title = "Sleep Duration Sample of 1000 of Size 25",
                 xaxis = list(title = "Hours of Sleep", range = c(5.5, 9)),
                 yaxis = list(title = "Frequency", range = c(0,.15)))

xmean2 = numeric(num_samples)
for (i in 1:num_samples) {
  xmean2[i] <- mean(sample(data$Sleep.Duration, size2, replace = FALSE))
}

plot2 = plot_ly(x = xmean2, type = "histogram", histnorm = "probability")
plot2 %>% layout(title = "Sleep Duration Sample of 1000 of Size 50",
                 xaxis = list(title = "Hours of Sleep", range = c(5.5, 9)),
                 yaxis = list(title = "Frequency", range = c(0,.15)))

xmean3 = numeric(num_samples)
for (i in 1:num_samples) {
  xmean3[i] <- mean(sample(data$Sleep.Duration, size3, replace = FALSE))
}

plot3 = plot_ly(x = xmean3, type = "histogram", histnorm = "probability")
plot3 %>% layout(title = "Sleep Duration Sample of 1000 of Size 75",
                 xaxis = list(title = "Hours of Sleep", range = c(5.5, 9)),
                 yaxis = list(title = "Frequency", range = c(0,.15)))

# Comparison of Sampling Methods and Effect on Mean Sleep Duration

N = nrow(data)
paste("The mean of the population is", round(mean(data$Sleep.Duration),3))

#Simple random sampling
set.seed(5919)
n = 50
a = srswr(n, N)
rows1 = (1:N)[a!=0]
simple_random = data[a != 0,]
table(simple_random$Sleep.Duration)

paste("The mean using simple random sampling is", round(mean(simple_random$Sleep.Duration),3))

#Systematic sampling
k = floor(N / n)
paste("Sample size of:", k)
set.seed(5919)
b = sample(k,1)
paste("First person selected in first group: ", b)
print("All subsequent rows selected:")
rows2 = seq(b, by = k, length = n); rows2
systematic = data[seq(b, by = k, length = n),]
table(systematic$Sleep.Duration)
paste("The mean using systematic sampling is", round(mean(systematic$Sleep.Duration),3))

#Stratified by gender
mod_data = data.frame(Gender = data$Gender, Sleep = data$Sleep.Duration)
set.seed(5919)
print("Frequencies of gender in data:")
gender_freq = table(mod_data$Gender); gender_freq
print("Strata Sizes:")
strata_sizes = round(n * gender_freq / sum(gender_freq)); strata_sizes
stratified = sampling::strata(mod_data,
                              stratanames = c("Gender"),
                              size = strata_sizes, 
                              method = "srswor", 
                              description = TRUE)
strat_data = sampling::getdata(mod_data, stratified); strat_data
paste("The mean using stratified sampling by gender is", round(mean(strat_data$Sleep),3))

#Stratified by sleep disorder
mod_data2 = data.frame(Disorder = data$Disorder.Exists, Sleep = data$Sleep.Duration)
set.seed(5919)
print("Frequencies of sleep disorder existing in data:")
disorder_freq = table(mod_data2$Disorder); disorder_freq
print("Strata Sizes:")
strata_sizes2 = round(n * disorder_freq / sum(disorder_freq)); strata_sizes2
stratified2 = sampling::strata(mod_data2,
                               stratanames = c("Disorder"),
                               size = strata_sizes2, 
                               method = "srswor", 
                               description = TRUE)
strat_data2 = sampling::getdata(mod_data2, stratified2); strat_data2
paste("The mean using stratified sampling by sleep disorder is", round(mean(strat_data2$Sleep),3))

#Comparing the means
mean_comp = c(mean(data$Sleep.Duration), 
              mean(simple_random$Sleep.Duration), 
              mean(systematic$Sleep.Duration), 
              mean(strat_data$Sleep),
              mean(strat_data2$Sleep))
names(mean_comp) = c("Population", "SimpleRandom", "Systematic", "Strata_Gender", "Strata_Disorder")
mean_comp
