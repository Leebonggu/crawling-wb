import csv

def save_to_csv(infos):
  file = open('player_info.csv', mode="w")
  writer = csv.writer(file)
  writer.writerow(["name", "nationality", "current_club", "clubs"])
  for info in infos:
    writer.writerow(list(info.values()))
  return