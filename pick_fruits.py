"""
904. Fruit Into Baskets
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.


Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
"""


def totalFruit(self, fruits) -> int:
        while r<len(fruits):
            window=(r-l)+1
            size=max(size,window)    
            if fruits[l]!=fruits[r] and fruits[r-1]!=fruits[r] and (r-l)>1:
                l+=1
            else:
                r+=1
        return size
    
"""
Explanation:

Obvious solution is using hashmap to track the frequency of any two bucket.
But I've tried solving this code without using hashmap. Suprisingly this solution
does gives the right output for half of the test cases. 

Still this approach fails for cases like alternate numbers [1,2,1,2,1,2].
"""
