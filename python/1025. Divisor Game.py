def divisorGame(self, N):
        return (N % 2) == 0
        
# DP
def divisorGame(self, N):
        dp = [0]* (N+1)
        dp[1] = False
        for i in range(2, N+1):
            flag = 0
            for j in range(1, i):
                if (i % j) == 0 and dp[i-j] == False:
                    flag = 1
                    break
            dp[i] = True if flag == 1 else False
        
        return dp[N]
