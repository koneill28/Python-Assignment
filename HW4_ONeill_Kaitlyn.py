
# Name: Kaitlyn O'Neill
# Course: BMGT302
# Section: 0401
# Date: April 8, 2022

# Part 1

# define credit values
min_credit = 300
max_credit = 850
credit_needed = 605

# define credit multipliers
min_credit_multiplier = -.2
max_credit_multiplier = .2

# create lists for applicant information
name_list = []
credit_list = []
multiplier_list = []
count_eligible = []
count_ineligble = []
total_yes = []

# set value for total bookings 
total_bookings = 0

    
# collect applicant data
def determine_credit():
    entering_info = 'Y'

    while entering_info == 'Y':
        print('Enter Y for Yes and N for No')
        
        entering_info  = input('Are you still entering applicant information? ')
        if entering_info == 'Y':
            applicant_name = input('Applicant Name: ')
            name_list.append(applicant_name)

            valid_input = True
            while valid_input:
                try:
                    applicant_credit_score = int(input('Credit Score: '))
                    valid_input = False 
                except ValueError:
                    print('Error, please try again!')
                else:
                    credit_list.append(applicant_credit_score)
                    
                                
            valid_input = True
            while valid_input:
                try:
                    credit_multiplier = float(input('Credit Score Multiplier (in decimal format): '))
                    valid_input = False
                except ValueError:
                    print('Error, please try again!')
                else:
                    multiplier_list.append(credit_multiplier)
                    
                
determine_credit()

# create file and add data
with open('accounts.txt', mode = 'w') as accounts:
    for i in range(len(name_list)):
        accounts.write(f'{name_list[i]}'+ ' ' + f'{credit_list[i]}' + ' ' + f'{multiplier_list[i]}\n')

# update credit list 
updated_credit_list = [credit_list[i] * (multiplier_list[i] +1) for i in range(len(credit_list))]

# determine booking eligibility 
def booking_eligibility(list1):
    booking_eligible = ['No' if credit < credit_needed else 'Yes' for credit in list1]
    return(booking_eligible)

booking_eligible = booking_eligibility(updated_credit_list)

# count number of bookings made
for value in updated_credit_list:
    if value > credit_needed:
        total_bookings += 1

# determine bookings made and declined
total_declined = len(name_list) - total_bookings

# account for division by zero
try:
    percent_booked = (total_bookings/len(name_list)) * 100
except ZeroDivisionError:
    percent_booked = 0
        

# print booking data
print('Credit Account Analysis:')
print(f'Total applications booked: {total_bookings}')
print(f'Total applications declined: {total_declined}')
print(f'Percent of applications booked: %.2f%%' % (percent_booked))

# print data from file 
with open('accounts.txt', mode ='r') as accounts:
    print('Original Data:')
    print(f'{"Name":<10} {"Original Credit Score":<20}{"Credit Multiplier":>20}')
    for record in accounts:
        name, credit, multiplier = record.split(' ')
        print(f'{name:<10} {credit:<20} {multiplier:>20}')


# print additional data
print('Finalized Applicant Data:')
print(f'{"Name":<10} {"Updated Credit":<20} {"Booking Eligible":>20}')
for i in range(len(name_list)):
    print(f'{name_list[i]:<10} {updated_credit_list[i]:>20} {booking_eligible[i]:>20}\n')


# Part 2

import random

# create list for dice values
dice_list = []

# define die value
min_die_value = 1
max_die_value = 6


# determine number of rolls
valid_input = True
while valid_input:
    try:
        die_roll = int(input('How many times do you want to roll the pair of dice? '))
        valid_input = False
    except ValueError:
        print('Error, please try again!')

            
# determine dice values
for roll in range(die_roll):
    dice_value = (random.randrange(min_die_value,max_die_value +1) + random.randrange(min_die_value,max_die_value +1))
    dice_list.append(dice_value)

# determine frequencies of dice values
dice_dict = {}
def dice_freq(list1):
    for value in list1:
        dice_dict[value] = dice_dict.get(value, 0) +1
    return dice_dict
    
dice_freq(dice_list)



# print dice data
print('Dice Report:')
print(f'{"Dice Totals:":<16} {"Number of Rolls:":<20} {"Percent of Each Roll:":>19}')
for i in range (2,13):
    if i in dice_dict:
        percent_dice = (dice_dict[i] / die_roll) *100

        print(f'{i:<17d}' + f'{dice_dict[i]:.2f}' + f'%.2f%%' % (percent_dice))
    else:
        print(f'{i:<17d}' + f'{0:<21d}' + f'00.00%')


# I pledge on my honor that I have not given nor received any unauthorized
# assistance on this assignment.
# Kaitlyn O'Neill
    


