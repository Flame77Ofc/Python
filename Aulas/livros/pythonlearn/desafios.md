1. Write a for loop that prints out the integers 2 through 10, each on
a new line, using range().
2. Write a while loop that prints out the integers 2 through 10. (Hint:
You’ll need to create a new integer first.)
3. Write a function called doubles() that takes a number as its input
and doubles it. Then use doubles() in a loop to double the number 2
three times, displaying each result on a separate line. Here’s some
sample output:
4
8
16





1. Using break, write a program that repeatedly asks the user for some
input and quits only if the user enters "q" or "Q".
2. Using continue, write a program that loops over the numbers 1 to
50 and prints all numbers that are not multiples of 3.



1. Create a tuple literal named cardinal_numbers that holds the strings
"first", "second", and "third", in that order.
2. Using index notation and print(), display the string at index 1 in
cardinal_numbers.
3. In a single line of code, unpack the values in cardinal_numbers into
three new strings named position1, position2, and position3. Then
print each value on a separate line.
4. Using tuple() and a string literal, create a tuple called my_name that
contains the letters of your name.
5. Check whether the character "x" is in my_name using the in keyword.
6. Create a new tuple containing all but the first letter in my_name using
slice notation.

1. Create a list named food with two elements, "rice" and "beans".
2. Append the string "broccoli" to food using .append().
3. Add the strings "bread" and "pizza" to food using .extend().

4. Print the first two items in the food list using print() and slice no-
tation.

5. Print the last item in food using print() and index notation.
6. Create a list called breakfast from the string "eggs, fruit, orange
juice" using the string .split() method.
7. Verify that breakfast has three items using len().

8. Create a new list called lengths using a list comprehension that con-
tains the lengths of each string in the breakfast list.




1. Create a tuple called data with two values. The first value should
be the tuple (1, 2), and the second value should be the tuple (3,
4).
2. Write a for loop that loops over data and prints the sum of each
nested tuple. The output should look like this:
Row 1 sum: 3
Row 2 sum: 7
3. Create the list [4, 3, 2, 1] and assign it to the variable numbers.
4. Create a copy of the numbers list using the [:] slice notation.
5. Sort the numbers list in numerical order using .sort().


100000. Challenge: List of lists
Write a program that contains the following lists of lists:
universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]
Define a function, enrollment_stats(), with a single parameter. This
parameter should be a list of lists in which each individual list contains
three elements:
1. The name of a university
2. The total number of enrolled students
3. The annual tuition fees
enrollment_stats() should return two lists, the first containing all the
student enrollment values and the second containing all the tuition
fees.
Next, define two functions, mean() and median(), that take a single list
argument and return the mean or median of the values in each list,
respectively.
Using universities, enrollment_stats(), mean(), and median(), calculate
the total number of students, the total tuition, the mean and median
numbers of students, and the mean and median tuition values.
Finally, output all values and format the output so that it looks like
this:
******************************
Total students: 77,285
Total tuition: $ 271,905
Student mean: 11,040.71
Student median: 10,566
Tuition mean: $ 38,843.57
Tuition median: $ 39,849
******************************




1. Create an empty dictionary named captains.
2. Using square bracket notation, enter the following data into the
dictionary one item at a time:
• 'Enterprise': 'Picard'
• 'Voyager': 'Janeway'
• 'Defiant': 'Sisko'
3. Write two if statements that check if "Enterprise" and "Discovery"
exist as keys in the dictionary. Set their values to "unknown" if the
key does not exist.
4. Write a for loop to display the ship and captain names contained
in the dictionary. For example, the output should look something
like this:
The Enterprise is captained by Picard.
5. Delete "Discovery" from the dictionary.
6. Bonus: Make the same dictionary by using dict() and passing in
the initial values when you first create the dictionary.

1. Create a list with the names of friends and colleagues. Calculate the average length of the names.

2. Create a list with the names of friends and colleagues. Search for the name John using a for loop. Print not found if you didn't find it. (Hint: use else).

3. Create a list of tuples of first name, last name, and age for your friends and colleagues. If you don't know the age, put in None. Calculate the average age, skipping over any None values. Print out each name, followed by old or young if they are above or below the average age.

1. Create a variable, age, set to your age. Create another variable, old, that uses a condition to test whether you are older than 18. The value of old should be True or False.

2. Create a variable, name, set to your name. Create another variable, second_half, that tests whether the name would be classified in the second half of the alphabet? What do you need to compare it to?

3. Create a list, names, with the names of people in a class. Write code to print 'The class is empty!' or 'Class has enrollments.', based on whether there are values in names. (See the tip in this chapter for details).

4. Create a variable, car, set to None. Write code to print 'Taxi for you!', or 'You have a car!'. based on whether or not car is set (None is not the name of a car).