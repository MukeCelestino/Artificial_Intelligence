i = 10
name = "Muketoi Celestino"
is_rainy = True
temp = 50

# builtin python function
x = pow(5,2)
print(x)

mood = input("How do you feel about AI? ")

if mood == "excited":
    print("me too")
    print("I am super excited about AI")
else:
    print("That's cool too")
    print("It's okay to feel " + mood)

num = input("How many times do you want to repeat? ")
num = int(num)  # int(), float(), str()
i = 0
while i < num:
    print("AI is the Future")
    i += 1

scores = [100, 90, 80, 77, 99, 60, 30, 100]
print("Average = ", sum(scores)/len(scores))

print(scores[0])
print(scores[1])
print(scores[-1])

scores += [1, 2, 3]
print(scores)

nums = []
while True:
    num = input("Enter a num (Type 'exit' to end): ")
    if num == "exit":
        break
    nums.append(float(num))

print(nums)