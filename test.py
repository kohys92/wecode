def get_even_number():
    even_list = []
    for num in range(1,51):
        if num%2 == 0:
            even_list.append(num)    

    return even_list

# print(get_even_number())