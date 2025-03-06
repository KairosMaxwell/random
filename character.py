
data_dictionary ={}
entered_End = False
highest_scorer =""
high=0
summation = 0
while entered_End is False:
    student_name = input("Student name: ")
    if student_name.lower() == "end":
        entered_End = True
        break
    else:
        score = float(input("score: "))
        data_dictionary.setdefault(student_name, score)
        data_dictionary.update({})
        highest = max(data_dictionary.values())
        high = highest
        for key, value in data_dictionary.items():
            if value == highest:
                found = True
                highest_scorer = key

overall = sum(data_dictionary.values())
average = overall / len(data_dictionary)



print("Class average score is",average)
print(f"Highest score of {high} is achieved by ",highest_scorer,"!")
print("{:>9s} {:>9s}".format("Student Name","Grade"))
print("{:>9s} {:>9s}".format("====","===="))

for values in data_dictionary:
    print("{:>9s} {:>9.4f}".format(values,data_dictionary[values]))
















