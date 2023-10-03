amount = int(input("Enter amount to be sent\n "))
network = input("What network are you sending from ")

mtnCharge = 0.0075 * amount
vfCharge = 0 * amount
eLevy = 0.015 * amount

if amount <= 100 and network == "mtn":
    totalCharge = mtnCharge
    received = amount
    print("mtn charge is gh" + str("%.2f"%mtnCharge)+".")
    print("transactions less than 100gh do not attract e-levy charges")
    print("total tax is gh" + str("%.2f"%totalCharge)+".")
    print("Payment made for gh" + str("%.2f"%received) + ".")
    response = input("\ndo you still want to send? yes or no?\n ")

    def send():
        print("thanks for transacting with us!")
    def noSend():
        print("transaction terminated")
    if response == "yes":
        send()
    elif response == "no":
        noSend()



elif amount > 100 and network == "mtn":
    totalCharge = mtnCharge + eLevy
    received = amount
    print("mtn charge is gh" + str("%.2f" % mtnCharge) + ".")
    print("e-levy charge is gh" + str("%.2f"%eLevy) + ".")
    print("total tax is gh" + str("%.2f" % totalCharge) + ".")
    print("Payment made for gh" + str("%.2f"%received)+".")
    response = input("\ndo you still want to send? yes or no?\n ")


    def send():
        print("thanks for transacting with us!")
    def noSend():
        print("transaction terminated")
    if response == "yes":
        send()
    elif response == "no":
        noSend()

elif amount <= 100 and network == "vodafone":
    totalCharge = 0
    received = amount
    print("transactions from vodafone carry no charges")
    print("transactions less than 100gh do not attract e-levy charges")
    print("total tax is gh" + str("%.2f"%totalCharge)+".")
    print("Payment made for gh" + str("%.2f"%received) + ".")
    response = input("\ndo you still want to send? yes or no?\n ")


    def send():
        print("thanks for transacting with us!")


    def noSend():
        print("transaction terminated")


    if response == "yes":
        send()
    elif response == "no":
        noSend()

elif amount > 100 and network == "vodafone":
    totalCharge = eLevy
    received = amount
    print("transactions from vodafone carry no charges")
    print("e-levy charge is gh" + str("%.2f"%eLevy)+".")
    print("total tax is gh" + str("%.2f"%totalCharge) + ".")
    print("Payment made for gh" + str("%.2f" % received) + ".")

    response = input("\ndo you still want to send? yes or no?\n ")
    def send():
        print("thanks for transacting with us!")
    def noSend():
        print("transaction terminated")
    if response == "yes":
        send()
    elif response == "no":
        noSend()



