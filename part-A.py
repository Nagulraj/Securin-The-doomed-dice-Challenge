#part-A (i)

def possible_combinations(adice,bdice):
    result=0
    for i in adice:
        for j in bdice:
            result+=1
    return result

adice=[1,2,3,4,5,6]
bdice=[1,2,3,4,5,6]
no_of_combinations=possible_combinations(adice,bdice)
print("part-A (i)")
print("Total number of Possible Combinations are:",end="")
print(no_of_combinations)
print()


#part-A (ii)


def distribution_of_combinations(adice, bdice):
    matrix=[[] for i in range(6)]
    for i in adice:
        for j in bdice:
            each_throw=(i,j)
            matrix[i-1].append(each_throw)
    return matrix


matrix=distribution_of_combinations(adice, bdice)

print("part-A (ii)")

print("All Possible Combinations are:")
# print(matrix)
for combinations in matrix:
    for combination in combinations:
        print(combination,end=" ")
    print()

print()





#part-A (iii)





prob_sum={}
for combinations in matrix:
    for combination in combinations:
        combination_sum=sum(combination)
        if combination_sum not in prob_sum:
            prob_sum[combination_sum]=1
        else:
            prob_sum[combination_sum]+=1
print("part-A(iii)")

for combination_sum in prob_sum.keys():
    print(f"the probability of the sum {combination_sum} is {prob_sum[combination_sum]}/36")


