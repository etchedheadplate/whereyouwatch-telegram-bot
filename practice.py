sub_list1 = [1,2,3,4,5]
sub_list2 = [6,7,8,9,10]
sub_list3 = [11,12,13,14,15]
prime_list = [sub_list1, sub_list2, sub_list3]

def return_sublist(list):
    list_counter = 0
    for sublist in list:
        for string in sublist:
            yield string
        list_counter += 1
        yield list_counter
        print("* list change to " + str(list_counter))

print_list = return_sublist(prime_list)

print('== return_sublist test ==')
print(next(print_list))
print(next(print_list))
print(next(print_list))
print(next(print_list))
print(next(print_list))
print(next(print_list))
print(next(print_list))
print(next(print_list))
print(next(print_list))
print(next(print_list))
print(next(print_list))
print(next(print_list))
print(next(print_list))
print(next(print_list))
print(next(print_list))
print()

'''some_url = 'somesite[dot]com'
page_num = 0

def page_turner(url, page_num):
    while True:
        page_num += 1
        result_url = url + '/' + str(page_num)
        yield result_url

print_url = page_turner(some_url)

print('== page_turner test ==')
print(next(print_url))
print(next(print_url))
print(next(print_url))
print(next(print_url))
print(next(print_url))
print(next(print_url))
print(next(print_url))
print(next(print_url))
print(next(print_url))
print(next(print_url))
print()'''