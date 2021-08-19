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
import pandas

# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# temp_list = data["temp"].to_list()
# print(data["temp"].max())

# GET DATA IN COLUMNS   
# print(data["condition"])

# GET DATA IN ROW
# print(data[data["day"] == "Monday"])
# print(data[data["temp"] == data["temp"].max()])

# CREATE A DATAFRAME FROM SCRATCH
data_dict =  {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")