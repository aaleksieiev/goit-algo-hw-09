import timeit
import matplotlib.pyplot as plt

def find_coins_greedy(amount, bank):
    left_over = amount
    result = {}
    for coin_type in bank:
        left_over = left_over - coin_type
        while left_over >= 0:
            if coin_type not in result:
                 result[coin_type] = 0;
            result[coin_type] = result[coin_type] + 1
            left_over = left_over - coin_type
        left_over = left_over + coin_type

    return dict(sorted(result.items()))

def find_min_coins(amount, bank):
    min_coins_required = [0] + [float("inf")]*amount
    last_coin_used = [0] * (amount+1)
    
    #знаходження мін кількості монет
    for s in range(1, amount +1):
        for coin in bank:
            if s >= coin and min_coins_required[s-coin]+1 < min_coins_required[s]:
                min_coins_required[s] = min_coins_required[s-coin]+1
                last_coin_used[s] = coin
                
    # Відновлення набору монет
    count_coins = {}
    current_sum = amount
    while current_sum > 0:
        coin = last_coin_used[current_sum]
        count_coins[coin] = count_coins.get(coin, 0)+1
        current_sum -=coin
        
    return dict(sorted(count_coins.items()))

def main():

    amount = 1313
    bank = [50, 25, 10, 5, 2, 1]

    print(f"bank: {bank}; amount: {amount}")

    

    m1 = timeit.timeit(lambda: find_coins_greedy(amount, bank), number=100)
    
    m2 = timeit.timeit(lambda: find_min_coins(amount, bank), number=100)
    
    print(f"find_coins_greedy: {m1}")
    print(find_coins_greedy(amount, bank))
    print(f"find_min_coins: {m2}")
    print(find_min_coins(amount, bank))

    time_data = []
    for i in range(1000, 20000, 100):
        time_data.append(
            (
                i,
                timeit.timeit(lambda: find_coins_greedy(amount, bank), number=20),
                timeit.timeit(lambda: find_min_coins(amount, bank), number=20),
            )
        )


    x = [x[0] for x in time_data]
    y1 = [x[1] for x in time_data]
    y2 = [x[2] for x in time_data]

    # Create subplots stacked vertically
    fig, (ax1, ax2) = plt.subplots(2, 1)

    # Plot data on the first subplot
    plt.sca(ax1)
    plt.plot(x, y1, label="Greedy")
    plt.xlabel("Sum")
    plt.ylabel("Time")
    plt.legend()
    plt.grid()

    # Plot data on the second subplot
    plt.sca(ax2)
    plt.plot(x, y2, label="Dynamic")
    plt.legend()
    plt.xlabel("Sum")
    plt.ylabel("Time")
    plt.grid()
    plt.show()
    
if __name__ == "__main__":
    main()