# Conclusions for task 1 and 2

## Task 1

### Complexity comparison:

n - requested amount.

k - number of set of coins.

- Greedy: O(k) time and O(k) space.

- Dynamic programming: O(n × k) time and O(n) space.

Since there are only six sets of coin, the greedy algorithm is much faster and uses less memory.

### Conclusions:

For the given denominations [50, 25, 10, 5, 2, 1], the greedy algorithm shows a more optimal result while requiring less computing.

Dynamic programming is slower because it calculates solutions for all smaller amounts before finding the requested one. However, it is more general and can find the optimal solution even for coin systems where the greedy algorithm does not work correctly.

#### For this particular coin system, the greedy algorithm is more efficient for large amounts. Dynamic programming is useful when the coin denominations do not guarantee an optimal greedy solution.