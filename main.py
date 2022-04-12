def convert_to_hex(n):
    step1 = n // 16
    step2 = n % 16
    for_remainder = [step2]
    while step1 > 0:
        step2 = step1 % 16
        step1 = step1 // 16

        for_remainder.append(step2)

    solution = for_remainder[::-1]

    convert_chart = {'10': 'A', '11': 'B',
                     '12': 'C', '13': 'D', '14': 'E', '15': 'F'}
    str_of_ints = ''

    for i in solution:
        if i < 10:
            str_of_ints += str(i)
        else:
            str_of_ints += convert_chart[str(i)]
    return f"{n} in hexadecimal is {str_of_ints}"


dec_to_hex = convert_to_hex(int(input("enter a number: ")))
print(dec_to_hex)
