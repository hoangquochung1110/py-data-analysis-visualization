# year-of-potential-life-lost
## Description

In this repo, we'll find the correlation between years of potential life lost (YPLL) and some additional measures, such as age, gender, income or HIV rate. 

#### Years of potential life lost (YPLL)
YPLL is an early mortality measure. It measures, across 10.000 people, total number of years below the age of 75 a 10.000-people group loses. For example, if a person dies at 73, he contributes 2 years to this sum, while another guy dies at 78, he contributes 0 years to the sum.
The file **ypll.csv** contains per-county YPLLs for the U.S. in 2011 

#### The additional measures
It can be found in **addtional_measures_cleaned.csv**, including all sorts of measures ranging from % of population below the age of 18 or median household income to % of population with diabetes.

## Data cleaning
A few notes on data cleaning  
1. Delete the top row because it is metaheader 
2. In ypll.csv, only consider rows whose 'Unreliable' comlumn unchecked and 'YPLL Rate' column not blank. 
3. In addtional_measures_cleaned.csv, some of rows don't contain value for some of the additional measures, for example, Broomfield, Colorado doesn't specify the percentage of illiterate child to the total population. These rows should be filter.
In addtional, there is a row per state that summaries  the state's statistics. It has an empty value for 'county' column and should be also filtered as we'll do county-by-county analysis.

The script named 
