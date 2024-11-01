# goit-algo-hw-09

We have a set of coins [50, 25, 10, 5, 2, 1]. Imagine that you are developing a system for a cash register that has to determine the best way to give change to a customer.

You need to write two functions for the cash register system that gives change to the customer:

The function of the greedy algorithm find_coins_greedy. This function should take the money given to the customer and return a dictionary with the number of coins of each denomination used to make up the amount. For example, for 113, this would be the dictionary {50: 2, 10: 1, 2: 1, 1: 1}. The algorithm should be greedy, i.e., choose the most available coin denominations first.
Dynamic programming function find_min_coins. This function should also take an amount of change but use a dynamic programming method to find the minimum number of coins needed to generate that amount. The function should return a dictionary with the coin denominations and the number of coins needed to reach the given amount most efficiently. For example, for the sum of 113, this would be the dictionary {1: 1, 2: 1, 10: 1, 50: 2}
Compare the performance of the greedy and dynamic programming algorithms based on their execution time or O large and pay attention to their performance for large sums. Highlight how they handle large amounts and why one algorithm may be more efficient in certain situations. Include your findings in the readme.md file for homework.


Result:
{1: 1, 2: 1, 10: 1, 50: 2}
find_coins_greedy: 11.629851346995565  ()
{50: 2, 10: 1, 2: 1, 1: 1}
find_min_coins: 249.79091520899965
