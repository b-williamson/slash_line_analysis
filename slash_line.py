import numpy as np
from numpy import random as rndm
import csv
from matplotlib import pyplot as plt

#lists made from the csv that will help make arrays
average_list = []
obp_list = []
slugging_list = []

#pulling data from the csv
with open("slash_lines.csv", encoding="UTF-8", newline="") as stats_file:
  average = csv.DictReader(stats_file)
  for average_row in average:
    average_list.append(average_row["AVG"])
    
with open("slash_lines.csv", encoding="UTF-8", newline="") as stats_file:
  obp = csv.DictReader(stats_file)
  for obp_row in obp:
    obp_list.append(obp_row["OBP"])
    
with open("slash_lines.csv", encoding="UTF-8", newline="") as stats_file:
  slugging = csv.DictReader(stats_file)
  for slugging_row in slugging:
    slugging_list.append(slugging_row["SLG"])
    
#creating arrays from the lists gathered from the csv
average_array = np.array(average_list).astype(np.float)
obp_array = np.array(obp_list).astype(np.float)
slugging_array = np.array(slugging_list).astype(np.float)

#calculating means and standard deviations to help create random normal distributions to compare with the real stats
average_mean = np.mean(average_array)
average_std = np.std(average_array)
obp_mean = np.mean(obp_array)
obp_std = np.std(obp_array)
slugging_mean = np.mean(slugging_array)
slugging_std = np.std(slugging_array)

#random normal distributions of the three metrics' values
average_rn = np.random.normal(average_mean, average_std, 10000)
obp_rn = np.random.normal(obp_mean, obp_std, 10000)
slugging_rn = np.random.normal(slugging_mean, slugging_std, 10000)

#plotting the histograms
plt.figure()
plt.subplot(3, 2, 1)
plt.hist(average_array, 20, color = "purple")
plt.xlabel('Average')
plt.ylabel('Number of Players')
plt.title('2021 Average Distribution')
plt.subplots_adjust(wspace=0.4, hspace=1)

plt.subplot(3, 2, 2)
plt.hist(average_rn, 20, color = "purple")
plt.xlabel('Average')
plt.ylabel('Number of Players')
plt.title('Random Sample Distribution')
plt.subplots_adjust(wspace=0.4, hspace=1)

plt.subplot(3, 2, 3)
plt.hist(obp_array, 20, color = "green")
plt.xlabel('On-Base Percentage')
plt.ylabel('Number of Players')
plt.title('2021 On-Base Distribution')
plt.subplots_adjust(wspace=0.4, hspace=1)

plt.subplot(3, 2, 4)
plt.hist(obp_rn, 20, color = "green")
plt.xlabel('On-Base Percentage')
plt.ylabel('Number of Players')
plt.title('Random Sample Distribution')
plt.subplots_adjust(wspace=0.4, hspace=1)

plt.subplot(3, 2, 5)
plt.hist(slugging_array, 20, color = "red")
plt.xlabel('Slugging Percentage')
plt.ylabel('Number of Players')
plt.title('2021 Slugging Distribution')
plt.subplots_adjust(wspace=0.4, hspace=1)

plt.subplot(3, 2, 6)
plt.hist(slugging_rn, 20, color = "red")
plt.xlabel('Slugging Percentage')
plt.ylabel('Number of Players')
plt.title('Random Sample Distribution')
plt.subplots_adjust(wspace=0.4, hspace=1)

plt.savefig("slash_line_analysis.png", format="png")
plt.show()