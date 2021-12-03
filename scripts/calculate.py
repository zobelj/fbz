from bracket.models import School
from bracket.models import Calculate_Setting

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
    