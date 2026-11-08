# Conclusions for task 1 and 2

## Task 1

### Complexity comparison:

n - requested amount.

k - number of set of coins.

- Greedy: O(k) time and O(k) space.

- Dynamic programming: O(n × k) time and O(n) space.

Since there are only six sets of coin, the greedy algorithm is much faster and uses less memory.

### Conclusion:

For the given denominations [50, 25, 10, 5, 2, 1], the greedy algorithm shows a more optimal result while requiring less computing.

Dynamic programming is slower because it calculates solutions for all smaller amounts before finding the requested one. However, it is more general and can find the optimal solution even for coin systems where the greedy algorithm does not work correctly.

#### For this particular coin system, the greedy algorithm is more efficient for large amounts. Dynamic programming is useful when the coin denominations do not guarantee an optimal greedy solution.

## Task 2

### Conclusion:

The Monte Carlo method gives an approximate value of the integral. Its result is close to the value calculated using quad (2.666667), but it may be different between executions because it uses random numbers.

Increasing the number of random samples improves the accuracy of the estimation, however, it also increases the execution time.

#### The Monte Carlo method can be used to estimate integrals, but numerical integration with quad provides a more accurate result for this example.
