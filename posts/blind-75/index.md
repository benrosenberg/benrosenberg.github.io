---
title: Blind 75 Solutions and Methods
author: "[Ben Rosenberg](https://benrosenberg.info)"
date: \today
---

<style>
/* @media (min-width:1281px) {
    #myBtn { right: px; }
} */

#myBtn { 
    display: none; 
    position: fixed; 
    bottom: 50px;
    right: 50px; 
    z-index: 99; 
    font-size: 18px; 
    border: none;
    outline: none; 
    background-color: #599F4B; 
    color: white;
    cursor: pointer; 
    padding: 15px; 
    border-radius: 4px;
} 

#myBtn:hover { 
    background-color: #555; 
}
</style>

<button onclick="topFunction()" id="myBtn" title="Go to top">Top</button>

# How to use this list

This is a collection of thoughts on and solutions to the **Blind 75**, a well-known list of Leetcode problems that are commonly seen on coding interviews for positions in software engineering and related fields. Above, there is a table of contents with links to each question, arranged by the type of problem. 

Each of the code blocks found in the problem discussions has on its left edge a colored sidebar, which has the following meaning:

 - <div style="display:inline; color:#fb4934">Red</div>: not a recommended method of solving the problem, or doesn't work, or excessively complex, etc.
 - <div style="display:inline; color:#CCCCCC">Grey</div>: neutral. Not a solution, or not a great solution but a good solution, etc.
 - <div style="display:inline; color:#599F4B">Green</div>: recommended solution (or only solution that I have found).

Some of the code blocks were adapted from other sources. The links to these sources are in a comment at the beginning of the code block.

If you use any of the code or text from this page, please either cite the source given in the code and this page, or just cite this page ([https://benrosenberg.info/posts/blind-75/](https://benrosenberg.info/posts/blind-75/)).

# Array

## Two Sum

> Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
> You may assume that each input would have exactly one solution, and you may not use the same element twice.
> You can return the answer in any order.

This problem has an easy solution (brute force) and a slightly less intuitive solution.

The easy brute force solution is to just look at all the pairs of indices:

```{.python .numberLines startFrom="1" .neutral}
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target: 
                    return [i, j]
```

The less intuitive solution is to iterate through the entire list and create a dictionary storing the differences needed to get to the target number. For the bit of added space complexity we use ($O(n)$ over the brute force's $O(1)$) we get a much faster $O(n)$ runtime (over the brute force's $O(n^2)$).

```{.python .numberLines startFrom="1" .good}
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # this is now O(n)
        diff_dict = {target - nums[i] : i for i in range(len(nums))}
        
        for i in range(len(nums)):
            if nums[i] in diff_dict and diff_dict[nums[i]] != i: 
                return [i, diff_dict[nums[i]]]
```

## Best Time to Buy and Sell Stock

> You are given an array `prices` where `prices[i]` is the price of a given stock on the $i$th day.
> You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
> Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

This problem is the first example of the "keeping track of the optimum" idea in the array problems. Rather than iterating through all the possible times for buying and selling stock (which takes $O(n^2)$ time), we can instead just iterate once and keep track of the relevant information as we go. (The brute force method is omitted as it generally exceeds the time limit on Leetcode, and is pretty easy to code up [it's basically a slightly modified version of the brute-force two-sum].)

The below solution runs in $O(n)$ time and $O(1)$ space.

```{.python .numberLines startFrom="1" .good}
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # keep track of max profit as we go
        max_profit = 0
        
        min_price = prices[0]
        for i in prices[1:]:
            this_profit = i - min_price
            if this_profit > max_profit:
                max_profit = this_profit
            
            if i < min_price:
                min_price = i
        
        return max_profit
```

## Contains Duplicate

> Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

This is, without a doubt, one of the easiest Leetcode problems, if not *the* easiest (at least in Python). The solution is below:

```{.python .numberLines startFrom="1" .good}
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
```

Recall that a property of a `set` is that it contains no duplicate elements. By casting `nums` to a `set`, we get a version of `nums` without duplicates. (This cast takes $O(n)$ time, as it needs to remove the duplicates.) Then, we take the length of this newly created set, and compare it with the length of `nums` -- if the lengths are the same, then no elements were removed in the casting. Otherwise, some element must have been removed, so there must have been at least one duplicate element.

A more traditional (and less Pythonic) solution might be as follows:

```{.python .numberLines startFrom="1" .good}
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        no_duplicates = set()

        for num in nums:
            # Set.add() only adds if element not present
            no_duplicates.add(num)

        return len(no_duplicates) != len(nums)
```

The reason we can use `.add()` inside of the loop is that the `set` structure is a kind of hashmap, which has $O(1)$ amortized lookup time. Thus, the total time complexity remains $O(n)$.

## Product of Array Except Self

> Given an integer array `nums`, return an array answer such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.
> The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.
> You must write an algorithm that runs in $O(n)$ time and without using the division operation.

To be honest, I broke the rules a little on this one -- I used the division operation. But Leetcode didn't detect it, so whatever I guess?

The efficient method used below is to get the product of the entire array, and just divide it by whatever value is at the present index when necessary to get the "product besides self". (Complications re:zero are worked out below.)

This solution is a little more complicated than it needed to be, but it works. The stuff with `reduce` and the `prod` function just makes it easier for me to take a product of an array. 

The below code runs in $O(n)$ time and $O(1)$ space:

```{.python .numberLines startFrom="1" .good}
from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def prod(L):
            return reduce(lambda x,y:x*y, L)
        
        # in this case the entire array will be zeroes
        if nums.count(0) > 1:
            return [0]*len(nums)
        
        # in this case we need to account for the fact that
        # zero breaks division
        if nums.count(0) == 1:
            no_zero = nums[:nums.index(0)] + nums[nums.index(0)+1:]
            no_zero_prod = prod(no_zero)

        total_prod = prod(nums)
        
        # divide total product by relevant entry if possible, otherwise return nonzero product
        return [total_prod // i if i != 0 else no_zero_prod for i in nums]
```

If there is more than one zero, the entire array will just be zeroes (because there will always be another zero, regardless of what index you're in). This check, as well as the one below it (to ensure that zeroes are successfully dealt with), enables us to use the "illegal" division shortcut on [line 21](#cb6-21).

## Maximum Subarray

> Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
> 
> **Note**: A *subarray* is a contiguous part of an array.

The following code is a solution from Wikipedia.

```{.python .numberLines startFrom="1" .good}
# source: wikipedia
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if min(nums) > 0:
            return sum(nums)
        
        if max(nums) < 0:
            return max(nums)
        
        best_sum = float('-inf')
        current_sum = 0
        for x in nums:
            current_sum = max(x, current_sum + x)
            best_sum = max(best_sum, current_sum)
        return best_sum
```

This is kind of a DP (Dynamic Programming)-like solution. The first two checks are for simple edge cases that can be done in one simple pass and serve as starting points for the intuition behind the problem. The rest is **Kadane's Algorithm** for finding the maximum contiguous subarray:

 - Initialize variables for $\texttt{best\_sum}$ and $\texttt{current\_sum}$
 - Iterate through `nums` with variable $x$
   - At each value of $x$, check whether $\texttt{current\_sum} + x > x$; that is, whether it is better to continue the streak of adding numbers together, or to scrap that and just take the current $x$ as the better local max
     - If $\texttt{current\_sum} + x > x$, set $\texttt{current\_sum} := \texttt{current\_sum} + x$
     - Otherwise, continue (leave $\texttt{current\_sum}$ as is)
   - Perform a similar check for $\texttt{best\_sum}$: 
     - If $\texttt{best\_sum} > \texttt{current\_sum}$, set $\texttt{best\_sum} := \texttt{current\_sum}$
     - Otherwise, continue (leave $\texttt{best\_sum}$ as is)
 - Return $\texttt{best\_sum}$

This algorithm takes advantage of the fact that <u>for each local max subarray ending at index $i$, that max subarray will either be a singleton containing just element $i$, or will contain within it the local max subarray ending at index $i-1$.</u> This means that we can use previous results to find future results, and so there are overlapping subproblems; thus, this is a dynamic programming problem. 

The specific recurrence relation here is as follows: 
<div style="text-align:center;">`local_max[i]` = max(`local_max[i-1]` + `nums[i]`, `nums[i]`)</div>


You can see this on [line 13](#cb7-13).
    
## Maximum Product Subarray

> Given an integer array `nums`, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
> The test cases are generated so that the answer will fit in a 32-bit integer.

The idea behind this solution is similar to that of the previous question, with a couple extra caveats:

 - There may be an odd number of negative elements, so we check both forwards and backwards to ensure elements aren't excluded from the product because of the fact that they lie on the right side of an odd number of negatives (causing the product when they are included to remain negative)
   - Example of case that doesn't work without backwards check: `[3, -1, 4]` (answer is `3` if only checked forwards)
 - Zeroes delineate groups of elements, as multiplying by zero annihilates our running product

```{.python .numberLines startFrom="1" .good}
# source: https://github.com/mccornet/dynamic-programming-examples/wiki/09-The-maximum-product-subarray
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def product_pass(nums):
            best_prod = nums[0]
            current_prod = 1
            for num in nums:  
                # extend running product  
                current_prod = current_prod * num
                
                # reset total if zero encountered
                if current_prod == 0: 
                    current_prod = num

                best_prod = max(best_prod, current_prod)

            return best_prod

        # take max over both forward and backward passes
        return(max(product_pass(nums), product_pass(nums[::-1])))
```

## Find Minimum in Rotated Sorted Array

> Suppose an array of length $n$ sorted in ascending order is rotated between $1$ and $n$ times. For example, the array `nums = [0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]` if it was rotated $4$ times, or `[0,1,2,4,5,6,7]` if it was rotated $7$ times.
>
> Notice that rotating an array `[a[0], a[1], a[2], ..., a[n-1]]` $1$ time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.
>
> Given the sorted rotated array nums of unique elements, return the minimum element of this array.
> You must write an algorithm that runs in $O(\log(n))$ time.

The fact that we are told we need to do this in "$O(\log(n))$ time", combined with the fact that we are *searching* for something, should set off alarms that we need to use **binary search**:

```{.python .numberLines startFrom="1" .good}
class Solution:
    def findMin(self, nums: List[int]) -> int:  
        # small data
        if len(nums) < 3:
            return min(nums)
        
        # binary search
        mid = len(nums) // 2
        left = 0
        right = len(nums)-1
        
        if nums[left] > nums[mid]: # left is unsorted
            # try left
            return self.findMin(nums[left:mid+1])
            
        elif nums[mid] > nums[right]: # right is unsorted
            # try right
            return self.findMin(nums[mid:right+1])
        
        else: # array must be sorted
            return nums[0] 
```

The solution to this is slightly complicated by the fact that the array is also rotated by some amount. So, rather than looking for a target value, we're instead looking for the place where the array goes from its minimum to its maximum; e.g., for `[4,5,6,7,0,1,2]`, it would be the `[... 7, 0, ...]` part. We'll call this place the "pivot" of the array.

We can do this by changing the conditions for searching the left and right sides of the array. Usually in binary search, we search the left side if the target value is less than the `mid` value we've chosen; this time, we want to search the left side if the left side contains the pivot. The same logic holds for the right side.

It's easy to tell whether a part of the array contains the pivot: just check whether the first and last elements of that part are sorted correctly. Any rotation would disrupt the ordering of these elements; and in order for them to be out of order, the pivot must be in there somewhere! (This is actually similar logic to the Intermediate Value Theorem, which should have been taught in your calculus class.)

## Search in Rotated Sorted Array

> There is an integer array `nums` sorted in ascending order (with distinct values).
> 
> Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index $k$ ($1 \leq k < \texttt{nums.length}$) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` ($0$-indexed). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index $3$ and become `[4,5,6,7,0,1,2]`.
> 
> Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or $-1$ if it is not in `nums`.
>
> You must write an algorithm with $O(\log(n))$ runtime complexity.

The solution that I wrote for this problem leans on the solution to the previous problem ("Find Minimum in Rotated Sorted Array"), reconstructs the array based on the results of that solution, and then uses a simple binary search to find the target:

```{.python .numberLines startFrom="1" .good}
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # add indices to array as metadata 
        nums_with_indices = list(zip(nums, range(len(nums))))
        
        # same binary search as "Find Minimum in Rotated Sorted Array", but with index metadata
        def min_search(nums_with_indices):  
        
            if len(nums_with_indices) < 3:
                return min(nums_with_indices, key=lambda x : x[0])

            mid = len(nums_with_indices) // 2
            left = 0
            right = len(nums_with_indices)-1

            if nums_with_indices[left][0] > nums_with_indices[mid][0]: # left is unsorted
                # try left
                return min_search(nums_with_indices[left:mid+1])

            elif nums_with_indices[mid][0] > nums_with_indices[right][0]: # right is unsorted
                # try right
                return min_search(nums_with_indices[mid:right+1])

            else: # array must be sorted
                return nums_with_indices[0]
        
        # get the index of the min element
        x, min_index = min_search(nums_with_indices)
        
        # now we can construct a sorted version of the array
        sorted_nums = nums_with_indices[min_index:] + nums_with_indices[:min_index] # swap position of subarrays
        
        # regular binary search 
        def bin_search(sorted_nums, target):
            if len(sorted_nums) == 1:
                if sorted_nums[0][0] == target:
                    return sorted_nums[0][1]
                return -1
    
            mid = len(sorted_nums) // 2
        
            if sorted_nums[mid][0] > target:
                return bin_search(sorted_nums[:mid], target) # search left for target
            elif sorted_nums[mid][0] < target:
                return bin_search(sorted_nums[mid:], target) # search right for target
            else:
                if sorted_nums[mid][0] == target:
                    return sorted_nums[mid][1]
                else:
                    return -1
            
        # now use regular binary search on sorted array
        return bin_search(sorted_nums, target)
```

The main complication in this translation is that instead of returning just a value, we need to return the *index* of the target, so we need to pass the indices around everywhere as metadata. (The fact that we add metadata to every element kind of makes the algorithm $O(n)$, but Leetcode accepts it, so whatever.)

## 3 Sum

> Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that $i \neq j$, $i \neq k$, and $j \neq k$, and `nums[i] + nums[j] + nums[k] == 0`.
> 
> **Note**: The solution set must not contain duplicate triplets.

This problem can be solved similarly to the next one ("Container With Most Water"); both use the idea of left and right pointers closing in on a solution. 

Since we're looking for 3 different numbers in the array, the best by which we can really reduce our time is a factor of $n$, so we'll be looking at $O(n^2)$ time here. To that end, we need to essentially solve another version of two-sum, which we know we can solve in $O(n)$ time.

Since we're already at $O(n^2)$, we might as well sort the array to make things easier for us. Sorting is $O(n\log(n))$, so it has no effect on our total time complexity.

Then, we iterate through the array, skipping duplicates (which is easily done since the array is sorted), and employ a two-pointer technique to close in on a desirable two-sum. Since the array is sorted, we can use a method in which we initialize a left pointer to the first index of the remainder of the array, and a right pointer to the rightmost index of the array. 

Then, at each step (while the left pointer hasn't touched the right pointer [that is, while $l < r$]) we can check the value of the sum of `nums[l]` and `nums[r]`, and compare it to the desired value. Note that since we're trying to sum to $0$, we are looking for indices $l$ and $r$ such that $\texttt{nums}[l] + \texttt{nums}[r] = -\texttt{nums}[i]$, where $i$ is the iteration variable for our outer loop. (You can rearrange this expression to get $\texttt{nums}[l] + \texttt{nums}[r] + \texttt{nums}[i] = 0$.)

If our two-sum using $l$ and $r$ is too high, we can decrement the right pointer to decrease it; and if the two-sum is too low, we can increment the left pointer to increase it. That way, we find all relevant solutions.

```{.python .numberLines startFrom="1" .good}
# source: [Neetcode](https://www.youtube.com/watch?v=jzZsG8n2R9A)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        nums.sort() # O(n log n)
        
        out = []
        
        for i in range(len(nums)-1):
            # skip if already seen
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # left and right pointers close in on solution
            l, r = i+1, len(nums)-1
            while l < r:
                # skip if already seen
                if nums[l] == nums[l-1] and l > i+1:
                    l += 1
                    continue
                if r < len(nums)-1 and nums[r] == nums[r+1]:
                    r -= 1
                    continue
                
                this_sum = nums[l] + nums[r]
                if this_sum > -nums[i]:
                    r -= 1
                elif this_sum < -nums[i]:
                    l += 1
                else:
                    # found triplet [nums[i], nums[l], nums[r]]
                    out.append([nums[i], nums[l], nums[r]])
                    l += 1
            
        return out
```

We also skip duplicates when incrementing and decrementing the left and right pointers. The fact that we skip duplicates in all instances of pointer manipulation means that we output no duplicate triples (as required). In the case that we found a good set of pointers, we append our new triplet to the running list, and continue by incrementing the left pointer (it doesn't really matter which pointer we increment or decrement, as long as we make a change -- Leetcode accepts both solutions).


## Container With Most Water

> You are given an integer array `height` of length $n$. There are $n$ vertical lines drawn such that the two endpoints of the $i$th line are $(i, 0)$ and $(i, \texttt{height}[i])$.
>
> Find two lines that together with the $x$-axis form a container, such that the container contains the most water.
> Return the maximum amount of water a container can store.
> 
> **Note**: You may not slant the container.

This problem can actually be solved in a "greedy" way, by starting at either end of the array and closing in on the center. 

The below solution starts with two pointers, `l` and `r`, and moves them closer to the center according to which choice increases the storage capacity more. It stops looking when the two pointers meet (when `l >= r`).

```{.python .numberLines startFrom="1" .good}
# source: [Neetcode](https://www.youtube.com/watch?v=UuiTKBwPgAo)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # idea: start at endpoints and close in on center
        l, r = 0, len(height) - 1
        max_fill = 0
        
        while l < r:
            # the amount filled will be the base (r-l) times the min side height
            this_fill = (r - l) * min(height[l], height[r])

            max_fill = max(this_fill, max_fill)

            if height[l] < height[r]: # move L 
                l += 1
            else: # move R
                r -= 1
                
        return max_fill
```


# Binary

## Sum of Two Integers

> Given two integers $a$ and $b$, return the sum of the two integers without using the operators $+$ and $-$.

This problem is phrased (and constructed) rather poorly. Leetcode actually accepts the following solution (!):

```{.python .numberLines startFrom="1" .bad}
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # this is literally illegal but works
        return a + b
```

As you can guess from the section, we're supposed to use the numbers' representation in binary in order to do this. The best way to do this is with *bitwise operations*, which are described in the following table:

operation | name | meaning | examples
-|-|-|-
`^` | XOR | bitwise exclusive or | `(0,0), (1,1) => 0; (0,1), (1,0) => 1` 
`|` | OR | bitwise or | `(0,1), (1,0), (1,1) => 1; (0,0) => 0`
`&` | AND | bitwise and | `(0,0), (0,1), (1,0) => 0; (1,1) => 1`
`<<` | LSHIFT | bit shift left | `(b0010, 1) => b0100; (6,1) => 12`
`>>` | RSHIFT | bit shift right | `(b0010, 1) => b0001; (6,1) => 3`
`~` | INVERT | bitwise complement | `b0010 => b1101; 6 => -7; -7 => 6`

Using these operators, we get the following solution:

```{.java .numberLines startFrom="1" .good}
class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {
            int tmp = (a & b) << 1;
            a = a ^ b;
            b = tmp;
        }
        return a;
    }
}
```

Note that this solution is in **Java** and *not* in Python. This is because integers are weird in Python. In general, it's probably best to stick with Java for anything that requires the use of bitwise operations.

What's going on in this solution? Let's look at each line and see what it does.

 - On [line 4](#cb14-4), we assign `tmp` the value `(a & b) << 1`. 
   - Let's unpack the value we get here. First, we're taking the *bitwise and* of `a` and `b`. This gives us only the locations where we have two `1`'s. Then, we're shifting them all to the left by one place, using the *bitwise left shift* operator. 
   - This is the **carry** part of addition. When we have two `1`'s, we get 0, but we need to carry the `1` to the next place over.
 - On [line 5](#cb14-5), we reassign `a` to the value `a ^ b`.
   - This is the result of taking the *bitwise xor* of `a` and `b`, and represents the immediate result from summing the two elements together (without the carrying). For example, `0 ^ 0 = 0`, and `0 + 0 = 0`; similarly, `0 ^ 1 = 1 ^ 0 = 1`, and `0 + 1 = 1`; the only difference is regarding the carrying done in the `1 + 1` case (which is `0` for `1 ^ 1` but requires a carry in regular addition). We don't worry about the carry part because it's taken care of by the value calculated and assigned to `tmp`.
 - We then assign `b` to `tmp` on [line 6](#cb14-6). (We needed to delay this assignment in order to use the value of `b` in the assignment to `a`. This is an inconvenient part of Java; in Python, we would have been able to update the variables with simple multiple assignment, as `a, b = a ^ b, (a & b) << 1`.)
 - The while loop on [line 3](#cb14-3) ensures that we keep iterating through our value pairs until we get to `b == 0`, which indicates that there are no more digits left to carry and our result is final (and stored in `a`).

## Number of 1 Bits

> Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

This one is trivial with the following implementation:

```{.python .numberLines startFrom="1" .good}
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
```

There's probably a more "efficient" or "traditional" way to do it, which may or may not involve using bitwise operators, but the above works fine and is accepted by Leetcode.

## Counting Bits

> Given an integer $n$, return an array `ans` of length $n + 1$ such that for each $i$ ($0 \leq i \leq n$), `ans[`$i$`]` is the number of `1`'s in the binary representation of $i$.

This problem is kind of like two-sum: there's an easy way to do it, and an efficient way to do it.

Here's the easy way, using our solution to "Number of 1 Bits":

```{.python .numberLines startFrom="1" .bad}
class Solution:
    def countBits(self, n: int) -> List[int]:
        def ones(b):
            return bin(b).count('1')
        
        return [ones(i) for i in range(n+1)]
```

This solution comes out to $O(n\log(n))$ time, as each call of `ones(b)` takes $\log(n)$ time (as there are $\log(n)$ digits in the binary representation of a number).

Here's the efficient solution, using the dictionary `memo` to save the results from previous calculations. 

```{.python .numberLines startFrom="1" .good}
class Solution:
    def countBits(self, n: int) -> List[int]:

        memo = {0: 0, 1: 1}

        def ones(b):
            if b in memo:
                return memo[b]

            # if b ends in 1, subtract the one and return 1 + rest
            if b % 2 == 1:
                memo[b] = 1 + ones(b-1)
                return memo[b]

            # if b ends in 0, divide by 2 and return result
            memo[b] = ones(b / 2)
            return memo[b]
        
        return [ones(i) for i in range(n+1)]
```

This solution takes $O(n)$ time, as we only need to calculate each value once and can use previous values in the calculation of future values. The dictionary `memo` provides $O(1)$ lookup time.

Note that in order to get the "overlapping subproblems" idea necessary to take advantage of dynamic programming (of which this is indeed an example -- memoization is a hallmark of certain DP problems), we need to use an "overlapping subproblems" method to calculate the number of `1`-bits in a number. For this we use case analysis: 

 - If a number is divisible by 2, then it ends in zero. That means we can shift the entire number over by 1 by dividing by 2. We don't add anything to our running total; this step just shrinks the number so we progress towards termination.
 - Alternatively, if a binary number ends in 1, then it is not divisible by 2; we can subtract that one and operate as though the number was divisible by 2. 

We can also use bitwise operators and a simple parity check:

```{.python .numberLines startFrom="1" .neutral}
class Solution:
    def countBits(self, n: int) -> List[int]:

        memo = {0: 0, 1: 1}

        def ones(b):
            if b in memo: return memo[b]
            add = int(b % 2 == 1)
            memo[b] = add + ones(b >> 1)
            return (memo[b])
        
        return [ones(i) for i in range(n+1)]
```

But this solution is a little more terse and probably not that much faster than the previous solution.

## Missing Number

> Given an array `nums` containing $n$ distinct numbers in the range $[0, n]$, return the only number in the range that is missing from the array.

This is a simple $O(n \log(n))$ solution:

```{.python .numberLines startFrom="1" .bad}
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        for i,e in enumerate(nums):
            if e != i:
                return i
            
        return len(nums)
```

If we sort the array, then the numbers should all be present at their respective indices. If any one of them is incorrect, we can return the index -- that's what element is missing. If none of the indices are returned in the loop, the missing element must have been greater than the maximum element in `nums`: it must be `len(nums)`, which is the length of the complete array minus 1.

Here's another solution, using a `set` structure for $O(n)$ time complexity (but $O(n)$ space complexity as well):

```{.python .numberLines startFrom="1" .neutral}
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = set(nums)
        
        for i in range(len(nums+1)):
            if i not in seen:
                return i
```

There are two other solutions to this problem, each of which has $O(n)$ time complexity and only $O(1)$ space complexity. The first one relies on a mathematical fact.

Recall that: $$\sum_{i=1}^n i = \frac{n(n+1)}{2}$$

Here's a more efficient version, using that fact:

```{.python .numberLines startFrom="1" .good}
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) # this works with the zero-indexing
        
        should_be = n*(n+1)//2
        
        but_is = sum(nums) 
        
        return should_be - but_is 
```

The last version is the only one which uses bitwise operators; specifically, XOR:

```{.python .numberLines startFrom="1" .good}
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        out = 0
        for i in range(len(nums)):
            out = out ^ i ^ nums[i]
        return out ^ len(nums)
```

Here, we take advantage of the fact that XOR'ing identical elements will cancel them out. Thus, we are left with only the unique elements.

We could also do this using `fold_left` (aka `reduce` in Python), concatenating the relevant lists to combine all the elements:

```{.python .numberLines startFrom="1" .good}
from functools import reduce
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        def xor_fold(L): 
            return reduce(lambda x,y:x^y, L)
        return xor_fold(list(range(len(nums)+1)) + nums)
```

## Reverse Bits

> Reverse the bits of a given 32-bit unsigned integer.

Here is a simple solution:

```{.python .numberLines startFrom="1" .bad}
class Solution:
    def reverseBits(self, n: int) -> int:
        return int((bin(n).replace('0b','')[::-1] + '0' * (34-len(bin(n)))), 2)
```

This solution looks scary but is rather straightforward once you know what's going on. A better way to describe the process here is to use "functional pseudocode" and pipes:

```{.python .numberLines startFrom="1" .neutral}
n   |> bin                  # get the binary rep of n
    |> .replace('0b', '')   # remove the leading '0b' 
    |> [::-1]               # reverse the string
    |> + '0' * (34 - len(bin(n)))   # add necessary zeroes to get to 32 bits
    |> int(..., 2)          # convert the string back into decimal
```

The `34` comes from the fact that we want 32 bits, but the length of `bin(n)` contains the extra two characters `0b`.

Here's an $O(1)$ solution using bitwise operators:

```{.python .numberLines startFrom="1" .good}
# source: [Neetcode](https://www.youtube.com/watch?v=UcoN6UjAI64)
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res |= bit << (31 - i)
            
        return res
```

In this solution, `res` is our result. It's the binary reversal of `n`.

This code does the following:

 - [Line 3](#cb26-3): Initialize result to `0` (this is, in 32-bit binary, 32 zeroes)
 - [Line 4](#cb26-4): Iterate through all 32 bits of `n` with iteration variable `i`
   - On each iteration:
     - [Line 5](#cb26-5): Initialize `bit` to the value of the `i`th bit of `n`
     - [Line 6](#cb26-6): Set the `31 - i`th bit of `res` equal to `bit` (the `31 - i` part means that the order is reversed when copying `n` into `res`). Since `res` is initially all zeroes, bitwise OR'ing with `bit` will yield exactly `bit` in the desired position.

# Dynamic Programming

## Climbing Stairs

> You are climbing a staircase. It takes `n` steps to reach the top.
> 
> Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

This is a simple dynamic programming problem, and as such can be solved with memoization:

```{.python .numberLines startFrom="1" .good}
class Solution:
    def climbStairs(self, n: int) -> int:
        ways_to = {0 : 1, 1 : 1}
        
        def possibilities(n):
            if n in ways_to:
                return ways_to[n]
            
            one_step = possibilities(n-1)
            two_steps = possibilities(n-2)
            
            ways_to[n] = one_step + two_steps
            
            return ways_to[n]
        
        return possibilities(n)
```

This solution has time complexity $O(n)$. 

## Coin Change

> You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.
>
> Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.
>
> You may assume that you have an infinite number of each kind of coin.

This is another rather simple dynamic programming problem. The values we can memoize here are the amounts of coins that it takes to make each amount. Note that in this problem, as with the previous one and all dynamic programming problems, we store the best solution that we've found to a subproblem, because the problems overlap and the fact that the solution for the subproblem is optimal means that it is contained in the optimal solution to the entire problem.

```{.python .numberLines startFrom="1" .neutral}
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        fewest_to_make = {0 : 0}
        
        def make_change(n):
            if n in fewest_to_make:
                return fewest_to_make[n]
            
            fewest_list = [1 + make_change(n-c) for c in coins if n-c >= 0 and make_change(n-c) >= 0]
            
            if len(fewest_list) == 0:
                fewest = -1
            else:
                fewest = min(fewest_list)
            
            fewest_to_make[n] = fewest
            
            return fewest_to_make[n]
        
        return make_change(amount)
```

This solution is a little more readable, as it doesn't use a complicated list comprehension (and is better commented):

```{.python .numberLines startFrom="1" .good}
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        fewest_to_make = {0 : 0}
        
        def make_change(n):
            if n in fewest_to_make:
                return fewest_to_make[n]
            
            # get a list of ways to make n, taking the 
            # min of each possibilty for decreasing n
            # by some coin c
            fewest_list = []
            for c in coins:
                # can't subtract coin c from n
                if n-c < 0:
                    continue
                
                m = make_change(n-c)
                # aren't any ways to make n - c
                if m == -1:
                    continue
                    
                # we've found a way to make n
                # add 1 because we used a coin (c) to do so
                fewest_list.append(1 + m)
            
            if len(fewest_list) == 0:
                # there weren't any ways to make n
                fewest = -1
            else:
                # fewest coins possible to make n
                fewest = min(fewest_list)
            
            # update storage dictionary
            fewest_to_make[n] = fewest
            
            return fewest_to_make[n]
        
        return make_change(amount)
```

This solution has time complexity $O(n)$, where $n$ is the size of `amount`. 

## Longest Increasing Subsequence

> Given an integer array `nums`, return the length of the longest strictly increasing subsequence.
> 
> **Note**: A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, `[3,6,2,7]` is a subsequence of the array `[0,3,1,6,2,2,7]`.

This is a more difficult DP problem (in my opinion). Maybe I only had difficulty with it because I was assuming we had to do this in $O(n)$ time, but it was actually allowable to do it in $O(n^2)$ time. 

The difficult part is in that $O(n) \to O(n^2)$ translation. The added time complexity comes because of the fact that we need to remember more than just one piece of state information from the entire rest of the array; instead, we need to remember two pieces of state information from *each place in the array that we have seen so far*. 

Specifically, this is a combination of the length of the LIS (longest increasing subsequence) starting at that index, and the minimum element in that LIS. If the element we're currently examining is of a value greater than or equal to the minimum of some LIS, then our current element **cannot be added** to that subsequence (as it is no longer increasing).

This solution uses list comp and tuples within a list to make things more compact, but is not the most readable:

```{.python .numberLines startFrom="1" .bad}
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # go from LIS(n) -> LIS(n-1) by taking 
        # max(1, [1 + len(LIS(x)) where LIS(x) starts > nums[n-1]])

        longest_starting_here = [(0,0)]*len(nums)
        
        for i in range(len(nums)-1, -1, -1):         
            choices = [1] + [1 + lsh[0] for lsh in longest_starting_here[i:] if lsh[1] > nums[i]]
            
            longest_starting_here[i] = max(choices), nums[i]
        
        return max(longest_starting_here, key=lambda x : x[0])[0]
```

It also for some reason stores `nums[i]` as part of the tuple, which is completely unnecessary. Don't use that solution.

This is a much cleaner (and better-commented) solution (which does the same thing):

```{.python .numberLines startFrom="1" .good}
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # initialize data storage
        LIS = [0] * len(nums)
        
        # iterate backwards through the indices of nums
        # this range construct gives us [len(nums)-1, ..., 0]
        for i in range(len(nums)-1, -1, -1):         
            choices = [1] 
            
            # look at LIS already found
            for j,LIS_length in enumerate(LIS[i+1:]):
                # can only add this to choices if it's increasing
                if nums[j+i+1] > nums[i]:
                    choices.append(1 + LIS_length)
            
            LIS[i] = max(choices)
        
        return max(LIS)
```

This solution has time complexity $O(n^2)$, where $n$ is the size of `nums`. 

## Longest Common Subsequence

> Given two strings `text1` and `text2`, return the length of their longest common subsequence. If there is no common subsequence, return `0`.
> 
> A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
> For example, `"ace"` is a subsequence of `"abcde"`.
> 
> **Note**: A common subsequence of two strings is a subsequence that is common to both strings.

*This problem's solution was inspired by a [Neetcode video](https://www.youtube.com/watch?v=Ua0GhsJSlWM).*

This is a more difficult "2-dimensional" DP problem, which is best solved using a *matrix*. 

Take the example given, $t_1 = \texttt{"ace"}$ and $t_2 = \texttt{"abcde"}$. This should of course return 3, but we'll walk through it now using the matrix representation. 

Consider a matrix with the characters of $t_1$ along the columns and the characters of $t_2$ along the rows:
$$\begin{matrix} 
                & \texttt{a} & \texttt{c} & \texttt{e} \\
    \texttt{a}  &            &            &            \\
    \texttt{b}  &            &            &            \\
    \texttt{c}  &            &            &            \\ 
    \texttt{d}  &  & \color{red} \bullet \color{black} & \\    
    \texttt{e}  &            &            &            
\end{matrix}$$

The entries of this matrix will represent the size of the longest common subsequence of the substrings beginning at the characters which denote its position. For the position denoted by the red dot, for example, the contents of the entry at the position of the red dot would be the longest common subsequence of `ce` and `de` (and would therefore be `1`).

We can further say that the value of any entry just outside the matrix (on its bottom or right ends) will be `0`, as they correspond to the empty string, which only has common subsequences of length zero:
$$\begin{matrix} 
                & \texttt{a} & \texttt{c} & \texttt{e} & \\
    \texttt{a}  &            &            &            & 0 \\
    \texttt{b}  &            &            &            & 0 \\
    \texttt{c}  &            &            &            & 0 \\ 
    \texttt{d}  &            &            &            & 0 \\    
    \texttt{e}  &            &            &            & 0 \\
                & 0          & 0          & 0          & 0
\end{matrix}$$

Now we can start filling in the matrix. We will use the following recurrence relation, where $A_{i,j}$ corresponds to the matrix entry at row $i$ and column $j$, and $t_1^i$ and $t_2^j$ correspond to the $i$th and $j$th characters of $t_1$ and $t_2$ respectively:
$$A_{i,j} = \begin{cases}
    1 + A_{i+1, j+1}     & t_1^i = t_2^j \\
    \max(A_{i+1, j}, A_{i, j+1}) & \text{otherwise}
\end{cases}$$

In the above recurrence relation, if we see identical letters, then we increase the length of the common subsequence and continue along both strings at the same time (by incrementing both $i$ and $j$); otherwise, we take the maximum of the problems in which we increment $i$ and that in which we increment $j$, being analogues for shortening $t_1$ or $t_2$ by one character.

Running the above relation on the matrix, starting from the bottom up, yields the following result:
$$\begin{matrix} 
                & \texttt{a} & \texttt{c} & \texttt{e} & \\
    \texttt{a}  & 3          & 2          & 1          & 0 \\    \texttt{b}  & 2          & 2          & 1          & 0 \\
    \texttt{c}  & 2          & 2          & 1          & 0 \\ 
    \texttt{d}  & 1          & 1          & 1          & 0 \\    
    \texttt{e}  & 1          & 1          & 1          & 0 \\
                & 0          & 0          & 0          & 0
\end{matrix}$$

The following solution is a direct translation of the above algorithm (with the exception that it initializes all matrix entries to `0` beforehand, and performs some tricks to get the indices and elements exactly correct while iterating):

```{.python .numberLines startFrom="1" .good}
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        matrix = [[0 for j in range(len(text1)+1)] 
                     for i in range(len(text2)+1)]
        
        for i,ei in enumerate(text2[::-1]):
            i = len(text2) - i - 1
            for j,ej in enumerate(text1[::-1]):
                j = len(text1) - j - 1
                if ei == ej: # same letter
                    matrix[i][j] = 1 + matrix[i+1][j+1]
                else:
                    matrix[i][j] = max(matrix[i+1][j], matrix[i][j+1])
                    
        return matrix[0][0]
```

This solution has time complexity $O(n^2)$, where $n$ is the size of `text1` times the size of `text2`. 

## Word Break Problem

> Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.
> 
> **Note**: The same word in the dictionary may be reused multiple times in the segmentation.

This is another easy DP problem with simple memoization. Here, the subproblem is whether a substring of `s` beginning `len(w)` characters after the start of `s` can be segmented for some word `w`:

```{.python .numberLines startFrom="1" .good}
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        can_be_segmented = {'' : True}
        
        def can_segment(word) -> bool:
            if word in can_be_segmented:
                return can_be_segmented[word]
            
            w_removed = []
            for w in wordDict:
                if word.startswith(w):
                    w_removed.append(word[len(w):])
                    
            possible = any([can_segment(wr) for wr in w_removed])
        
            can_be_segmented[word] = possible
            return possible
        
        return can_segment(s)
```

This solution honestly probably doesn't require any comments. It's pretty straightforward.

This solution has time complexity $O(n)$, where $n$ is the size of `s`. 

## Combination Sum

> Given an array of distinct integers `nums` and a target integer `target`, return the number of possible combinations that add up to `target`.
> 
> The test cases are generated so that the answer can fit in a 32-bit integer.

For some reason this one took me forever to get, maybe because I kept messing up on small things and didn't work out an example beforehand. (**Note**: ALWAYS work out an example beforehand, just to make sure you know what you're doing.)

The following solution is actually rather simple, and is similar to previous problems:

```{.python .numberLines startFrom="1" .good}
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        min_num = min(nums)
        numset = set(nums)
        ways_to = {min_num : 1}
        
        def ways(n):
            if n in ways_to:
                return ways_to[n]
            
            if n in numset:
                found_ways = 1
            else:
                found_ways = 0
                
            for num in nums:
                res = n - num
                if res < min_num:
                    continue
                found_ways += ways(res)
            
            ways_to[n] = found_ways
            return found_ways
        
        return ways(target)
```

The interesting thing here is that we avoid all complications with zero by just saying that it doesn't exist, and making `min_num` the minimum number we allow ourselves to deal with. We also avoid zero by checking explicitly whether a number is in `nums` (to make this faster we cast `nums` to a `set`).

This solution has time complexity $O(n)$, where $n$ is the size of `target`. 

## House Robber

> You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
> 
> Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

This problem is an interesting application of DP, since the choice here is a bit more complex. You need to choose, at each index $i$, whether you want to take house $i$ and everything that is possible to take along with that house (this is $\texttt{nums}[i+2 \to]$), or the house $i+1$ next to it and everything that entails (so, $\texttt{nums}[i+3 \to]$). 

The nitpicky part here is checking whether `nums` is long enough to take the rest if possible. For small data ($n < 3$) we can just be greedy, as the invariant here is that we never make it possible to take two adjacent houses.

```{.python .numberLines startFrom="1" .good}
class Solution:
    def rob(self, nums: List[int]) -> int:
       
        best_choices = [-1]*(len(nums)-2) + [max(nums[-2:])] + [nums[-1]] 
        
        def get_nonadj_choices(i):
            if best_choices[i] != -1:
                return best_choices[i]
            
            if len(nums[i:]) <= 2:
                return max(nums[i:])
            
            if i + 2 >= len(nums):
                take_first = nums[i]
            else:
                take_first = nums[i] + get_nonadj_choices(i+2)
            
            if i + 3 >= len(nums):
                take_second = nums[i+1]
            else:
                take_second = nums[i+1] + get_nonadj_choices(i+3)
            
            best_choices[i] = max(take_first, take_second)
            
            return best_choices[i]
        
        return get_nonadj_choices(0)
```

Note further that this solution works because $\texttt{nums}[i] \geq 0 \;\; \forall i$. If this were not the case, we would have to change this solution (currently, we choose between taking house $i$ and house $i+1$; if we were working with negatives, we might not want to choose either).

This solution has time complexity $O(n)$, where $n$ is the size of `nums`. 

## House Robber II

> You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
> 
> Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

This problem is trivial if you have the solution to "House Robber I":

```{.python .numberLines startFrom="1" .neutral}
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) < 3:
            return max(nums)
        
        def rob1(nums):

            best_choices = [-1]*(len(nums)-2) + [max(nums[-2:])] + [nums[-1]] 

            def get_nonadj_choices(i):
                if best_choices[i] != -1:
                    return best_choices[i]

                if len(nums[i:]) <= 2:
                    return max(nums[i:])

                if i + 2 >= len(nums):
                    take_first = nums[i]
                else:
                    take_first = nums[i] + get_nonadj_choices(i+2)

                if i + 3 >= len(nums):
                    take_second = nums[i+1]
                else:
                    take_second = nums[i+1] + get_nonadj_choices(i+3)

                best_choices[i] = max(take_first, take_second)

                return best_choices[i]

            return get_nonadj_choices(0)
        
        return max(rob1(nums[1:]), rob1(nums[:-1]))
```

We literally just check whether it's best to take the first element or the last element. 

This solution has time complexity $O(n)$, where $n$ is the size of `nums`. 

I'm sure there's a "better", more "thoughtful" way to do this, but the above solution works and is easy to reason about. I don't see why anyone would do anything else.

## Decode Ways

> A message containing letters from A-Z can be encoded into numbers using the following mapping:
> 
> ```
> 'A' -> "1"
> 'B' -> "2"
> ...
> 'Z' -> "26"
> ```
> 
> To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, `"11106"` can be mapped into:
> 
>  - `"AAJF"` with the grouping `(1 1 10 6)`
>  - `"KJF"` with the grouping `(11 10 6)`
> 
> Note that the grouping `(1 11 06)` is invalid because `"06"` cannot be mapped into `'F'` since `"6"` is different from `"06"`.
> 
> Given a string `s` containing only digits, return the number of ways to decode it.
> 
> The test cases are generated so that the answer fits in a 32-bit integer.

This problem is similar to "Combination Sum", but even more similar to "Word Break". Like "Combination Sum", we start with a dictionary of "min values", each of which is initialized to `1` in our dictionary. Then, as in "Word Break", we iterate through possible "words" (checked for feasibility with the handy `.startswith()`), removing them from the string and seeing how many ways there are to make them. (The modification from "Word Break" here is that in "Word Break", we were only looking for `true` or `false` as to whether it was possible to create the string from words in the list provided.)

The solution is as follows:

```{.python .numberLines startFrom="1" .good}
class Solution:
    def numDecodings(self, s: str) -> int:
        num_ways = {str(n):1 for n in range(1,11)}
        num_ways[0] = 0
        
        def ways(s):
            if s in num_ways:
                return num_ways[s]
            
            total_ways = 0
            for i in range(1,27):
                si = str(i)
                if s.startswith(si):
                    if si == s:
                        total_ways += 1
                    else:
                        res = s[len(si):]
                        total_ways += ways(res)
                    
            num_ways[s] = total_ways
            return total_ways
        
        return ways(s)
```

This solution has time complexity $O(n)$, where $n$ is the size of `s`. 

## Unique Paths

> There is a robot on an `m` by `n` grid. The robot is initially located at the top-left corner (i.e., `grid[0][0]`). The robot tries to move to the bottom-right corner (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.
> 
> Given the two integers `m` and `n`, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
> 
> The test cases are generated so that the answer will be less than or equal to $2 \times 10^9$.

This one is trivial if you're familiar with combinatorics. Take the example `m = 1`, `n = 2`. The possible paths here are: 

```
DRR, RDR, RRD
```

If you have knowledge of combinatorics your eyes should be lighting up -- these are the permutations of $D^m R^n$! (The exclamation point is added for emphasis, not as a factorial.)

But we will be using a factorial here -- or rather, three of them. Note that the formula for permutations which maintain the same number of elements, of arrays with element types $e_1, \dots, e_n$ with quantities $r_1, \dots, r_n$, is as follows: 
$$|P| = \frac{\left(\sum_{i=1}^n r_i\right)!}{\prod_{j=1}^n (r_j!)}$$

In other words, we divide the factorial of the total number of elements by the factorials of each of the repetitions. For example, for permutations of `DRR` as above, we divide $3! = 6$ by $2! = 2$ to get $3$ (this is what we got above as well).

The solution is a simple translation of this:

```{.python .numberLines startFrom="1" .good}
from math import factorial
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return factorial(m+n-2)//(factorial(m-1) * factorial(n-1))
```

This solution has whatever time complexity Python's `Math.factorial` function is implemented in -- probably $O(n)$, if not slightly faster due to optimizations.

As with "House Robber II", I actually know for a fact that there's a more DP-oriented way to do this, but the above solution works and is easy to reason about. I don't see why anyone would do anything else, especially given how simple it is.

## Jump Game

> You are given an integer array `nums`. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
> 
> Return `true` if you can reach the last index, or `false` otherwise.

I went a little crazy on this one and decided to scrap the DP in favor of bit manipulation (my DP solution was failing for a 10,000-length list and I had no idea why it wasn't fast enough):

```{.python .numberLines startFrom="1" .bad}
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # initialize total to 0b1
        total = 1
        index = len(nums) - 1

        # go from right to left
        while index >= 0:       
            rindex = len(nums) - index
            value = nums[index]
            if value + index >= len(nums):
                # can go to the end -- put a '1' in bit <rindex>
                total |= 1 << (rindex - 1)
            else:
                # need to check whether it's possible to reach any ones so far
                # create as many ones in a row as there are possible jump locations
                ones = (1 << (value + 1)) - 1
                # shift these ones over to the desired location
                shifted = ones << (rindex - value - 1)
                # check for intersection
                if total & shifted > 0:
                    # put a '1' in this bit (if we don't do this, it stays a '0' as desired)
                    total |= 1 << (rindex - 1)
            index -= 1

        # get location of bit that tells us whether the first index can jump to the last index
        zero_index = 1 << (len(nums) - 1)

        # return true if total has a '1' at the zero index
        return total & zero_index > 0
```

I don't recommend that you use this solution. It really violates the spirit of the problem, especially given that the problem is literally in the DP section.

This solution has time complexity $O(n)$, where $n$ is the size of `nums`. 

# Graph

## Clone Graph

> Given a reference of a node in a connected undirected graph.
> 
> Return a deep copy (clone) of the graph.
> 
> Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors:
> 
> ```java
> class Node {
>     public int val;
>     public List<Node> neighbors;
> }
> ```

We use a DFS (depth-first search) and an internediate representation as an adjacency dictionary as follows:

```{.python .numberLines startFrom="1" .neutral}
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # return empty if given empty
        if node == None:
            return None
        
        # initialize data storage
        # use dict for adj list because we don't 
        # know the graph size yet
        seen = []
        adj_dict = {}
        
        def dfs(n):
            seen.append(n.val)
            
            neighbor_vals = []
            
            for neighbor in n.neighbors:
                if neighbor.val not in seen:
                    dfs(neighbor)
                neighbor_vals.append(neighbor.val)
                
            adj_dict[n.val] = neighbor_vals
        
        # populate adjacency dict
        dfs(node)
    
        # build new graph

        # create a node for each value found
        nodes = [Node(val=v) for v in range(1, len(adj_dict) + 1)]

        # update nodes' neighbors according to adj dict
        for node_index in range(len(nodes)): 
            node = nodes[node_index]
            neighbors = []
            for neighbor_val in adj_dict[node.val]:
                neighbors.append(nodes[neighbor_val - 1])
            node.neighbors = neighbors
        
        return nodes[0]
```

There might be a way to do this with a lower space complexity, i.e. by creating the copy *during* the DFS instead of after it, but this solution is perfectly functional.

This solution has time complexity $O(m \cdot n)$, where $n$ is the size of the graph and $m$ is the width of the graph's representative adjacency list; that is, the maximum number of neighbors that a node has. 

## Course Schedule

> There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [`$a_i$`, `$b_i$`]` indicates that you must take course $b_i$ first if you want to take course $a_i$.
> 
> For example, the pair `[0, 1]`, indicates that to take course 0 you have to first take course `1`.
> 
> Return `true` if you can finish all courses. Otherwise, return `false`.

This problem asks us to look for a cycle in the graph. We can do this via topological sort, which is described as follows (in Python-like pseudocode):

```python
while size(graph) > 0:
    removable nodes = []
    for node in graph:
        if number_of(in_edges(node)) = 0:
            add node to removable nodes
    
    if number_of(removable nodes) = 0:
        return False
    
    for node in removable nodes:
        remove node from graph

return True
```

By going through the courses, iteratively removing any nodes with no prerequisites, we effectively conduct a topological traversal of the graph. Whatever subgraph obstructs the algorithm (at which time the number of removable courses is `0`) contains a cycle, which means that we can return `false`.

Here is a solution:

```{.python .numberLines startFrom="1" .good}
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:   
        # create better version of the graph
        prq = {i : set() for i in range(numCourses)}
        for p in prerequisites:
            prq[p[1]].add(p[0])
        
        # do topological sort
        while len(prq) > 0:
            pop = {k for k,v in prq.items() if len(v) == 0}
            for k in pop:
                prq.pop(k)
            for k,v in prq.items():
                prq[k] = v - pop
            if len(pop) == 0:
                return False
        
        return True
```

This solution runs in $O(m+n)$ time, where $m$ is the size of `numCourses` and $n$ is the size of `prerequisites`. 

## Pacific Atlantic Water Flow
## Number of Islands
## Longest Consecutive Sequence
## Alien Dictionary (Leetcode Premium)
## Graph Valid Tree (Leetcode Premium)
## Number of Connected Components in an Undirected Graph (Leetcode Premium)

# Interval

## Insert Interval
## Merge Intervals
## Non-overlapping Intervals
## Meeting Rooms (Leetcode Premium)
## Meeting Rooms II (Leetcode Premium)

# Linked List

## Reverse a Linked List
## Detect Cycle in a Linked List
## Merge Two Sorted Lists
## Merge K Sorted Lists
## Remove Nth Node From End Of List
## Reorder List

# Matrix

## Set Matrix Zeroes
## Spiral Matrix
## Rotate Image
## Word Search
 
# String

## Longest Substring Without Repeating Characters
## Longest Repeating Character Replacement
## Minimum Window Substring
## Valid Anagram
## Group Anagrams
## Valid Parentheses
## Valid Palindrome
## Longest Palindromic Substring
## Palindromic Substrings
## Encode and Decode Strings (Leetcode Premium)

# Tree

## Maximum Depth of Binary Tree
## Same Tree
## Invert/Flip Binary Tree
## Binary Tree Maximum Path Sum
## Binary Tree Level Order Traversal
## Serialize and Deserialize Binary Tree
## Subtree of Another Tree
## Construct Binary Tree from Preorder and Inorder Traversal
## Validate Binary Search Tree
## Kth Smallest Element in a BST
## Lowest Common Ancestor of BST
## Implement Trie (Prefix Tree)
## Add and Search Word
## Word Search II

# Heap

## Merge K Sorted Lists
## Top K Frequent Elements
## Find Median from Data Stream


<script>
//Get the button
var mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}
</script>