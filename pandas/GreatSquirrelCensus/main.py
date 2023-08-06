import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colors = ["Gray", "Cinnamon", "Black"]
data_dict = {
    "Fur Color": [],
    "Count": []
}

for color in colors:
    number = len(data[data["Primary Fur Color"] == color])
    data_dict["Fur Color"].append(color)
    data_dict["Count"].append(number)

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
