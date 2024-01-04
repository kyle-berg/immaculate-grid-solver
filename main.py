import pandas as pd
from pybaseball import playerid_reverse_lookup
from pybaseball import playerid_lookup

df_master = pd.read_csv("Appearances.csv")
print("Master dataframe loaded")

while True:
    team1 = input("Enter Team 1 ID/POSITION: ")
    team2 = input("Enter Team 2 ID: ")

    if team1 == "C":
        df_both = df_master.loc[(df_master['G_c'] > 1) & (df_master['teamID'] == team2)]
        df_both = df_both.sort_values("G_all", ascending=True)

    elif team1 == "P":
        df_both = df_master.loc[(df_master['G_p'] > 1) & (df_master['teamID'] == team2)]
        df_both = df_both.sort_values("G_all", ascending=True)

    elif team1 == "1B":
        df_both = df_master.loc[(df_master['G_1b'] > 1) & (df_master['teamID'] == team2)]
        df_both = df_both.sort_values("G_all", ascending=True)

    elif team1 == "2B":
        df_both = df_master.loc[(df_master['G_2b'] > 1) & (df_master['teamID'] == team2)]
        df_both = df_both.sort_values("G_all", ascending=True)

    elif team1 == "3B":
        df_both = df_master.loc[(df_master['G_3b'] > 1) & (df_master['teamID'] == team2)]
        df_both = df_both.sort_values("G_all", ascending=True)

    elif team1 == "SS":
        df_both = df_master.loc[(df_master['G_ss'] > 1) & (df_master['teamID'] == team2)]
        df_both = df_both.sort_values("G_all", ascending=True)

    elif team1 == "LF":
        df_both = df_master.loc[(df_master['G_lf'] > 1) & (df_master['teamID'] == team2)]
        df_both = df_both.sort_values("G_all", ascending=True)

    elif team1 == "CF":
        df_both = df_master.loc[(df_master['G_cf'] > 1) & (df_master['teamID'] == team2)]
        df_both = df_both.sort_values("G_all", ascending=True)

    elif team1 == "RF":
        df_both = df_master.loc[(df_master['G_rf'] > 1) & (df_master['teamID'] == team2)]
        df_both = df_both.sort_values("G_all", ascending=True)

    else:
        df_t1 = df_master.loc[df_master['teamID'] == team1]
        df_t2 = df_master.loc[df_master['teamID'] == team2]
        
        df_both = pd.merge(df_t1, df_t2, on='playerID')
        df_both = df_both.sort_values("G_all_x", ascending=True)
        
    print(df_both.to_string())

    player = df_both["playerID"].iloc[0]
    print(player)
    print(playerid_reverse_lookup([player], key_type='bbref')["name_first"] + " " + playerid_reverse_lookup([player], key_type='bbref')["name_last"])