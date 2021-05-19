## Install requirements
# Pandas
# Numpy
# Statistics
# Matplotlib


# Import Requirements
import pandas as pd
import numpy as np
import statistics
import matplotlib.pyplot as plt


# Instruction 1: Read selected data file and output its content

# Solution 1:

headings = ['Country', 'Population', 'Total Cases', 'Deaths', 'Active Cases', 'Recoveries']

covid_dataset = pd.read_csv('covid_19_10th_may_data.csv', header=None, skiprows=0, names=headings)

print(covid_dataset)


# Instruction 2:  Output statistical summaries of the data file. You will decide on what summaries are appropriate and useful

# Solution 1:

# Statistical summaries for the Total Cases, Deaths, Active Cases and Recoveries in the 20 countries

# Drop the Country and Population Column

removed_country_and_polulation_column = covid_dataset.drop(['Country', 'Population'], axis=1)

# Display Summaries
print(removed_country_and_polulation_column.sum())



# Instruction 3: Produce at least 2 graphs on some aspect of the dataset. You will decide what graphs/charts you will produce

# Solution 1:

# Displaying the Countries and Recoveries represented on a bar graph

covid_dataset.plot(x ='Country', y='Recoveries', kind = 'bar')
plt.show()



# Solution 1 - Part 2

# Displaying the Countries and Deaths represented on a pie chart of the first 5 countries in the dataset

# Resetting the index to use the Country Column

covid_dataset_with_reseted_index = covid_dataset.set_index('Country')

covid_dataset_with_reseted_index.head().plot.pie(y='Deaths',figsize=(15, 15),autopct='%1.0f%%', startangle=90)
plt.show()


# Instruction 4: 
# Perform and output results of comparative statistical analyses of the data of any 
# two aspects of data in the dataset e.g. if the dataset contains data by gender, months, years etc.
# comparisons can be done among those.


# Solution 1:

# Part 1

# Comparing the Deaths in Barbados to the deaths in Guyana

# Define variables

barbados_record = covid_dataset[covid_dataset['Country'] == 'Barbados']
guyana_record = covid_dataset[covid_dataset['Country'] == 'Guyana']



barbados_deaths = int(barbados_record['Deaths'].to_string(index=False))
guyana_deaths = int(guyana_record['Deaths'].to_string(index=False))

print('The total number of deaths in Barbados is {0} Compared to Guyana which is: {1}'.format(barbados_deaths, guyana_deaths))


# Part 2

# Comparing the recoveries in Barbados to the recoveries in Guyana

# Define variables

barbados_record = covid_dataset[covid_dataset['Country'] == 'Barbados']
guyana_record = covid_dataset[covid_dataset['Country'] == 'Guyana']



barbados_deaths = int(barbados_record['Recoveries'].to_string(index=False))
guyana_deaths = int(guyana_record['Recoveries'].to_string(index=False))

print('The total number of recoveries in Barbados is {0} Compared to Guyana which is: {1}'.format(barbados_deaths, guyana_deaths))



# Instruction 5: Perform Any ONE other creative analysis of some aspect of the data in the dataset.

# Lets extract the country with the higest number of deaths from the dataset

country_with_highest_deaths = covid_dataset[covid_dataset['Deaths'] == covid_dataset['Deaths'].max()]
country_with_lowest_deaths = covid_dataset[covid_dataset['Recoveries'] == covid_dataset['Recoveries'].min()]

print('The country with the higest number of deaths is:')
print(country_with_highest_deaths)

print('The country with the lowest number of deaths is:')
print(country_with_lowest_deaths)





