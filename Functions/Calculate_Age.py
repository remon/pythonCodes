#Created by Amr_Aly
#Creation date : 02/07/2018
#It's a simple function to calculate your age
#The error that will occur by the date 29/02/1980 or 84 or 88 or 92 or 96 or...etc
#This error is almost one day you can neglect it 
#I think that it's very useful procedure if you use it in 
#a real project with datetimepicker and textbox
#your birth date = y1, m1, d1
#current date    = y2, m2, d2

def calculate_age(y1, m1, d1, y2, m2, d2): 

    if d2 < d1:
        d2 = d2 + 30
        m2 = m2 - 1
        if m2 < m1:
            m2 = m2 + 12
            y2 = y2 - 1

    years    = int(y2 - y1)
    months   = int(m2 - m1)
    days     = int(d2 - d1) 
    your_age = str(years) + ' Years', str(months) + ' Months', str(days) + ' Days'
   
    return your_age

#This date 29/2/1984 as an example its result must be (34 years, 4 months , 2 days)
#But with this method the result will be(34 years, 4 months , 3 days)
#you see now that you can neglect it , one day only is the difference
#Don't forget that . It's a simple procedure

print calculate_age(1984,2,29,2018,7,2)


