def usd_to_eur(amount):
    return amount * 0.92

def usd_to_gbp(amount):
    return amount * 0.79

def usd_to_cfa(amount):
    return amount * 600

print("Currency Converter")
print("1. USD to EUR")
print("2. USD to GBP")
print("3. USD to CFA")

choice = input("Choose an option (1/2/3): ")
amount = float(input("Enter amount in USD: "))

if choice == '1':
    print("EUR:", usd_to_eur(amount))
elif choice == '2':
    print("GBP:", usd_to_gbp(amount))
elif choice == '3':
    print("CFA:", usd_to_cfa(amount))
else:
    print("Invalid choice")


while True:
    print("\nCurrency Converter")
    print("1. USD to EUR")
    print("2. USD to GBP")
    print("3. USD to CFA")
    print("4. Exit")

    choice = input("Choose (1/2/3/4): ")

    if choice == '4':
        print("Goodbye!")
        break

    amount = float(input("Enter amount in USD: "))

    if choice == '1':
        print("EUR:", amount * 0.92)
    elif choice == '2':
        print("GBP:", amount * 0.79)
    elif choice == '3':
        print("CFA:", amount * 600)
    else:
        print("Invalid choice")