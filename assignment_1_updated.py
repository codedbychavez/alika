import pandas as pd
import numpy as np
import statistics
import matplotlib.pyplot as plt

print("COVID-19 Data Obtained for 20 listed Countries Retrieved from Monday May 10, 2021")
print("Data was obtained from Ministry of Health Dashboards from respective countries and was approved of use by Mr. Lelander Singh!")

headings = ['Country', 'Population', 'Total Cases', 'Deaths', 'Active Cases', 'Recoveries']
covid_data = pd.read_csv('covid_19_10th_may_data.csv',header=None,skiprows=0,names=headings)

print(covid_data)

print("----------------------------------------------------------------------------------------")

col_max1 = covid_data['Total Cases'].max(axis=0)
print("Highest number of cases in the specified countries at specified date = ", col_max1)

col_min1 = covid_data['Total Cases'].min(axis=0)
print("Lowest number of cases in the specified countries at specified date = ", col_min1)

col_max2 = covid_data['Deaths'].max(axis=0)
print("Highest number of deaths in the specified countries at specified date = ", col_max2)

col_min2 = covid_data['Deaths'].min(axis=0)
print("Lowest number of deaths in the specified countries at specified date = ", col_min2)

col_max3 = covid_data['Active Cases'].max(axis=0)
print("Highest number of active cases in the specified countries at specified date = ", col_max3)

col_min3 = covid_data['Active Cases'].min(axis=0)
print("Lowest number of active cases in the specified countries at specified date = ", col_min3)

col_max4 = covid_data['Recoveries'].max(axis=0)
print("Highest number of recoveries in the specified countries at specified date = ", col_max4)

col_min4 = covid_data['Recoveries'].min(axis=0)
print("Lowest number of recoveries in the specified countries at specified date = ", col_min4)

avg1 = statistics.mean(covid_data['Active Cases'])
print("Average amount of active cases on May 10 within specified countries = ", avg1)

avg2 = statistics.mean(covid_data['Deaths'])
print("Average deaths on May 10 within specified countries = ", avg2)



print()
print()
print()


#DATA FILTER

dx = pd.DataFrame({"Country": ['Anguilla','Antigua & Barbuda','Bahamas','Barbados', 'Belize', 'Bermuda', 'British Virgin Islands', 'Cayman Islands', 'Dominica', 'Grenada', 'Guyana', 'Haiti', 'Jamaica', 'Montserrat', 'St. Lucia', 'St Kitts & Nevis', 'St. Vincent & The Grenadines', 'Suriname','Trinidad & Tobago', 'Turks & Caicos Islands'], '  ' "Population": ['15003','97929','393244','287375','397628','62278','30231','65722','71986','112523','786552','11402528','2961167','4992','183627','53199','110940','586632','1399488','38717'], '  ' "Total Cases": ['99','1231','10733','3946','12700','2434','216','548','175','161','14442','13164','46708','20','4690','45','1922','11112','13454','2402'],'   ' "Deaths": ['0','32','212','45','323','30','1','2','0','1','327','263','806','1','75','0','12','215','215','17'], '   ' "Active Cases": ['49','35','840','4','63','17','3','9','0','0','80','63','39','0','154','0','169','1164','99','27'], '   ' "Recoveries": ['17','1170','9781','3861','12303','3095','191','537','175','158','12267','12154','22268','19','4521','44','1741','9778','9381','2358'], '   ' "Recoveries": ['17','1170','9781','3861','12303','3095','191','537','175','158','12267','12154','22268','19','4521','44','1741','9778','9381','2358']})
second_row = dx.loc[[0]]

#Variables: Data filter
first_row = "Anguilla"
second_row = "Antigua & Barbuda"
third_row = 'Bahamas'
fourth_row = 'Barbados'
fifth_row = 'Belize'
sixth_row = 'Bernuda'
seventh_row = 'British virgin islands'
eight_row = 'Cayman islands'
nineth_row = 'Dominica'
tenth_row = 'Grenada'
elev_row = 'Guyana'
twelv_row = 'Haiti'
thirth_row = 'Jamaica'
frteen_row = 'Montserrat'
fifteen_row = 'St. lucia'
sixteen_row = 'St. kitts & nevis'
seventeen_row = 'St. vincent & the grenadines'
eighteen_row = 'Suriname'
nineteen_row = 'Trinidad & tobago'
twenty_row = "Turks & Caicos Islands"


STcountry = str(input("Enter a CARICOM country to view their Covid-19 statistics: ").title())
print()

#Conditionals for data filter
if STcountry == first_row:
    first_row = dx.loc[[0]]
    print(first_row)

elif STcountry == second_row:
    second_row = dx.loc[[1]]
    print(second_row)

elif STcountry == third_row:
    third_row = dx.loc[[2]]
    print(third_row)

elif STcountry == fourth_row:
    fourth_row = dx.loc[[3]]
    print(fourth_row)

elif STcountry == fifth_row:
    fifth_row = dx.loc[[4]]
    print(fifth_row)

elif STcountry == sixth_row:
    sixth_row = dx.loc[[5]]
    print(sixth_row)

elif STcountry == seventh_row:
    seventh_row = dx.loc[[6]]
    print(seventh_row)

elif STcountry == eight_row:
    eight_row = dx.loc[[7]]
    print(eight_row)

elif STcountry == nineth_row:
    nineth_row = dx.loc[[8]]
    print(nineth_row)

elif STcountry == tenth_row:
    tenth_row = dx.loc[[9]]
    print(tenth_row)

elif STcountry == elev_row:
    elev_row = dx.loc[[10]]
    print(elev_row)

elif STcountry == twelv_row:
    twelv_row = dx.loc[[11]]
    print(twelv_row)

elif STcountry == thirth_row:
    thirth_row = dx.loc[[12]]
    print(thirth_row)

elif STcountry == frteen_row:
    frteen_row = dx.loc[[13]]
    print(frteen_row)

elif STcountry == fifteen_row:
    fifteen_row = dx.loc[[14]]
    print(fifteen_row)

elif STcountry == sixteen_row:
    sixteen_row = dx.loc[[15]]
    print(sixteen_row)

elif STcountry == seventeen_row:
    seventeen_row = dx.loc[[16]]
    print(seventeen_row)

elif STcountry == eighteen_row:
    eighteen_row = dx.loc[[17]]
    print(eighteen_row)

elif STcountry == nineteen_row:
    nineteen_row = dx.loc[[18]]
    print(nineteen_row)

else:
    twenty_row = dx.loc[[19]]
    print(twenty_row)



country = covid_data['Country']
act = covid_data['Active Cases']
tot = covid_data['Total Cases']
dth = covid_data['Deaths']
rec = covid_data['Recoveries']

#Line Graph 1-Total Cases May 10th 2021

plt.xticks(fontsize=10, rotation=90)
plt.xlabel('Country', fontsize=10)
plt.ylabel('Total Cases', fontsize=10)
plt.title("Line Graph Showing Total Cases up to May 10th 2021")

plt.scatter(country, tot)
plt.plot(country, tot, label="Total Cases")
plt.legend()
plt.grid() 

plt.show()

#Line Graph 2-Active Cases May 10th 2021

plt.xticks(fontsize=10, rotation=90)
plt.xlabel('Country', fontsize=10)
plt.ylabel('Active Cases', fontsize=10)
plt.title("Line Graph Showing Active Cases for May 10th 2021")

plt.scatter(country, act)
plt.plot(country, act, label="Active Cases")
plt.legend()
plt.grid()

plt.show()

#Line Graph 3-Deaths May 10th 2021

plt.xticks(fontsize=10, rotation=90)
plt.xlabel('Country', fontsize=10)
plt.ylabel('Number Total Deaths vs Active Cases', fontsize=10)
plt.title("Line Graph Showing Total Deaths up to May 10th 2021")

plt.scatter(country, dth)
plt.scatter(country, rec)
plt.plot(country, dth, label="Deaths")
plt.plot(country, rec, label="Recoveries")
plt.legend()
plt.grid()

plt.show()




 


