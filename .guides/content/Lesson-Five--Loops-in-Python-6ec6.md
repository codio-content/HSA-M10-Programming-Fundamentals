## Why is iteration important?
Iteration allows programs to be simplified by stating that certain steps will repeat until told otherwise. This makes designing programs quicker and simpler because they don’t need to include lots of unnecessary steps.


### Example Algorithm: Brushing Your Teeth
Let's go back to our teeth brushing algorithm. 

A simple algorithm can be created for cleaning teeth. Suppose a person has ten top teeth. To make sure that every one of the top teeth is cleaned, the algorithm would look something like this:

1. put toothpaste on toothbrush
2. use toothbrush to clean tooth 1
3. use toothbrush to clean tooth 2
4. use toothbrush to clean tooth 3
5. use toothbrush to clean tooth 4
6. use toothbrush to clean tooth 5
7. use toothbrush to clean tooth 6
8. use toothbrush to clean tooth 7
9. use toothbrush to clean tooth 8
10. use toothbrush to clean tooth 9
11. use toothbrush to clean tooth 10
12. rinse toothbrush


The flode chart on the left makes it easy to see that steps 2 through to 11 are essentially the same step repeated, just cleaning a different tooth every time. **Iteration can be used to greatly simplify the algorithm**. Look at this alternative:

1. put toothpaste on toothbrush
2. use toothbrush to clean a tooth
3. move onto next tooth
4. repeat steps 2 and 3 until all teeth are clean
5. rinse toothbrush


Click to view the updated flode chart. 
[BruthTeethLoop.flode](open_file "BrushTeethLoop.flode")


This algorithm is much simpler and only contains 5 instructions rather than 12.  

However, there is a problem:  How do we know when all teeth are clean (step 4)? A **condition** is needed to solve this problem.







