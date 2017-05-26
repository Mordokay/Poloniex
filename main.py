from Poloniex import *
from time import sleep
import msvcrt
import re

#Chave do Pedro
#apiKey = 'RFKEPYEE-YWB8ZKU0-MRFZTWVB-NA3Q2DUK'
#secretkey = '3746916934be509d5c407e3abf1656d964fec222cb6a81a679f0d1c460171965569bb3763bb1d0aed61e40b695de2d662042bd5fbeeda47bc49a9c3218470c80'

#Chave do Francisco
apiKey = 'OAZSH6RM-79SUB8IL-DITSZL85-BYQVF51T'
secretkey = '8d471b7103203babfbb75c2e4f6e1f2c40df2d2792b138f7415ffacc76e38e974a8caa34f745f84c493b87fcfa1336bc64d4fb58aa1a19bfff3cf9bc74e4b983'


conn = Poloniex(apiKey,secretkey)

#while True:
#    if(conn.returnOrderBook("BTC_XRP",10)["bids"][0][1] > conn.returnBalances()["XRP"]):
#        conn.sell("BTC_XRP", 0.00011198, 2)
while True:
    if msvcrt.kbhit() and msvcrt.getch() == chr(27).encode():
        print("\n")
        break

    # Now ask for input
    user_input = input("Input command: \n 1 -> Trade \n 2 -> Get Balance \n 3 -> List Trades \n 4 -> List Coins \n 5 -> Help \n\n >>>>>>>>>")
    if re.search('[a-zA-Z]', user_input):
        print("Command must not contain letters")
    elif(int(user_input) == 1):
        user_input = input("Select Currency Pair: ")
        while True:
            if msvcrt.kbhit() and msvcrt.getch() == chr(27).encode():
                print("\n")
                break
            print("Trading the coin " + user_input)
            sleep(1)
    elif(int(user_input) == 2):
        user_input = input("Select Currency: ")

        if user_input in conn.returnBalances():
             print(conn.returnBalances()[user_input])
        else:
             print("There is no currency named: " + user_input)
    elif (int(user_input) == 3):
        user_input_pair = input("Select Currency Pair: ")
        user_choice = input("1 -> Bids\n2 -> Asks \n\n >>>>>>>>>")

        while True:
            if msvcrt.kbhit() and msvcrt.getch() == chr(27).encode():
                print("\n")
                break

            if int(user_choice) == 1:
                print(conn.returnOrderBook(user_input_pair, 5)["bids"])
                sleep(1)
            elif int(user_choice) == 2:
                print(conn.returnOrderBook(user_input_pair, 5)["asks"])
                sleep(1)

    elif (int(user_input) == 4):
        balances = conn.returnBalances()
        count = 0
        for key, value in balances.items():
            print(key + " <> ", end='')
            count += 1
            if count >= 12:
                count = 0
                print()
    elif (int(user_input) == 5):
        print("I wanna help you!!!")
    else:
        print("Incorrect command called " + str(user_input))


   # if(float(conn.returnOrderBook("BTC_XRP",10)["bids"][0][0]) > 0.0001093):
   #     # print(conn.sell("BTC_XRP", 0.0001093, 2));
   #     # break
   # else:
   #     print("Waiting For Good Value")sd

#print(conn.returnBalances()["BTC"])
#print(conn.returnTicker())
#print(conn.sell("BTC_XRP", 0.00011198, 2));
#print(conn.cancelOrder(51754372938));
#print(conn.buy("BTC_XRP", 0.00010850, 0.0003));
#print(conn.returnTradeHistory("BTC_XRP"))
#print(conn.getMarginPosition("BTC_XRP"))
#print(conn.buy("BTC_XRP", "0.00011370", "2"))