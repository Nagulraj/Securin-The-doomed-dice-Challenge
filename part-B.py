possible_die_faces_a = [0,1,2,3,4]
possible_die_faces_b = [1,2,3,4,5,6,7,8]
total_spots = 42
original_sum_probabilities = {2: 1, 4: 3, 5: 4, 6: 5, 7: 6, 9: 4, 3: 2, 8: 5, 10: 3, 11: 2, 12: 1}

def die_a_combinations(current_die, valid_combos_die_a):    
  if len(current_die) == 6:
    valid_combos_die_a.append(current_die)
    return
    
  for face in possible_die_faces_a:
    die_a_combinations(current_die+[face], valid_combos_die_a)    


def die_b_combinations(previous_face_index, current_die, current_spot_count, valid_combos_die_b):
  if (current_spot_count > total_spots):
    return
    
  if len(current_die) == 6:
    if current_spot_count == total_spots:
      valid_combos_die_b.append(current_die)
    return
    
  for i in range(previous_face_index+1, len(possible_die_faces_b)):
    die_b_combinations(i,current_die+[possible_die_faces_b[i]], current_spot_count + possible_die_faces_b[i], valid_combos_die_b)

def calculate_dice_probabilities(die_a, die_b):
  prob = {}
  for die_face_a in die_a:
    for die_face_b in die_b:
      if die_face_a+die_face_b in prob:
        prob[die_face_b+die_face_a]+=1
      else:
        prob[die_face_b+die_face_a]=1
      
  return prob

def is_valid_dice(die_a, die_b):
  new_probabilities = calculate_dice_probabilities(die_a, die_b)
  return new_probabilities == original_sum_probabilities
 
def undoom_dice(die_a, die_b):
  valid_combos_die_a = []
  die_a_combinations([], valid_combos_die_a)

  for die_combination_a in valid_combos_die_a:
    valid_combos_die_b = []
    die_b_combinations(-1, [], sum(die_combination_a), valid_combos_die_b)
    for die_combination_b in valid_combos_die_b:
      if is_valid_dice(die_combination_a, die_combination_b):
        print("New_Die_A = ", die_combination_a)
        print("New_Die_B = ", die_combination_b)
        return

  print("No valid dice combination exists")

die_a=[1,2,3,4,5,6]
die_b=[1,2,3,4,5,6]
undoom_dice(die_a,die_b)