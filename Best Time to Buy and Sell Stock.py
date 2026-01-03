def best_time(prices):
    mini=float('inf')
    cost=0
    profit=float('-inf')
    for i in range(len(prices)):
        mini=min(mini,prices[i])
        cost=prices[i]-mini
        profit=max(profit,cost)
    return profit

prices=list(map(int,input().split()))
print(best_time(prices))