def buy_sell(prices: list[int]) -> tuple[int, tuple[int, int]]:
    if len(prices) <= 1:
        return (0, (0, 0))
    max_profit: int = prices[1] - prices[0]
    buy: int = 0
    sell: int = 1
    min_price = prices[0]
    for i in range(len(prices) - 1):
        if prices[i] >= min_price:
            continue
        min_price = prices[i]
        local_max_profit: int = prices[i + 1] - prices[i]
        local_sell: int = i + 1
        for j in range((i + 1), len(prices)):
            ops += 1
            if (prices[j] - prices[i]) > local_max_profit:
                local_max_profit = prices[j] - prices[i]
                local_sell = j
        if local_max_profit > max_profit:
            max_profit = local_max_profit
            sell = local_sell
            buy = i
    return (max_profit, (buy, sell))

if __name__ == "__main__":
    print(buy_sell([6, 9, 1, 3, 2, 8, 9, 7, 4, 2, 8, 6]))
