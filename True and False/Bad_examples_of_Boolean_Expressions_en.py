#Bad examples of boolean expressions:
#added by Heba-Ahmad
#These are Bad examples of Boolean expressions that should be avoided 
#Bad Example 1
if True:
#this example shows that True and False are both Boolean but using true or false is useless in a conditional expression as
#they are always True or false.  An 'if True:' or an 'if False' in Python simply means that
#the code in this block will always execute.
#Having an 'if True:' is as good as having no if block. For example, the code:
    if True:
        x = "ok"
        print (x)

#Is the same as the code:
x = "ok"
print (x)

#Furthermore, we need to keep in mind that in case if True: statement has a following 'else block', then that else block will never be executed.
#Example:
if True:
    print 'I will always be printed!'
else:
#Unreachable code, will never be executed.
    print 'I will never get a chance...'

#True and False are both Boolean, but using 'if True:' or 'if False:' is not a good practice and should be avoided.

#Bad Example 2:
#Boolean operators AND, OR, and NOT have a specific meanings that are'nt quite the same as their common meanings. For example:
is_delicious= True
if is_delicious or not is_delicious:
    print("The dinner is either delicious or not delicious.")
#Here is_delicious or not is_delicious, will always evaluate to True. it is useless in a conditional expression, because the indented code will always get run.

#Bad Example 3:

something = "c"
if something == "a" or "b":
  print "ok"
else:
  print "not ok"

#This is not a boolean expression, the expression to the right of the OR is not a boolean expression -it's a string!-.
#This code is valid python though, it doesn't produce an error when run
if something == "a" or "b":
    print "ok"
#is logically equivalent to:
if (something == "a") or ("b"):
    print "ok"
#Which, for the value "c", is equivalent to:
if (False) or ("b"):
    print "ok"
#The or operator chooses the first argument with a positive truth value:
if ("b"):
    print "ok"
#And since "b" has a positive truth value, the if block executes.
#That is what causes "ok" to be printed regardless of the given value of something which is "c".

#All of this reasoning also applies to the expression
if "a" or "b" == something:
    print something
#the first value, "a", is true, so the if block executes.

#correct example3:
#There are two common ways to properly construct this conditional:
#- First way by using multiple == operators to explicitly check against each value:
if something == "a" or something == "b":
    print something
#- Second way by composing a sequence of valid values, and use the in operator to test for membership:
if something in ("a", "b"):
    print something

#Bad Example 4:
#Do not compare a variable that is a boolean with == True or == False - it's more readable to avoid such a comparison:
if something == True:
    print "ok"
#This one is a valid conditional expression, but we could (and should) express the conditional more briefly and more clearly.
# If something is equal to True, then it is a boolean expression in its own right we can make the code more readable by instead using:

#Better example 4:
if something:
    print "something is Ture"

#If you want to check whether a boolean is False, you can use NOT, for example
if not something:
  print "something is Ture"
else:
  print "something is False"
#output:
#>>> something is False

#If we put some other object that is not a boolean in the if statement
#in place of the boolean expression, for example: "if something:" in "Better example 4"
#Python will check for its truth value and use that to decide whether or not to run the indented code.

#Below is a table with examples of the truth values of various objects:
table= """
         True           |        False
--------------------------------------------
True                    | False
--------------------------------------------
1                       | 0
--------------------------------------------
Numbers other than zero	| The string 'None'
--------------------------------------------
Nonempty strings        | Empty strings
--------------------------------------------
Nonempty lists          | Empty lists
--------------------------------------------
Nonempty dictionaries   | Empty dictionaries
"""
print "Table with examples of the truth values of various objects:" ,table
