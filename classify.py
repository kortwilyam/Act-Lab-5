def classify_age(age):
    if age < 0:
        print("Invalid! Di kapa nagagawa")
        
    elif age <= 12:
        print("Child")
    elif age <= 19:
        print("Teen")
    elif age <= 64:
        print("Adult")
    elif age >= 65:
        print("Senior")
        
while True:
    age = int(input("Ilang taon kana?"))
    classify_age(age)