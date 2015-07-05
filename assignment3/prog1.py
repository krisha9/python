# program to perform append and extend operation on list

L_1 = [9, 10, 11, '&', "python"]
L_2 = ["django", '@', [4, 5, 6, 'K']]

print("\nlist 1 is:", L_1)
print("\nlist 2 is:", L_2)

L_1.append(L_2)
print("\nperforming append operation on list 1:", L_1)

#performing extend operation on list 1
L_1 = [9, 10, 11, '&', "python"]
L_1.extend(L_2)
print("\nperforming extend operation on list 1:", L_1)
