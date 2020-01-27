# Fraud Detection Delta Hacks 2020: Project Apati
## Inspiration 
Fraud is a crime that can impact any Canadian, regardless of their education, age or income. 
From January 2014 to December 2017, Canadians lost more than $405 million to fraudsters. ~ [Statistic Info](https://www.competitionbureau.gc.ca/eic/site/cb-bc.nsf/eng/04334.html)

We wanted to develop technology that detects potentially fraudulent activity and give account owners the ability to cancel such transactions. 

## How it works
Using scikit-learn, we were able to detect patterns in a user's previous banking data provided by TD's davinci API. 
We examined categories such as the location of the purchase, the cost of the purchase, and the purchase category. Afterwards, we determined certain parameters for the cost of purchase based on the purchase category, and purchase locations to validate transactions that met the requirements. Transactions that were made outside of these parameters were deemed suspicious activity and an alert is sent to the account owner, providing them with the ability to validate/decline the purchase. If the transaction is approved, it is added to the MongoDB database with the rest of the user's previous transactions.

## Challenges we ran into
Initially, we tried to use Tensorflow for our ML model to analyze the user's previous banking history to find patterns and make the parameters. However, we were having difficulty correctly implementing it and there were mistakes being made in the model. This is why we decided to switch to scikit-learn, which our team had success using and our ML model turned out as we had expected.

## Accomplishments that we are proud of
Learning to use and implement Machine Learning with such a large data set that we were provided with. Training the model to detect suspicious activity was finally achieved after several attempts.

## What we learned
Handling large data files.
Pattern detection/Data Analysis.
Data Interpretation and Model development.

## What's next for Project Apati
Improving the model by looking at other categories in the data to refine the model based on other transactions statistics. Providing more user's data to improve the training and testing data-set for the model.

## TD's da-vinci API + Data sets
[TD davinci API](https://td-davinci.com/)

## Presentation Link
[Presentation Slide Show](https://slides.com/malharshah/deck#/projectapati)

## Devpost Link
[Devpost](https://devpost.com/software/frauddetectiondeltahacks2020)
