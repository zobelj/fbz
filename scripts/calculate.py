from bracket.models import School, Calculate_Setting, Player
import pandas as pd

pyth_exponent = 11.5

def calculate(away_name, home_name, neutral_site):

    settings = Calculate_Setting.objects.all()

    if(neutral_site):
        hcao = 1
        hcad = 1
    else:
        hcao = settings[0].hcao
        hcad = settings[0].hcad

    away = School.objects.get(name=away_name)
    home = School.objects.get(name=home_name)

    #variables
    away_adjO = away.adjO * hcad
    away_adjD = away.adjD * hcao
    away_adjT = away.adjT
    home_adjO = home.adjO * hcao
    home_adjD = home.adjD * hcad
    home_adjT = home.adjT

    #constants
    avg_adjT = settings[0].avg_adjT
    avg_adjO = settings[0].avg_adjO
    
    #calculations
    away_win_percentage_season = (away_adjO ** pyth_exponent) / ((away_adjO ** pyth_exponent) + (away_adjD ** pyth_exponent))
    home_win_percentage_season = (home_adjO ** pyth_exponent) / ((home_adjO ** pyth_exponent) + (home_adjD ** pyth_exponent))

    away_win_percentage_game = ((away_win_percentage_season - (away_win_percentage_season * home_win_percentage_season)) / ((away_win_percentage_season + home_win_percentage_season) - (2 * away_win_percentage_season * home_win_percentage_season)))
    home_win_percentage_game = ((home_win_percentage_season - (home_win_percentage_season * away_win_percentage_season)) / ((away_win_percentage_season + home_win_percentage_season) - (2 * away_win_percentage_season * home_win_percentage_season)))

    away_adjT_plus = away_adjT / avg_adjT
    home_adjT_plus = home_adjT / avg_adjT

    expected_adjT = away_adjT_plus * home_adjT_plus * avg_adjT

    away_adjO_plus = away_adjO / avg_adjO
    home_adjO_plus = home_adjO / avg_adjO

    away_adjD_plus = away_adjD / avg_adjO
    home_adjD_plus = home_adjD / avg_adjO

    away_adj_score = away_adjO_plus * home_adjD_plus * avg_adjO
    home_adj_score = home_adjO_plus * away_adjD_plus * avg_adjO

    away_predicted_score = away_adj_score * (expected_adjT / 100)
    home_predicted_score = home_adj_score * (expected_adjT / 100)

    total_score = home_predicted_score + away_predicted_score
    home_spread = away_predicted_score - home_predicted_score

    return round(away_predicted_score,2), round(home_predicted_score,2), away_win_percentage_game, home_win_percentage_game, total_score, home_spread

def update_reference_stats(school_name):
    print("Updating reference stats for " + school_name)
    ref_name = school_name.lower().replace(" ", "-").replace("'", "")
    if(ref_name == "usc"):
        ref_name = "southern-california"
    if ref_name[-3:] == "st.":
        ref_name = ref_name.replace("st.", "state")
    ref_name = ref_name.replace("st.", "st")

    url = f"https://www.sports-reference.com/cbb/schools/{ref_name}/2022.html"

    df = pd.read_html(url)[-1]
    # read each name and check if it is in the database
    # if it is, update the player
    # if it is not, create a new player
    players = []

    for index, row in df.iterrows():
        player_name = row['Player']
        school_name = school_name
        player_g = row['G']
        player_gs = row['GS']
        player_mp = row['MP']
        player_fg = row['FG']
        player_fga = row['FGA']
        player_fg_pct = row['FG%']
        player_fg2 = row['2P']
        player_fg2a = row['2PA']
        player_fg2_pct = row['2P%']
        player_fg3 = row['3P']
        player_fg3a = row['3PA']
        player_fg3_pct = row['3P%']
        player_ft = row['FT']
        player_fta = row['FTA']
        player_ft_pct = row['FT%']
        player_orb = row['ORB']
        player_drb = row['DRB']
        player_trb = row['TRB']
        player_ast = row['AST']
        player_stl = row['STL']
        player_blk = row['BLK']
        player_tov = row['TOV']
        player_pf = row['PF']
        player_pts = row['PTS']

        players.append(Player(name=player_name, school=school_name, g=player_g, gs=player_gs, mp=player_mp, fg=player_fg, fga=player_fga, fg_pct=player_fg_pct, fg2=player_fg2, fg2a=player_fg2a, fg2_pct=player_fg2_pct, fg3=player_fg3, fg3a=player_fg3a, fg3_pct=player_fg3_pct, ft=player_ft, fta=player_fta, ft_pct=player_ft_pct, orb=player_orb, drb=player_drb, trb=player_trb, ast=player_ast, stl=player_stl, blk=player_blk, tov=player_tov, pf=player_pf, pts=player_pts))
    
    Player.objects.filter(school=school_name).delete()
    Player.objects.bulk_create(players)

def get_reference_stats(school_name):
    players = Player.objects.filter(school=school_name)
    if(len(players) != 0):
        return players

    update_reference_stats(school_name)
    
    return Player.objects.filter(school=school_name)    
