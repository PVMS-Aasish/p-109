import pandas as pd
import statistics
import csv

df=pd.read_csv('StudentsPerformance.csv')
race_list=df['race/ethnicity'].to_list()

race_mean=statistics.mean(race_list)
print(race_mean) 

race_median=statistics.median(race_list)
print('race_median: '+str (race_median) )

race_mode=statistics.mode(race_list)
print('race_mode'+str (race_mode))

print("mean , median and mode of race is {},{} and {} respectively".format(race_mean,race_median,race_mode))

math_list=df['math score'].to_list()

math_mean=statistics.mean(math_list)
print(math_mean) 

math_median=statistics.median(math_list)
print('math_median: '+str (math_median) )

math_mode=statistics.mode(math_list)
print('math_mode'+str (math_mode))

print("mean , median and mode of math is {},{} and {} respectively".format(math_mean,math_median,math_mode))

race_std_deviation=statistics.stdev(race_list)
print(race_std_deviation)

math_std_deviation=statistics.stdev(math_list)
print(" math stdev :- "+str(math_std_deviation))

race_first_std_dev_start,race_first_std_dev_end=race_mean-race_std_deviation,race_mean+race_std_deviation
race_list_of_data_within_first_std_dev=[result for result in race_list if result>race_first_std_dev_start and result<race_first_std_dev_end]
print("{}% of data for  lies within race stddev".format(len(race_list_of_data_within_first_std_dev)*100.0/len(race_list)))

race_second_std_dev_start,race_second_std_dev_end=race_mean-(2*race_std_deviation),race_mean+(2*race_std_deviation)
race_list_of_data_within_second_std_dev=[result for result in race_list if result>race_second_std_dev_start and result<race_second_std_dev_end]
print("{}% of data for race lies within second stddev ".format(len(race_list_of_data_within_second_std_dev)*100/len(race_list)))

race_third_std_dev_start,race_third_std_dev_end=race_mean-(3*race_std_deviation),race_mean+(3*race_std_deviation)
race_list_of_data_within_third_std_dev=[result for result in race_list if result>race_third_std_dev_start and result<race_third_std_dev_end ]
print("{}% of data for race lies within third stddev ".format(len(race_list_of_data_within_third_std_dev)*100/len(race_list))) 

math_first_std_dev_start,math_first_std_dev_end=math_mean-math_std_deviation,math_mean+math_std_deviation
math_list_of_data_within_first_std_dev=[result for result in math_list if result>math_first_std_dev_start and result<math_first_std_dev_end]
print("{}% of data for math lies within first stddev".format(len(math_list_of_data_within_first_std_dev)*100.0/len(math_list)))

math_second_std_dev_start,math_second_std_dev_end=math_mean-(2*math_std_deviation),math_mean+(2*math_std_deviation)
math_list_of_data_within_second_std_dev=[result for result in math_list if result>math_second_std_dev_start and result<math_second_std_dev_end]
print("{}% of data for math lies within second stddev ".format(len(math_list_of_data_within_second_std_dev)*100/len(math_list)))

math_third_std_dev_start,math_third_std_dev_end=math_mean-(3*math_std_deviation),math_mean+(3*math_std_deviation)
math_list_of_data_within_third_std_dev=[result for result in math_list if result>math_third_std_dev_start and result<math_third_std_dev_end ]
print("{}% of data for math lies within third stddev ".format(len(math_list_of_data_within_third_std_dev)*100/len(math_list))) 