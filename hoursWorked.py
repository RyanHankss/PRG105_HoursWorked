#define a function that accepts hours worked and pay rate
def payment(hours, rate):

    my_pay = hours * rate

    #convert to string
    str_payment = str(my_pay)

    print("I've made $" + str_payment + " in one day.")

my_hours = 6.5
my_wage = 60

 # call function

payment(3, 8.25)

payment(my_hours, my_wage)
