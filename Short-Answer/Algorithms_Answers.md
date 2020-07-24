#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) I believe this is an O(n). There is a linear increase with every step, since the algorithm
iterations reflect n directly. If n = 2, the loop will run 2 times. If n = 5, the loop
would run 5 times. This happens on and on  


b) The runtime for this problem I believe is O(nlogn). The first for loop, we are iterating through all of n, 
so that would be O(n). The while loop, as n increases, the number of operations increases, but not linearly.
For n = 5-8, the while loop runs three times, for n = 9-16, the while loop runs 4 times. The operations are increasing, 
but at a slower rate than O(n). So this would be log n. O(n) * O(log n) gives you O(n log n). 
 As n goes up, the sum is larger than n, but smaller than n^2.

c) In it's current form runtime is O(1), since it's returning a constant value and not looping over anything. 
The runtime would be O(n). Since iterations would follow a linear line. This works similar to the factorial problem I think. 
Whatever your n is, you recur n times (because base case is bunnies == 0 and not bunnies == 1).  So you are always going to have 
the one base case operation, plus n recursions. 

## Exercise II

I would take a binary search approach to solve this problem. 
 Assuming ground floor is 0, and you have a 6 story building, start in the middle on the 3rd floor. Throw off an egg. If it cracks, you know you are higher than floor f. Let's say it cracks. Then you would assume floor 2 in the top of the building, and floor 0 is still the bottom. The middle floor at that point is now floor 1. You throw it off and it doesn't crack, you know floor 2 is floor f. If it does crack, floor 1 or floor 0 could be floor f so you would need to try tossing an egg one more time. 

 Runtime complexity I believe is O(logn)
