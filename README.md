# Securin-The-doomed-dice-Challenge
answers for the second level of assessment

                                        PART-A

part-A (i)

Two nested for loops—one for iterating over the values of adice and another for generating corresponding values of bdice for each adice value. Introduce a count variable to keep track of the total possibilities, ie 36

part-A (ii)

similar to previous part we use two nested loops to find all the possible combination ,declare a 2 D matrix 6X6  where eachthrow of dice a and dice b is stored as tuple and the tuple is appended to the matrix.This way a 6X6 matrix is created with all the possibilities.

To print each possibilities we use two nested loops 

part-A (iii)

we use the matrix generated in the previous step,we have to find the sum of the each throw,
we use two nested loops to get tuple. declare a dictionary to store the probablility of each sum,find each sum and store it in the dicitonaryto keep track of the sum occurances.



                                        PART-B
                                Functions-Description
die_a_combinations(current_die, valid_combos_die_a):
            This function generates all possible combinations of Die A, and it is called with an empty list for the current combination and an empty list for storing valid combinations.

die_b_combinations(previous_face_index, current_die, current_spot_count, valid_combos_die_b):
            This function generates all possible combinations of Die B, given the previous face index, the current combination, the current spot count, and a list for storing valid combinations .

calculate_dice_probabilities(die_a, die_b):
            This function calculates the probabilities of all possible sums for a given combination of Die A and Die B.

is_valid_dice(die_a, die_b):
            This function checks whether the given combination of Die A and Die B produces the same sum probabilities as the original set.

undoom_dice(die_a, die_b):
            This function generates all combinations of Die A and Die B and checks if any of them is valid. If a valid combination is found, it prints the new combinations; otherwise, it prints a message indicating that no valid combination exists.


                                Actual Execution Steps

->An empty list valid_combos_die_a is initialized.
->The die_a_combinations function is called with an empty current die ([]) and the empty list to store valid combinations (valid_combos_die_a).
->This recursive function generates all combinations of Die A and appends them to the valid_combos_die_a list.
->Iterates over all valid combinations of Die A 
->Then in a similar way, we are finding the Die B combinations
->Iterates through the combinations of Die B
->Then we check if the current combination of Die A and Die B produce the same probability.
->If current combination is valid then we print the die A and Die B combination and return the function
 
                                        Approach
In die_a_combinations and die_b_combinations
            To find all the possible combinations of both dice I use recursion. This is bruteforce technique to find the combinations.
        
                                        Assignments
possible_die_faces_a = [0,1,2,3,4]
            Since from the given the maximum value that the Die A can hold is 4. so the list contains all the possible values upto 4. 
        
possible_die_faces_b = [1,2,3,4,5,6,7,8]
            The maximum probability sum is 12 and from the previous point we can see the that the maximum value Die A can hold is 4.So with this we can say that maximum possible value in Die B is 8.So it has all the values with in 8.

total_spots = 42
            The sum of the spots in Die A is 21 ie n(n+1)/2 6(6+1)
            The sum of the spots in Die B is 21 ie n(n+1)/2 6(6+1)
These spots will be later doomed by Loki.But the spots count stays the same.

original_sum_probabilities = {2: 1, 4: 3, 5: 4, 6: 5, 7: 6, 9: 4, 3: 2, 8: 5, 10: 3, 11: 2, 12: 1}

    The above is  probability sum of the old dice A and old Dice B

            old Die A = [1,2,3,4,5,6]
            old Die B = [1,2,3,4,5,6]


                                         Answer
    
The New combination of Die A and Die B with same old Probability Sum is

        New Die A=[1,2,2,3,3,4]
        New Die B=[1,3,4,5,6,8]
            



