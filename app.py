# app.py

from database import add_seasonal_flavor, get_seasonal_flavors
from database import add_ingredient, get_ingredients
from database import add_customer_suggestion, get_customer_suggestions

def main():
    print("Chocolate House Management Application")
    print("1. Add Seasonal Flavor")
    print("2. View Seasonal Flavors")
    print("3. Add Ingredient")
    print("4. View Ingredients")
    print("5. Add Customer Suggestion")
    print("6. View Customer Suggestions")
    print("0. Exit")

    while True:
        choice = input("Enter choice : ")
        
        if choice == "1":
            flavor = input("Enter flavor name : ")
            available = input("Is it available (yes/no)? ").lower() == 'yes'
            add_seasonal_flavor(flavor, available)
            print("Seasonal flavor added successfully.....")

        elif choice == "2":
            flavors = get_seasonal_flavors()
            print("Seasonal Flavors :")
            for f in flavors:
                print(f)

        elif choice == "3":
            name = input("Enter ingredient name : ")
            quantity = int(input("Enter quantity : "))
            add_ingredient(name, quantity)
            print("Ingredient added successfully.....")

        elif choice == "4":
            ingredients = get_ingredients()
            print("Ingredients :")
            for i in ingredients:
                print(i)

        elif choice == "5":
            suggestion = input("Enter customer suggestion : ")
            allergy_warning = input("Enter allergy warning (if any) : ")
            add_customer_suggestion(suggestion, allergy_warning)
            print("Customer suggestion added successfully.....")

        elif choice == "6":
            suggestions = get_customer_suggestions()
            print("Customer Suggestions :")
            for s in suggestions:
                print(s)

        elif choice == "0":
            print("Exiting application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()