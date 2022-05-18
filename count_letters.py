def count_letters(string):
    your_dict={}
    for i in string.upper():
        if i in your_dict:
            your_dict[i] += 1
        else:
            your_dict[i] = 1
    return your_dict


print(count_letters("AaBbCcDcEe"))