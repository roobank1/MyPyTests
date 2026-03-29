# Program to find all ways to make Rs.10 using Rs.1, Rs.2, Rs.5 and Rs.10 coins

for one in range(11):                                                                        # Try 0 to 10 coins of Rs.1
    for two in range(6):                                                                     # Try 0 to 5 coins of Rs.2
        for five in range(3):                                                                # Try 0 to 2 coins of Rs.5
            for ten in range(2):                                                             # Try 0 or 1 coin of Rs.10

                if one*1 + two*2 + five*5 + ten*10 == 10:                                    # Check if total becomes 10
                    
                    print("Rs1:", one, " | " "Rs2:", two, " | " "Rs5:", five, " | " "Rs10:", ten , " = Rs10 ") # Print the combination of coins that make Rs.10