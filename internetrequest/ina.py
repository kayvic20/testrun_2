import requests

response = requests.get("http://checklight.pythonanywhere.com/streets")

data = response.json()
# print(data["response"][0:6:2])
streets_list = data["streets"]
# print(streets_list)
# # print(data.keys())
# # for streets in streets_list:
# #     print(streets["name"].ljust(25),"|", streets["state"].ljust(6),"|", streets['status'],"|",streets['avg_power'])


adenuga = streets_list[13]["history"]
# print(adenuga,":")
adenuga_timeline = adenuga["time_line"]
# print(adenuga_timeline)
for timeline in adenuga_timeline:
    print(timeline["time"],"|", timeline["status"])
# for timeline in adenuga_timeline:
#     if timeline["status"] == 1:
#         print(timeline["time"],"|", "ON")
#     elif timeline["status"] == 0:
#          print(timeline["time"],"|", "OFF")
