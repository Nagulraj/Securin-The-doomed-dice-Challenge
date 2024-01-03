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


