

while True:
    score = input("How many Credit Hours have you earned? ")

    score = int(score)

    if 0 <= score < 30:
        print("You are a Freshman.")
        break
    elif 30 <= score < 60:
        print("You are a Sophomore.")
        break
    elif 60 <= score < 90:
        print("You are a Junior.")
        break
    elif 90 <= score <= 150:
        print("You are a Senior.")
        break
    else:
        print("That is not Valid. Number must be between 0 and 150! ")
