def catMouseGame(graph):
    n = len(graph)
    # dp[turn][mouse][cat] = result
    dp = [[[0] * n for _ in range(n)] for _ in range(2 * n)]
    
    # Base cases
    for mouse in range(n):
        for cat in range(n):
            if mouse == cat:
                dp[0][mouse][cat] = 2  # Cat wins
            elif mouse == 0:
                dp[0][mouse][cat] = 1  # Mouse wins

    # Fill the dp table
    for turn in range(2 * n - 1, -1, -1):
        for mouse in range(n):
            for cat in range(n):
                if mouse == cat:
                    continue
                if turn % 2 == 0:  # Mouse's turn
                    for next_mouse in graph[mouse]:
                        if next_mouse == 0:
                            dp[turn][mouse][cat] = 1  # Mouse wins
                        elif dp[turn + 1][next_mouse][cat] == 1:
                            dp[turn][mouse][cat] = 1  # Mouse can win
                    if dp[turn][mouse][cat] == 0:
                        dp[turn][mouse][cat] = 2  # Cat wins
                else:  # Cat's turn
                    for next_cat in graph[cat]:
                        if next_cat == 0:
                            continue
                        if dp[turn + 1][mouse][next_cat] == 2:
                            dp[turn][mouse][cat] = 2  # Cat can win
                    if dp[turn][mouse][cat] == 0:
                        dp[turn][mouse][cat] = 1  # Mouse wins

    return dp[0][1][2]  # Starting positions for mouse and cat
