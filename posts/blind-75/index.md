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
## Coin Change
## Longest Increasing Subsequence
## Longest Common Subsequence
## Word Break Problem
## Combination Sum
## House Robber
## House Robber II
## Decode Ways
## Unique Paths
## Jump Game

# Graph

## Clone Graph
## Course Schedule
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