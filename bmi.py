def calculate_bmi(weight, height):
    print("height = " + str(height))
    print("weight = " + str(weight))

    bmi = weight / (height**2)
    print("bmi = " + str(bmi))

    if (bmi < 18.5):
        print("Under Weight")
        return -1

    if (bmi > 25.0):
        print("Over Weight")
        return 1

    if (18.5 < bmi > 25.0):
        print("Normal Weight")
        return 0

calculate_bmi(weight=57, height=1.82)