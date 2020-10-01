# Here we will show sorting in lists
# Lists have 2 main methods for sorting - sort and sorted
# added by jagritvats
# sort methods sorts the lists while sorted method does not modify the list but returns the sorted lists

li=[7,3,9,1,0] 
print(li)
li.sort()
print(li) # we can see li has become sorted


print()


li=[2345,678,2134,7687]
print(li)
li2=sorted(li) # the returned value i.e. sorted list is stored in li2
print(li2) # sorted list
print("\n Original List:")
print(li) # we can see here original list is unchanged

print('Reverse Sorted:')
li3=sorted(li,reverse=True) # reverse parameter sorts by descending order
print(li3)
