import requests
from bs4 import BeautifulSoup

URL = f"https://en.wikipedia.org/wiki/"


def extract_clubs_history(html):
  if (html.find('td')) is not None:
    # print(html.find('td').find('a')["title"])
    title = html.find('td').find('a')["title"]
    if "season" not in title:
      return title

def extract_player_info(player):
  # for player_list in player_lists:
  #   print(player_list)
  clubs = []
  result = requests.get(f"{URL}{player}")
  bs_result = BeautifulSoup(result.text, "html.parser")
  info_table = bs_result.find("table", {"class": "infobox vcard"})
  
  name = info_table.find("caption", {"class": "fn"}).getText().strip()
  nationality = info_table.find("td", {"class": "birthplace"}).getText().strip()
  current_club = info_table.find("td", {"class": "org"}).getText().strip()

  # clubs
  get_clubs = bs_result.find("table", {"class": "wikitable"})
  clubs_temp = get_clubs.find_all('tr')

  for club_temp in clubs_temp:
    if (extract_clubs_history(club_temp)) is not None:
      club = extract_clubs_history(club_temp)
      clubs.append(club)
  return {"name": name, "nationality": nationality, "current_club": current_club, "clubs": clubs}
  

def accumulate_player_info(player_list):
  players = []
  for player in player_list:
    info = extract_player_info(player)
    print('ing...', info)
    players.append(info)

  print(players)
  return players
  # return player 
  
  
      # clubs.append(club_temp)

  # tests = info_table.find_all("tr")
  # for temp_club in temp_clubs:
  #   extract_clubs_history(temp_club)
    
  # for test in tests:
  #   if (test.find('th')) is not None:
  #     th_value = test.find('th').getText().strip()
  #     print(test.find('th'))
  #     print(th_value)
  #     if (th_value == "National team‡"):
  #       return
  #     if (test.find('th').find("a")) is not None:
  #       print(test.find('th').find("a"))
      

      # print(test.find('th').getText().strip() == "Club information")
  
  # name[:-3]
  # for temp_club in temp_clubs:
  #   if (temp_club.find("a") is not None and temp_club.find("a").has_attr('title')):
  #     print(temp_club.find("a"))
  
      
    #   # print(temp_club.find("a").attrs)
    #   print(temp_club.find("a").get("title"))
    #   print(temp_club.find("a").string)
    # club = temp_club["title"]
# f"문자열={들어갈변수}"
