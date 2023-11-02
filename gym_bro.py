def calculate_water_intake(weight_kg, activity_level):
    # Convert weight to pounds
    weight_lbs = weight_kg * 2.20462

    # Calculate the base water intake
    base_intake_oz = weight_lbs / 2.2 * 30  # Adjust the multiplier as needed (30-35 mL per kg)

    # Calculate the additional intake based on activity level
    if activity_level == "light":
        activity_adjustment_oz = 8
    elif activity_level == "moderate":
        activity_adjustment_oz = 16
    elif activity_level == "intense":
        activity_adjustment_oz = 32
    else:
        activity_adjustment_oz = 0  # No adjustment

    # Total water intake
    total_intake_oz = base_intake_oz + activity_adjustment_oz

    return total_intake_oz



def calorie_calculator():
    print("Calorie_calculator:")
    print("Select your Gender")
    print("1. Male")
    print("2. Female")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        try:
            weight1 = float(input("Enter your weight in kilograms: "))
            height1 = float(input("Enter your height in centimeters: "))
            age1 = float(input("Enter your age: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            return  # Exit the function on invalid input

        # BMR formula for male
        BMR1 = round(66.47 + (13.75 * weight1) + (5.003 * height1) - (6.755 * age1))

        # Calculate macronutrients
        Carbohydrate = round(0.45 * BMR1 / 4)
        Protein = round(0.25 * BMR1 / 4)
        Fat = round(0.30 * BMR1 / 9)

        print(f"Your estimated BMR is {BMR1} calories with {Carbohydrate}g Carbohydrate, {Protein}g Protein, and {Fat}g Fat per day.")

    elif choice == '2':
        try:
            weight2 = float(input("Enter your weight in kilograms: "))
            height2 = float(input("Enter your height in centimeters: "))
            age2 = float(input("Enter your age: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            return  # Exit the function on invalid input

        # BMR formula for female
        BMR2 = round(655.1 + (9.563 * weight2) + (1.850 * height2) - (4.676 * age2))

        # Calculate macronutrients
        Carbohydrate2 = round(0.45 * BMR2 / 4)
        Protein2 = round(0.25 * BMR2 / 4)
        Fat2 = round(0.30 * BMR2 / 9)

        print(f"Your estimated BMR is {BMR2} calories with {Carbohydrate2}g Carbohydrate, {Protein2}g Protein, and {Fat2}g Fat per day.")

    else:
        print("Invalid choice. Please enter 1 or 2.")


    # Remove the recursive call to exit the function


def main():
    while True:
        print("GYM BRO HELPBITE")
        print("1. Calorie calculator")
        print("2. Water intake")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            calorie_calculator()
        elif choice == '2':
            weight_kg = float(input("Enter your weight in kilograms: "))
            while True:
                activity_level = input("Enter your activity level (light/moderate/intense): ").lower()
                if activity_level in ["light", "moderate", "intense"]:
                    break  # Valid input, exit the loop
                else:
                    print("Invalid input. Please enter 'light', 'moderate', or 'intense'.")

            water_intake_oz = calculate_water_intake(weight_kg, activity_level)
            print(f"Your estimated daily water intake is {water_intake_oz} ounces.")
        elif choice == '3':
            print("Exiting GYM BRO HELPBITE. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()

print(
    """
    .d888d8b888
    d88P"  Y8  P888
    888        888
    888888 888 888888    88888b.  .d88b.    .d8888b .d8888b
    888    888 888       888 "88d 8P  Y8   b88K     88K
    888    888 888       888  888 8888888  "Y8888b. "Y8888b.
    888    888 Y88b.     888  88Y 8b.           X88     X88
    888    888 "Y888888  888 "Y88 888888P' 88888P  88888P     '"""
)




























