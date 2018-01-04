import csv
import pandas as pd
file = open("Iris.csv")
reader = csv.reader(file)
iris_list = list(reader)
clean_iris_list = iris_list.split(",")
print(iris_list)
