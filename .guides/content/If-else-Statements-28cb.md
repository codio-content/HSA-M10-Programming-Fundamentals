The `IF-ELSE` instruction allows there to be more than two paths through an program. Any number of `IF-ELSE` instructions can be added to an program. It is used along with other instructions:

`IF` represents a question
`THEN` points to what to do if the answer to the question is true
`IF-ELSE` represents another question
`THEN` points to what to do if the answer to that question is true
`IF-ELSE` represents another question
`THEN` points to what to do if the answer to that question is true
`ELSE` points to what to do if the answer to the question is false

Using the if-else method, the grades algorithm could be improved like this:

1. Ask what your grade percentage is
2. `IF` you're grade is greater than or equal to 90, `THEN` print 'A'
3. `ELSE IF` you're grade is greater than or equal to 80, `THEN` print 'B'
4. `ELSE IF` you're grade is greater than or equal to 70, `THEN` print 'C'
5. `ELSE IF` you're grade is greater than or equal to 60, `THEN` print 'D'
6. `ELSE` print 'F'

If you try this algorithm using 80 as your grade, the answer to the question at step 3 is true, so the algorithm prints out your letter grade as 'B'. 

If you use 50 as your grade, each step is processed until the end of the program and your letter grade is printed as 'F'. 

![Grades.jpg](https://insect-method.codio.io/Grades.jpg)




