from typing import List


def withdraw(amount: int, coins: List[int]) -> List[int]:
    result = [amount+1] * (amount+1)
    coins_results = [[] for _ in range(amount+1)]

    result[0] = 0

    for i in range(1, amount+1):
        for coin in coins:
            if i >= coin and result[i - coin] + 1 < result[i]:
                result[i] = result[i-coin] + 1
                coins_results[i] = coins_results[i-coin] + [coin]

    if result[amount] == amount+1:
        return []

    return coins_results[amount]

def main():
    # assert Solution().containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0) is True
    # assert Solution().containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2) is True
    # assert Solution().containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3) is False
    print(withdraw(40, [100, 50, 20]))
    print(withdraw(250, [100, 50, 20]))
    print(withdraw(260, [100, 50, 20]))





if __name__ == '__main__':
    main()