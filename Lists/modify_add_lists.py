#how to add element to lists
#how to modify elements in the lists

#example1
#added by @engshorouq
#create empty list
my_list=[]

#add element to empty string in two ways the first way(append)
my_list.append("Learn")
my_list.append(["Pythn","Language"])

#print list to show the output

print("list after adding iteam using append : \n",my_list)


#add element to my list by second way : using + operator
my_list=my_list+["version"]
my_list=my_list+[3]
my_list=my_list+["interting","language"]

#print list to show output
print("\nlist after adding iteam using append : \n",my_list)

#mistake in writing word inside list
#modify 1st iteam
my_list[0]="Learning"
#modify 2nd item the 1st item inside it
my_list[1][0]="Python"
#modify 3rd to 5th item
my_list[2:5]=["version 3","intersting","language"]

#print list to show output
print("\nlist after modification : \n",my_list)
