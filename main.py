import pandas as pd
from pybaseball import playerid_reverse_lookup
from pybaseball import playerid_lookup

df_master = pd.read_csv("Appearances.csv")
print("Master dataframe loaded")

while True:
    team1 = input("Enter Team 1 ID: ")
    team2 = input("Enter Team 2 ID: ")

    df_t1 = df_master.loc[df_master['teamID'] == team1]
    df_t2 = df_master.loc[df_master['teamID'] == team2]

    df_both = pd.merge(df_t1, df_t2, on='playerID')
    df_both = df_both.sort_values("G_all_x", ascending=True)
    print(df_both.to_string())

    player = df_both["playerID"].iloc[0]
    print(player)
    print(playerid_reverse_lookup([player], key_type='bbref')["name_first"] + " " + playerid_reverse_lookup([player], key_type='bbref')["name_last"])