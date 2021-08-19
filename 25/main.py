# # METHOD 1: CSV
# import csv

# with open("weather_data.csv") as data:
#     weather_data = csv.reader(data)
#     temperatures = []
#     for row in weather_data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# # METHOD 2: PANDAS
# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])