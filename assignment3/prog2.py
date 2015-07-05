# a03p02a.py
l1 = [p for p in range(1, 11)]
print("l1 : ", l1)


#​a03p02b.py
l2 = [q for q in range(10, 101, 10)]
print("\nl2 : ", l2)

# a03p02c.py
l3 = ["python", "django", "flask", "string", "function", "classes"]
print("\nl3 :", l3, "\n")

# a03p02d.py

l4=[]
d1= {"l1": l1}
d2={"l2":l2}
d3={"l3":l3}
l4=[d1,d2,d3]
print("l4 is a list of dictionaries=", l4)


# a03p02e.py

main_list1 = []
main_list1.append(l1)
main_list1.append(l2)
main_list1.append(l3)

print("\nMain list with list l1,l2 ,l3 using append is:", main_list1)


main_list2 = []
main_list2.extend(l1)
main_list2.extend(l2)
main_list2.extend(l3)
print("\nMain list with list l1,l2 ,l3 using extend is:", main_list2)


# a03p02f.py

l5 = l1 * 2
print("\nl5 :", l5)


# a03p02g.py

main_list1.append(l5)
print("\n After appending list 5 to the main list: ")
print(main_list1)

# a03p02h.py

print("\noccurence of the integer 1 in appended  main_list is:", main_list1.count(1), "\noccurence of integer 1 in extended mainlist is:",
      main_list2.count(1))
