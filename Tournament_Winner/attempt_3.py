def tournamentWinner(competitions, results):
    scores = {"": 0}
    curr_best_team = ""

    for i in range(0,len(results)):

        home_team, away_team = competitions[i][0], competitions[i][1]
        winning_team = ""

        winning_team = home_team if results[i] == 1 else away_team

        if winning_team not in scores:
            scores[winning_team] = 3
        else:
            scores[winning_team] += 3

        if not curr_best_team:
            curr_best_team = winning_team
        elif scores[winning_team] > scores[curr_best_team]:
            curr_best_team = winning_team
	
    return curr_best_team
