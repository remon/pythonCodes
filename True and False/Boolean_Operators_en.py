#This file contines a definition and some examples of how to use Boolean Operators
# what is Boolean operators?
#Boolean Operators compare statements and result in boolean values. There are three boolean operators(AND, OR, and NOT):
#1-and, checks if both the statements are True; 2-or, checks if at least one of the statements is True;
#3-not, gives the opposite of the statement.
#the table bellow shows the results of using AND, OR, and NOT boolean operators:
#Boolean operators aren't just evaluated from left to right. Just like with arithmetic operators, there's an order of operations for boolean operators:
#1-not is evaluated first; 2-and is evaluated next; 3-or is evaluated last.
boolean_operator= {"row1 c1": "  A  ", "row1 c2": "  B  ", "row1 c3": "A AND B", "row1 c4": "     ", "row1 c5": "  A  ", "row1 c6": "  B  ", "row1 c7": " A OR B", "row1 c8": "      ", "row1 c9": "  A  ", "row1 c10": "NOT A ","row2 c1": "True ", "row2 c2": "True ", "row2 c3": " True  ", "row2 c4": "     ", "row2 c5": "True ", "row2 c6": "True ", "row2 c7": " True  ", "row2 c8": "      ", "row2 c9": "True ", "row2 c10": "False", "row3 c1": "True ", "row3 c2": "False", "row3 c3": " False ", "row3 c4": "     ", "row3 c5": "True ", "row3 c6": "False", "row3 c7": " True  ", "row3 c8": "      ", "row3 c9": "False", "row3 c10": "True ","row4 c1": "False", "row4 c2": "True ", "row4 c3": " False ", "row4 c4": "     ", "row4 c5": "False", "row4 c6": "True ", "row4 c7": " True  ", "row4 c8": "      ", "row4 c9": "      ", "row4 c10": "      ", "row5 c1": "False", "row5 c2": "False", "row5 c3": " False ", "row5 c4": "     ", "row5 c5": "False", "row5 c6": "False", "row5 c7": " False ", "row5 c8": "      ", "row5 c9": "      "}
def display_board(boolean_operator):
    bord = """
    {row1 c1} | {row1 c2} | {row1 c3} | {row1 c4} | {row1 c5} | {row1 c6} | {row1 c7} | {row1 c8} | {row1 c9} | {row1 c10}
    -----------------------------------------------------------------------------------
    {row2 c1} | {row2 c2} | {row2 c3} | {row2 c4} | {row2 c5} | {row2 c6} | {row2 c7} | {row2 c8} | {row2 c9} | {row2 c10}
    -----------------------------------------------------------------------------------
    {row3 c1} | {row3 c2} | {row3 c3} | {row3 c4} | {row3 c5} | {row3 c6} | {row3 c7} | {row3 c8} | {row3 c9} | {row3 c10}
    -----------------------------------------------------------------------------------
    {row4 c1} | {row4 c2} | {row4 c3} | {row4 c4} | {row4 c5} | {row4 c6} | {row4 c7} | {row4 c8}
    -----------------------------------------------------------
    {row5 c1} | {row5 c2} | {row5 c3} | {row5 c4} | {row5 c5} | {row5 c6} | {row5 c7} | {row5 c8}
    """.format(**boolean_operator)
    print bord

display_board(boolean_operator)
order_for_boolean= "\n".join(["1- not is evaluated first"
,"2- and is evaluated next","3- or is evaluated last."])
print "The order of operations for boolean operators:"
print (order_for_boolean)
