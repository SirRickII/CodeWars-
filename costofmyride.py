'''This Kata is intended as a small challenge for my students

Create a function, called insurance(), that computes the cost of renting a car. 
The function takes 3 arguments: the age of the renter, the size of the car, 
and the number days for the rental. The function should return an integer 
number of the calculated total cost of the rental.

Age (integer) : There is a daily charge of $10 if the driver is under 25

Car Size (string) : There may be an additional daily charge based on the car size:

car size surcharge "economy" $0 "medium" $10 "full-size" $15

Rental Days (integer) : There is a base daily charge of $50 for renting a car. 
Simply multiply the one day cost by the number of days the car is rented in order 
to get the full cost.

Note: Negative rental days should return 0 cost. Any other car size NOT listed 
should come with a same surcharge as the "full-size", $15.'''

def insurance(age, size, num_of_days):
    
    cost = 0
    ad1_cost = 0
    ad2_cost = 0

    if num_of_days> 0:
        if age < 25:
            ad1_cost = 10*num_of_days
        if size == "medium":
            ad2_cost = 10*num_of_days
        elif size == "full-size" or "my custom car":
            ad2_cost = 15*num_of_days
        
        cost = ad1_cost + ad2_cost + 50*num_of_days
    elif num_of_days <= 0:
        cost = 0    

    return cost

print(insurance(25, "my custom car", 7))