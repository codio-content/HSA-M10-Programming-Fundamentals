A **condition** is a situation that is checked every time an **iteration** occurs.

The condition, in our tooth brushing program, will be to check if the number of teeth cleaned equals ten. If that condition is False (the number of teeth cleaned is less than ten), then another iteration occurs. If the condition is True (the number of teeth cleaned equals ten), then no more iterations occur.

|||warning 
It is also important to keep a count of how many teeth have been cleaned.
|||

A **counter** is used to do this.  The counter can be used to see if the condition has been met. This is known as **testing the condition**. The test sees whether the condition is True or False.

If a condition and a counter are included, the updated algorithm would look like this:

1. set number_of_teeth_cleaned to 0
2. put toothpaste on toothbrush
3. use toothbrush to clean a tooth
4. increase number_of_teeth_cleaned by 1
5. if number_of_teeth_cleaned < 10 then go back to step 3
6. rinse toothbrush

The counter is called `number_of_teeth_cleaned` , and the condition is `if number_of_teeth_cleaned < 10`. 

Using iteration, the number of steps has reduced from 12 in the first teeth-cleaning algorithm to just six in the algorithm with iteration.

This is very similar to selection as two routes are created. However, with iteration there is a loop back into the program, rather than creating and keeping two separate routes as would occur with selection.

We explore selection further in the next section. 


