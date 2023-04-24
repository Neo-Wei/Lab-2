def calculate_bmi(weight, height):
    print("height = " + str(height))
    print("weight = " + str(weight))

    bmi = weight / (height**2)
    print("bmi = " + str(bmi))

    if (bmi < 18.5):
        print("Under Weight")

    if (bmi > 25.0):
        print("Over Weight")

    if (18.5 < bmi > 25.0):
        print("Normal Weight")

calculate_bmi(weight=57, height=1.82)