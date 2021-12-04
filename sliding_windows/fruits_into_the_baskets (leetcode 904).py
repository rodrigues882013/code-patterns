'''
Given an array of characters where each character represents a fruit tree, you are given two baskets, 
and your goal is to put maximum number of fruits in each basket.

The only restriction is that each basket can have only one type of fruit.
You can start with any tree, but you can’t skip a tree once you have started. 
You will pick one fruit from each tree until you cannot, 
i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both baskets.

a, b, [c, a], c]

b1 {c: 1} b2 {a: 1}
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

a, [b, c,  b, b, c]
           
b1 {c: 2} b2 {b: 3}
Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
'''

import copy

def safe_value(d):
    if len(d.keys()) > 0 and list(d.values())[0] != 0:
        return list(d.values())[0]
    else:
        return 0

# My solution
def fruits_into_baskets2(fruits: list[str]) -> int:
    maximum_accumulated_into_baskets = -1
    runner = 0
    window_start = 0
    window_end = 0
    basket_one = {}
    basket_two = {}

   
    while runner < len(fruits):
        if fruits[runner] in basket_one:
            basket_one[fruits[runner]] += 1
            window_end += 1

        elif fruits[runner] in basket_two:
            basket_two[fruits[runner]] += 1
            window_end += 1

        else:
            if len(basket_one.keys()) == 0:
                basket_one[fruits[runner]] = 1

            elif len(basket_two.keys()) == 0:
                basket_two[fruits[runner]] = 1
                window_end += 1

            else:
                while (window_start < window_end and fruits[window_start] != fruits[window_end]) or window_start < window_end:
                    if safe_value(basket_one) == 0 or safe_value(basket_two) == 0:
                        break

                    if fruits[window_start] in basket_one:
                        basket_one[fruits[window_start]] -= 1

                    elif fruits[window_start] in basket_two:
                        basket_two[fruits[window_start]] -= 1

                    window_start += 1

                if safe_value(basket_one) == 0:
                    basket_one.clear()
                    basket_one = copy.deepcopy(basket_two)
                    basket_two.clear()
                    basket_two[fruits[runner]] = 1
                    window_end += 1
                

                elif safe_value(basket_two) == 0:
                    basket_two.clear()
                    basket_two[fruits[runner]] = 1
                    window_end += 1

        local_max = safe_value(basket_one) + safe_value(basket_two)
        maximum_accumulated_into_baskets = max(maximum_accumulated_into_baskets, local_max)
        runner += 1

    return maximum_accumulated_into_baskets


# Grokking's solution
def fruits_into_baskets(fruits):
  window_start = 0
  max_length = 0
  fruit_frequency = {}

  # try to extend the range [window_start, window_end]
  for window_end in range(len(fruits)):
    right_fruit = fruits[window_end]
    
    if right_fruit not in fruit_frequency:
      fruit_frequency[right_fruit] = 0
    
    fruit_frequency[right_fruit] += 1

    # shrink the sliding window, until we are left with '2' fruits in the fruit frequency dictionary
    while len(fruit_frequency) > 2:
      left_fruit = fruits[window_start]
      fruit_frequency[left_fruit] -= 1
      
      if fruit_frequency[left_fruit] == 0:
        del fruit_frequency[left_fruit]
      
      window_start += 1  # shrink the window
    max_length = max(max_length, window_end-window_start + 1)
  return max_length


def main():
    print(fruits_into_baskets(['A', 'B', 'C', 'A', 'C']))
    #print(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']))
    #print(fruits_into_baskets([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
    #print(fruits_into_baskets([1, 1]))
    #rint(fruits_into_baskets([0]))
    #print(fruits_into_baskets([1,0,1,4,1,4,1,2,3]))
    #print(fruits_into_baskets([0,1,6,6,4,4,6]))
    #print(fruits_into_baskets([1,0,0,0,1,0,4,0,4]))
    # [1], 0, 1, 4, 1, 4, 1, 2, 3
    # b1 {1: 1} b2 {}


if __name__ == '__main__':
    main()