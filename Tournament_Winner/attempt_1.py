def tournamentWinner(competitions, results):
    scores = {}
	
    for i in range(0,len(results)):
        if results[i] == 1:
            if competitions[i][0] in scores:
                scores[competitions[i][0]] += 3
            else:
                scores[competitions[i][0]] = 3
        else:
            if competitions[i][1] in scores:
                scores[competitions[i][1]] += 3
            else:
                scores[competitions[i][1]] = 3
	
	
    return max(scores, key=scores.get)
