import art

print(art.logo)

bids = {}

restart = True
while restart:
    bidder = input("What is your name?:\n")
    amount = input("What is your bid?: $")

    fin = input("Are there any other bidders? Type 'yes or 'no'.\n")


    if fin == 'no':
        bids[bidder] = amount
        restart =False
        #define blanks of final value
        clip = 0
        winner = ""
        #loop through the dictionary to find the highest amount
        for key in bids:

            money = bids[key]
            dough = int(money)
            if dough > clip:
                #print(key) #check who is the current highest at each iteration
                clip = dough
                winner = key
            print(clip)
        print(f"The winner of the auction is {winner.capitalize()} with a bid of {clip}")

    elif fin == "yes":
        bids[bidder] = amount
        print("\n"*20)
    else:
        print("Ooops, incorrect choice, please input either yes or no. Current Bid not saved, Please Try again")
        print(bids)









    # print(bids) #for debugging, check the current dictionary