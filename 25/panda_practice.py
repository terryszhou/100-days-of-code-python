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
# data_dict = data.to_dict()
# temp_list = data["temp"].to_list()
# print(data["temp"].max())

# GET DATA IN COLUMNS   
# print(data["condition"])

# GET DATA IN ROW
# print(data[data["day"] == "Monday"])
# print(data[data["temp"] == data["temp"].max()])

# CREATE A DATAFRAME FROM SCRATCH
# data_dict =  {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# MY SOLVE
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# data_dict = {}
# for color in data["Primary Fur Color"]:
#     if color in data_dict:
#         data_dict[color] += 1
#     else:
#         data_dict[color] = 1
# new_dict = {
#     "Fur Color": [],
#     "Count": []
# }
# for i in data_dict:
#     if i != "nan":
#         new_dict["Fur Color"].append(i)
#         new_dict["Count"].append(data_dict[i])
# new_data = pandas.DataFrame(new_dict).dropna()
# new_data.to_csv("new_data.csv")

# CLASS SOLVE
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
# }
# df = pandas.DataFrame(data_dict)
# df.to_csv("new_data.csv")





