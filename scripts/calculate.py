from bracket.models import School

pyth_exponent = 11.5

def calculate(away_name, home_name, neutral_site):

    if(neutral_site):
        hcao = 1
        hcad = 1
    else:
        hcao = 1.014
        hcad = 0.986

    away = School.objects.get(name=away_name)
    home = School.objects.get(name=home_name)

    #variables
    away_adjO = away.adjO * hcad
    away_adjD = home.adjD * hcao
    away_adjT = away.adjT
    home_adjO = home.adjO * hcao
    home_adjD = home.adjD * hcad
    home_adjT = home.adjT

    #constants
    average_adjT = 68.7
    average_points = 101
    

    #calculations
    away_win_percentage_season = (away_adjO ** pyth_exponent) / ((away_adjO ** pyth_exponent) + (away_adjD ** pyth_exponent))
    home_win_percentage_season = (home_adjO ** pyth_exponent) / ((home_adjO ** pyth_exponent) + (home_adjD ** pyth_exponent))

    away_win_percentage_game = ((away_win_percentage_season - (away_win_percentage_season * home_win_percentage_season)) / ((away_win_percentage_season + home_win_percentage_season) - (2 * away_win_percentage_season * home_win_percentage_season)))
    home_win_percentage_game = ((home_win_percentage_season - (home_win_percentage_season * away_win_percentage_season)) / ((away_win_percentage_season + home_win_percentage_season) - (2 * away_win_percentage_season * home_win_percentage_season)))

    away_adjT_plus = away_adjT / average_adjT
    home_adjT_plus = home_adjT / average_adjT

    expected_adjT = away_adjT_plus * home_adjT_plus * average_adjT

    away_adjO_plus = away_adjO / average_points
    home_adjO_plus = home_adjO / average_points

    away_adjD_plus = away_adjD / average_points
    home_adjD_plus = home_adjD / average_points

    away_adj_score = away_adjO_plus * home_adjD_plus * average_points
    home_adj_score = home_adjO_plus * away_adjD_plus * average_points

    away_predicted_score = away_adj_score * (expected_adjT / 100)
    home_predicted_score = home_adj_score * (expected_adjT / 100)

    #total_score = home_predicted_score + away_predicted_score
    #home_spread = away_predicted_score - home_predicted_score

    return round(away_predicted_score,2), round(home_predicted_score,2), away_win_percentage_game, home_win_percentage_game
    