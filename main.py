from player_list import return_player_lists
from scrap_worldbest_info import accumulate_player_info
from save_to_csv import save_to_csv
lists = return_player_lists()

total_player_info = accumulate_player_info(lists)
save_to_csv(total_player_info)
