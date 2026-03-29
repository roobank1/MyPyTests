# name = input("Enter your name :")
# age = int(input("Enter your age :"))



def CheckVotingAge( name, age ):
    print("Hai", name)
    if age >= 18:
        VoteElgible = True
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote")
        VoteElgible = False
    return VoteElgible  
    
print("Voting Rights : ", CheckVotingAge("R", 22 ))

   