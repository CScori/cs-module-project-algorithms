'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
'''
UNDERSTAND
i have a list
the list will always contain 1 unique element
i need to loop (while or for)
i need to check each number to see if it has a match (for)
i want to go over the loop once
constant tim big 0 
PLAN
based on the function i want to set pointer params
i then want to check if they are equal
if statement to check ifits a repeat // false
if no match return the number
REVIEW
used a param to set to 0 
(initially thought to increment but changed mind) runs o(n)
used for loop to go through arr
set doubles to log fn. (was going to increment but based on research found bit operators)
the ^ changes the values of double from 0 to 1 if there is more than one element
the log then leaves only the single element
return the single element

'''
def single_number(arr):
    # Your code here
    doubles = 0
    
    for odd_out in arr:
        doubles = (doubles ^ odd_out)
    return doubles


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")