# codefight
There are some tasks that I think I need to note  down
</br>
</br>
**#areSimilar.py
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.
Given two arrays a and b, check whether they are similar.**
Example
For a = [1, 2, 3] and b = [1, 2, 3], the output should be
areSimilar(a, b) = true.
The arrays are equal, no need to swap any elements.
For a = [1, 2, 3] and b = [2, 1, 3], the output should be
areSimilar(a, b) = true.
We can obtain b from a by swapping 2 and 1 in b.
For a = [1, 2, 2] and b = [2, 1, 1], the output should be
areSimilar(a, b) = false.
Any swap of any two elements either in a or in b won't make a and b equal.
</br>
</br>
**#adjacentElementsProduct
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.**
Example
For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.
7 and 3 produce the largest product.

</br>
**reverseInParentheses
Write a function that reverses characters in (possibly nested) parentheses in the input string.
Input strings will always be well-formed with matching ()s.**

Example
For inputString = "(bar)", the output should be
reverseInParentheses(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be
reverseInParentheses(inputString) = "foorabbaz";
For inputString = "foo(bar)baz(blim)", the output should be
reverseInParentheses(inputString) = "foorabbazmilb";
For inputString = "foo(bar(baz))blim", the output should be
reverseInParentheses(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
