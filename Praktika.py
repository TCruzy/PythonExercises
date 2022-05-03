"""1)დაწერეთ პროგრამა რომელიც გამოითვლის სამი მოცემული რიცხვის ჯამს, მაგრამ თუ ეს რიცხვები ერთმანეთის ტოლი დააბრუნებს
მათ ჯამს გამრავლებულს სამზე"""
import random

from click import secho


# def sum_thrice(x=int(input()), y=int(input()), z=int(input())):
#     print("x: %d y: %d z: %d"%(x, y, z))
#     return x + y + z
#     if x == y == z:
#         return (x+y+z)*3
# print(sum_thrice())

"""2)დაწერეთ პროგრამა რომელიც გაარკვევს მომხმარებლის მიერ შეყვანილი რიცხვი ლუწია თუ კენტი და გამოიტანს შესაბამის ინფორმაციას"""

# def odd_or_even(x=int(input("Give Me Number: "))):
#     print("x : %d"%(x))
#     if x % 2 == 0:
#         return "Luwia"
#     else:
#         return "Kentia"
# print(odd_or_even())

"""3)დაწერეთ პროგრამა რომელიც დაითვლის 4-იანების რაოდენობას მოცემულ სიაში"""

# def list_count_4(l = [2,3,1,5,4,3,4,6,4,4,4]):
#     x = 0
#     y = -1
#     while y < len(l)-1:
#         y += 1
#         if l[y] == 4:
#             x += 1
#     return f"4 is {x} times"
# print(list_count_4())

"""4)დაწერეთ პროგრამა რომელიც შეამოწმებს გადაცემული სიმბოლო ხმოვანია თუ თანხმოვანი"""

# def is_vowel(x = str(input("Give Me Letter :"))):
#     if len(x) > 1:
#         print(x)
#         return is_vowel(str(input("Give Me Letter :")))
#     else:
#         if x == "a" or x == "e" or x == "u" or x == "y" or x == "i" or x == "o":
#             return f"{x} Xmovania"
#         return f"{x} Tanxmovania"
# print(is_vowel())
"""5)დაწერეთ პროგრამა რომელიც შეამოწმებს არის თუ არა მოცემული მნიშვნელობა მოცემულ სიაში (არ გამოიყენოთ in ოპერატორი)"""

# def is_list_member(l = [2,2,4,5,1,23,5]):
#     for i in l:
#         if i == 23:
#             return "23 Aris Siashi"
#     return "23 Ar Aris Siashi"
# print(is_list_member())

"""6) დაწერეთ პროგრამა რომელიც მოახდენს მოცემული სიის ყველა ელემენტის ტექსტურ კონკატენაციას (მიმატებას) და დააბრუნებს
 ამ ახალ ტექსტს"""

# def concatenate_list_data(l = [3,5,23,31,13,4]):
#     x = ""
#     for i in l:
#         x += str(i)
#     return f"'{x}'"
# print(concatenate_list_data())

"""7)დაწერეთ პროგრამა რომელიც დააბრუნებს ყველა ფერს სიიდან color_list_1 რომელიც არ არის სიაში color_list_2 
სატესტო მონაცემები:

color_list_1 = ["White", "Black", "Red"]

color_list_2 = ["Red", "Green"]
მოსალოდნელი შედეგი:

['White', 'Black']"""

# def diff_in_colors(l = ["White", "Black", "Red","Green","Grey"],l2 = ["Green","Red","Grey"]):
#     x = 0
#     for i in l:
#         if i in l2:
#             l.remove(i)
#     return l
# print(diff_in_colors())

"""8)დაწერეთ პროგრამა რომელსაც გადაეცემა სამკუთხედის ფუძე და სიმაღლე და გამოითვლის ფართობს"""
# def triangle_area(f=int(input("Fudze : ")),h = int(input("Simaghle: "))):
#     return f"Fudze: {f} ,Simaghle: {h} , Fartobi : {(f*h)/2}"
# print(triangle_area())

"""9)დაწერეთ პროგრამა რომელიც დაითვლის სამი რიცხვის ჯამს, მაგრამ თუ ამ სამი რიცხვიდან ორი მაინც უდრის ერთმანეთს დააბრუნებს 0-ს."""

# def sum_of_three_if_not_equal(x=int(input()), y=int(input()), z=int(input())):
#     if x == y or x == z or y == z:
#       return 0
#     else:
#       return x+y+z
#
#
# print(sum_of_three_if_not_equal())

"""10)დაწერეთ პროგრამა რომელიც დაითვლის ორი რიცხვის ჯამს, მაგრამ თუ ეს ჯამი არის 15-სა(ჩათვლით) და 20-ს შორის(ჩათვლიდ) დააბრუნებს 20-ს"""

# def sum_of_two_20_if_between_15_and_20(x=int(input("x: ")),y =int(input("y: "))):
#     if 15 <= x + y <= 20:
#         return 20
#     return x + y
# print(sum_of_two_20_if_between_15_and_20())

"""11)დაწერეთ პროგრამა რომელიც დააბრუნებს True-ს თუ ორი რიცხვი ტოლია, ან მათი სხვაობა ან ჯამი არის 5, თუ არა და დააბრუნებს False-ს"""
# def test_number_5(x = int(input("x:")), y = int(input("y:"))):
#     if x == y or x + y == 5 or x - y == 5 or y - x == 5:
#         return True
#     return False
#
#
# print(test_number_5())

"""12)დაწერეთ პროგრამა რომელიც ამოხსნის (x + y) * (x + y)"""
# def x_plus_y_squared(x = int(input("x:")), y = int(input("y:"))):
#     return f"x : {x}, y : {y} , (x + y) * (x + y) = {x**2+2*(x*y)+y**2}"
# print(x_plus_y_squared())


"""13)დაწერეთ პროგრამა რომელიც დააჯამებს პირველ n მთელ რიცხვს """

# def sum_of_first_n_integers(n):
#     x = 0
#     for i in range(0,n+1):
#         x += i
#     return x
# print(sum_of_first_n_integers(int(input())))

"""14)დაწერეთ პროგრამა რომელიც დაითვლის პირველი n მთელი რიცხვის ნამრავლს (ფაქტორიალი) """
# def product_of_first_n_integers(n = int(input("Number: "))):
#     x = 1
#     for i in range(1,n+1):
#         x *= i
#     return f"{n}'is Faktoriali : {x}"
# print(product_of_first_n_integers())

"""15)დაწერეთ პროგრამა რომელიც გამოითვლის მართკუთხა სამკუთხედის ჰიპოტენუზას მომხმარებლის მიერ მითითებული კათეტების გამოყენებით"""

# def hipotenuse(k = int(input("Kateti 1: ")),k2 = int(input("Kateti 2: "))):
#     return f"Kateti 1 : {k}, Kateti 2 : {k2} , Hipotenuza : {(k**2+k2**2)**(1/2)}"
# print(hipotenuse())

"""16) დაწერეთ პროგრამა რომელიც მომხმარებლის მიერ შეყვანილ დღეებს, საათებს, წუთებსა და წამებს გადაიყვანს წამებში 
(გამოითვლის რამდენი წამია)"""
# def  to_seconds(day = int(input("Day : ")),hours = int(input("hours: ")),sec = int(input("Minute: "))):
#     hour = 3600
#     days = 3600*24
#     min = 60
#     return f"Day : {day}, Hour : {hours} , Minute : {min} , In Seconds = {(day*days)+(hours*hour)+(minute*min)}"
# print(to_seconds())

"""17)დაწერეთ პროგრამა რომელიც მომხმარებლის მიერ შეყვანილ წამებს გადაიყვანს დღეებში, საათებში, წუთებსა და წამებში"""

# def to_days_hours_minutes_seconds(sec = int(input("Seconds : "))):
#     minute = 60
#     hour = 3600
#     day = 24*3600
#     return f"Day :{int(sec//day)}, Hour : {(sec-sec//day)/hour} , Minute : {int((sec-(sec//day))/hour)/minute}, Second : {sec}  === Second = {sec}"
# print(to_days_hours_minutes_seconds())
# sec = int(input("Seconds : "))
# day = sec//86400
# hour = sec//36009
# minute = sec//60
# print(f"Day :{day}, Hour : {hour} , Minute : {minute},  === Second = {sec}")
"""18)დაწერეთ პროგრამა რომელიც დაითვლის მომხმარებლის მიერ შეყვანილი ოთხციფრიანი რიცხვის ციფრების ჯამს
(მაგალითად 5245 => 5 + 2 + 4 + 5 => 16"""

# def sum_of_digits(x = input("Number: ")):
#     y = []
#     z = ""
#     y.append(x)
#     for i in y:
#         z += i
#         print(z)
#         return int(z[0])+int(z[1])+int(z[2])+int(z[3])
# print(sum_of_digits())

"""19)დაწერეთ პროგრამა რომელიც ამოწმებს მეტია თუ არა სიის ყველა ელემენტი მოცემულ რიცხვზე"""

# def list_elements_greater_than(x = int(input("Number : ")), l = [5,52,9,23,31]):
#     for i in l:
#         if i > x:
#             return f"Siiss kvela Elementi Metia Ricxv {x}'ze"
#         return f"Siiss Kvela Elementi Araa Meti {x}'ze"
# print(list_elements_greater_than())

"""20)დაწერეთ პროგრამა რომელიც დაითვლის სტრინგში მოცემული სიმბოლოს რაოდენობას"""

# def count_a_char_in_string(s = "aaaasssddaaafffggg", x = str(input("Letter: "))):
#     z = 0
#     if len(x) > 1:
#         print("Letter lenght must be 1")
#         return count_a_char_in_string("aaaasssddaaafffggg", str(input("Letter: ")))
#     for i in s:
#         if x in i:
#             z += 1
#     return f"{x} in the string is {z} times"
# print(count_a_char_in_string())

"""21)დაწერეთ პროგრამა რომელიც გაცვლის ცვლადების მნიშვნელობებს ერთმანეთში (მაგ: თუ a არის 5 და b არის 8, შედეგი უნდა იყოს: 
a არის 8 და b არის 5) """

# def swap_variables(a=5, b=8):
#     print("a : %d , b : %d"%(a,b))
#     z = a
#     x = b
#     a = x
#     b = z
#     return "a : %d, b : %d"%(a, b)
# print(swap_variables())

"""22)დაწერთ პროგრამა რომელიც შეამოწმებს მომხმარებლის შეტანილი რიცხვი დადებითია, უარყოფითი თუ ნული"""

# def check_number_sign(x = int(input("Number : "))):
#     if x > 0:
#         return x, "Dadebitia"
#     elif x == 0:
#         return x, "Nulia"
#     else:
#         return x, "Uaryofitia"
# print(check_number_sign())

"""23)დაწერეთ პროგრამა რომელიც შეამოწმებს მომხმარებლის შეტანილი ტექსტი რიცხვია თუ არა, და თუ არ არის რიცხვი
 გამოიტანს შეცდომას ამის შესახებ (შეცდომა უნდა გამოდიოდეს სანამ მომხმარებელი არ შეიყვანს რიცხვს) ver davcere"""
"""write a program to check if a given string ia a text or number, don't use isdigit() function."""
# str = input("String : ")
# if str.isdigit():
#     print("Number")
# else:
#     print("Text")
"""24) დაწერეთ პროგრამა რომელიც სიიდან გაფილტრავს მხოლოდ დადებით რიცხვებს"""

# def filter_positive_numbers_from_list(l = [2,3,4,-4,-2,3,-15,3,0]):
#     l1 = []
#     for i in l:
#         if i >= 0:
#             l1.append(i)
#     return l1
# print(filter_positive_numbers_from_list())

"""25)დაწერეთ პროგრამა რომელიც დაითვლის რიცხვების სიის ელემენტების ნამრავლს"""

# def product_of_list(l = [3,3,5,1,3,-1]):
#     l1 = 1
#     for i in l:
#         l1 *= i
#     return l1
# print(product_of_list())

"""26)დაწერეთ პროგრამა რომელიც იპოვის მინიმუმს მოცემულ სიაში (არ გამოიყენოთ ჩაშენებული min ფუნქცია)"""

# NumList = [42,33,45,23,88,15,61,2]
#
# smallest = NumList[0]
# print(smallest)
# for j in range(1, len(NumList)):
#     if smallest > NumList[j]:
#         smallest = NumList[j]
# print("The Smallest Element in this List is : ", smallest)

"""27)დაწერეთ პროგრამა რომელიც იპოვის მაქსიმუმს მოცემულ სიაში (არ გამოიყენოთ ჩაშენებული max ფუნქცია) """

# def find_max_in_list(NumList = [42,33,45,23,88,15,61,2]):
#     biggest = NumList[0]
#     for i in range(1,len(NumList)):
#         if biggest < NumList[i]:
#             biggest = NumList[i]
#     return "Biggest", biggest
# print(find_max_in_list())

"""28)დაწერეთ პროგრამა რომელიც მოცემული რიცხვისთვის გამოითვლის ამ რიცხვზე ნაკლები ყველა დადებითი რიცხვის კუბების ჯამს """

# def sum_of_cubes(x = int(input("number : "))):
#     y = 0
#     while x > 0:
#         x -= 1
#         y += x**3
#     return "Sum Of Cubes :", y
#
# print(sum_of_cubes())

"""29)დაწერეთ პროგრამა რომელიც შეამოწმებს სიაში არსებობს თუ არა ისეთი ორი განსხვავებული რიცხვი რომელთა 
ნამრავლიც არის კენტი"""

# def diff_list(l = [2,8,1,2,5,3,7,9,13,4]):
#     x = -1
#     while x < len(l) - 1:
#         x += 1
#         for i in range(1, len(l)):
#             if (l[x] * l[i]) % 2 != 0:
#                 if l[x] == l[i]:
#                     continue
#                 print(l[x],l[i])
# print(diff_list())

"""30) დაწერეთ პროგრამა რომელიც მოცემული სიისთვის შეამოწმებს ყველა ელემენტი უნიკალურია თუ არა"""

# def test_distinct(l = [2, 1, 25, 21, 51, 51 , 544]):
#     count = 0
#     for i in l:
#         if l.count(i) > 1:
#             count += 1
#     if count > 1:
#         return "არაა ყველა ელემენტი უნიკალური ლისტში"
#     return "ყველა ელემენტი უნიკალურია ლისტში"
# print(test_distinct())


"""31)დაწერეთ ფუნქცია რომელიც შეამოწმებს გადაცემული სია ცარიელია თუ არა (დააბრუნებს True-ს თუ ცარიელია და 
False-ს წინააღმდეგ შემთხვევაში)"""

# def list_is_empty(l = [1]):
#     if len(l) < 1:
#         return True
#     return False
# print(list_is_empty())

"""32)დაწერეთ ფუნქცია რომელსაც გადაეცემა ორი სია და რომელიც დააბრუნებს True-ს თუ ამ ორ სიას აქვს ერთი მაინც
 საერთო ელემენტი, და False-ს წინააღმდეგ შემთხვევაში"""

# def common_data(l = [11,31,23,4,15,1], l2 = [123,32,5,15,13,2]):
#     for i in l:
#         for j in l2:
#             if i in l2 or j in l:
#                 return True
#         return False
# print(common_data())

"""33)დაწერეთ ფუნქცია რომელსაც გადაეცემა სია და რომელიც დააბრუნებს სიის ზომას მას შემდეგ რაც ამ სიიდან ამოიღებს ყველა 
კენტ რიცხვს"""

# def  remove_odds(l = [11,4,8,9 ,19,111,58,67, 12,45,10,15,43,97,67]):
#     print("Tavidan",len(l))
#     for i in l:
#         if i % 2 != 0:
#             l.remove(i)
#             for y in l:
#                 if y % 2 != 0:
#                     l.remove(y)
#     return "Kentebis Garda ",len(l)
# print(remove_odds())

"""34)დაწერეთ ფუნქცია რომელსაც გადაეცემა ორი სია და რომელიც დააბრუნებს ახალ სიას რომელიც შედგება 
ამ სიების განსხვავებული ელემენტებისგან (ანუ ელემენტებისგან რომელიც არის პირველ სიაში და არ არის მეორეში და
 ელემენტებისგან რომელიც არის მეორე სიაში და არ არის პირველ სიაში)."""

# def difference_between_two_lists(l = [1,2,3,4,5] , l2 = [11,23,15,5,7,3]):
#     for i in l:
#         if i in l2:
#             l.remove(i)
#             l2.remove(i)
#     return l+l2

# print(difference_between_two_lists())

"""35)დაწერეთ ფუნქცია რომელიც გადაცემულ სიმბოლოების სიას გადაიყვანს ტექსტში """

# def char_list_to_string(l = ["&",13,5,1,"#"]):
#     x = ""
#     print("list : ",l)
#     for i in l:
#         x += str(i)
#     return "new String",x
# print(char_list_to_string())

"""36) დაწერეთ ფუნქცია რომელსაც გადაეცემა სია და რომელიც დააბრუნებს ამ სიის უნიკალური ელემენტებისგან 
შედგენილ სიას დასორტირებულს ზრდადობით 
gavakete"""

# l = [2,3,41,2,3,23,5,2,23,2,15,69]
# for_unic = []
# for i in l:
#     if l.count(i) > 1:
#         l.remove(i)
#         while i in l:
#             l.remove(i)

# for key in range(len(l)):
#     max = l[0]
#     for i in l:
#         if i < max:
#             max = i
#     for_unic.append(max)
#     l.remove(max)
# print(for_unic)

"""37)დაწერეთ ფუნქცია რომელსაც გადაეცემა სია და რომელიც დააბრუნებს სიის ელემენტების სიხშირეს, ანუ 
დიქტს რომლის გასაღებები არის სიის ელემენტები და მნიშვნელობები კი ელემენტის რაოდენობა სიაში
gavakete"""
# from pprint import pprint
# def element_frequency(l = [12,51,24,1,12,1,4,3,4,3,12]):
#     dict = {}
#     for i in l:
#         if i in dict:
#             dict[i] += 1
#         else:
#             dict[i] = 1
#     return dict
# print(element_frequency())   

"""38) დაწერეთ ფუნქცია რომელსაც გადაეცემა სია და ორი მნიშვნელობა და რომელიც დაითვლის ამ სიაში იმ ელემენტების რაოდენობას
 რომელიც მოთავსებულია მოცემულ მნიშვნელობებს შორის
"""

# def count_range_in_list(l = [int(input("First Number : ")),int(input("Second Number :"))]):
#     x = l[0]+1
#     y = 0
#     while x < l[-1]:
#         x += 1
#         y += 1
#     return "%d Number Is Between %d and %d" % (y, l[0], l[-1])


# print(count_range_in_list())

"""39)დაწერეთ ფუნქცია რომელსაც გადაეცემა მთელი რიცხვების სია და რომელიც დააბრუნებს მთელ რიცხვს რომელიც შედგება 
გადაცემული სიის რიცხვების ციფრებისგან, ანუ მაგალითად [11, 33, 50] სიისთვის უნდა დააბრუნოს 113350"""

# def convert_multiple_integers_into_single_integer(l = [1,151,16,1,23,14]):
#     x = ""
#     for i in l:
#         x += str(i)
#     return int(x)
# print(convert_multiple_integers_into_single_integer())


"""40)დაწერეთ ფუნქცია რომელსაც გადაეცემა სია და დააბრუნებს ახალ სიას რომელშიც იქნება ამ სიის მხოლოდ კენტი ელემენტები"""

# def select_odds(l = [123,15,55,8,512,3,4,4,12,3]):
#     l1 = []
#     for i in l:
#         if i % 2 != 0:
#             l1.append(i)
#     return l1
# print(select_odds())

"""41)დაწერეთ ფუნქცია რომელსაც გადაეცემა მთელი დადებითი რიცხვი n და რომელიც დააბრუნებს დიქტს რომლის გასაღებები იქნება
 რიცხვები 1-დან n-ის ჩათვლით და რომლის მნიშვნელობები იქნება ეს რიცხვები აყვანილი კვადრატში. მაგალითად n=4-სთვის უნდა 
 დააბრუნოს {1:1, 2:4, 3:9, 4:16} 
"""

# def squares_dict(k = 5):
#     dict = {}
#     for i in range(1, k+1):
#         dict[i] = i**2
#     print(dict)
# print(squares_dict())

"""42) დაწერეთ ფუნქცია რომელსაც გადაეცემა დიქტი და რომელიც დააბრუნებს ახალ დიქტს რომლიდანაც ამოღებული იქნება ელემენტები 
ცარიელი მნიშვნელობებიც, მაგალითად {'c1': 'Red', 'c2': 'Green', 'c3': None} დიქტისთვის უნდა დააბრუნოს 
{'c1': 'Red', 'c2': 'Green' } """

# def remove_items_with_empty_values(d = {'c1': 'Red', 'c2': 'Green', 'c3': None, "c4": None}):
#     while None in d.values():
#         d.pop(list(d.keys())[list(d.values()).index(None)])
#     return d

# print(remove_items_with_empty_values())
"""1) Do/While ციკლის ოპერატორის გამოყენებით შეადგინეთ პროგრამა,რომელიც გამოთვლის y = x^2 + 5 ფუნქციის მნიშვნელობების და 
წარმოადგენს ფუნქციისა და არგუმენტის მნიშვნელობათა ცხრილს, სადაც x არგუმენტის [-5;5] ინტერვალში იცვლება h=1.5 ბიჯით
   2)შეადგინეთ პროგრამა, რომელიც 3 დან 30 მდე გამოთვლის კენტი რიცხვების ნამრავლს"""
# 1) x = -5
# while x <= 5:
#     y = x ** 2 + 5
#     print("x : %d , y : %d"%(x, y))
#     x += 1.5
# 2) def my():
#     y = 1
#     for i in range(3, 31, 2):
#         if i % 2 != 0:
#             y *= i
#     return y
# print(my())

""""45) დაწერეთ ფუნქცია რომელსაც გადაეცემა ორი სტრინგი და რომელიც დააბრუნებს ახალ სტრინგს რომელიც 
შედგება პრობელით გაერთიანებული ამ სტრინგებისგან და გადაცემული სტრინგის პირველ ორ სიმბოლოს გაცვლილი 
ექნება ადგილები, მაგალითად სტრინგებისთვის  'abc' და 'xyz' უნდა დააბრუნოს 'xyc abz'"""

# def join_swapped_strings(s = "abcd", s1 = "efgh"):
#     print("Strings : %s , %s" % (s, s1))
#     first_letter = s1[:2] + s[2:]
#     second_letter = s[:2] + s1[2:]
#     return f"{first_letter} {second_letter}"

# print(join_swapped_strings())




"""47) დაწერეთ ფუნქცია რომელსაც გადაეცემა სტრინგი და ორი რიცხვი n და m და რომელიც დააბრუნეს ახალ სტრინგს რომელიც
 შედგება ამ სტრინგს დამატებულს ბოლო n სიმბოლოს m-ჯერ. თუ გადაცემული სტრინგის სიგრძე ნაკლებია ან ტოლი n-ზე მაშინ უნდა 
 დააბრუნოს ეს ტექსტი გამეორებული m-ჯერ. მაგალითად 'Python', n=2,m=4 უნდა დააბრუნოს 'Pythononononon' ; 'abc', n=4, m=3
  უნდა დააბრუნოს 'abcabcabc'"""

# def append_end(str = "flugengengexoleni",n = int(input("n : ")), m = int(input("m : "))):
#     print(str+str[-n:]*m)
# append_end()

"""48)დაწერეთ ფუნქცია რომელსაც გადაეცემა ორი სტრინგი და რომელიც დააბრუნებს პირველ სტრინგს რომლიდანა ამოღებული იქნება 
ყველა სიმბოლო რომელიც არის მეორე სტრინგში. მაგალითად 'The quick brown fox jumps over the lazy dog.' და 'aeiou' უნდა
 დააბრუნოს 'Th qck brwn fx jmps vr th lzy dg.'"""

# def strip_chars(str = "The quick brown fox jumps over the lazy dog.", str2 = "aeiou"):
#     print(str)
#     l = []
#     l2 = []
#     for i in str:
#         l.append(i)
#     for j in str2:
#         l2.append(j)
#     for u in l2:
#         while u in l:
#             l.remove(u)
#     str3 = ""
#     for n in l:
#         str3 += n
#     print(str3)
# strip_chars()

"""50)დაწერეთ ფუნქცია რომელიც დააბრუნებს გადაცემული სიიდან სამი ყველაზე დიდი ელემენტიდან შექმნილ სიას. 
"""

# def largest_three_elements(l = []):
#     ll = int(input("Lenght of List: "))
#     x = 0
#     while x < ll:
#         z = int(input("number: "))
#         l.append(z)
#         x += 1
#     max1 = 0
#     max2 = 0
#     max3 = 0
#     l1 = []
#     for i in l:
#         if i >  max1:
#             max1 = i
#     for i in l:
#         if max2 < i < max1:
#             max2 = i
#     for i in l:
#         if max3 < i < max2:
#             max3 = i
#     l1.append(max1)
#     l1.append(max2)
#     l1.append(max3)
#     print("Whole List : ", l)
#     print("3 Biggest Number in this List :", l1)
# largest_three_elements()

"""51)დაწერეთ ფუნქცია რომელსაც გადაეცემა ორი მთელი რიცხვი და რომელიც დააბრუნებს ამ რიცხვების ჯამის ციფრების 
რაოდენობას, მაგალითად 5 და 7-ის შემთხვევაში უნდა დააბრუნოს 2 (5+7 = 12 და 12 შეიცავს 2 ციფრს)."""

# def count_of_digits_of_sum(first_number = 5, second_number = 7):
#     sum = first_number + second_number
#     return len(str(sum))
#
#
# print(count_of_digits_of_sum())

"""52. დაწერეთ ფუნქცია რომელიც დააბრუნებს გადაცემული მთელი რიცხვის ციფრების ჯამს"""
# def sum_of_digits_of_integer(number = int(input("number : "))):
#     sum_of_digits = 0
#     for i in str(number):
#         sum_of_digits += int(i)
#     return sum_of_digits
#
#
# print(sum_of_digits_of_integer())
"""Task"""
Users = [
    {
        "userId": 1,
        'firstName': "Ioseb",
        "lastName": "Geliashvili"
    },
    {
        "userId": 2,
        'firstName': "Nugo",
        "lastName": "Svianidze"
    },
    {
        "userId": 3,
        'firstName': "Elene",
        "lastName": "Pirmisashvili"
    }
]

chat_rooms = [
    {
        "name": "ნუგოს და იოსების ჩათი",
        "createdBy": 1,
        "recipient": Users[1]
    },
    {
        "name": "ნუგოს და ელენეს ჩათი",
        "createdBy": 2,
        "recipient": Users[2]
    },
    {
        "name": "იოსების და ელენეს ჩათი",
        "createdBy": 1,
        "recipient": Users[2]
    }
]

# მინდა დამიწერო ფუნქცია რომელსაც ჩავაწვდი მე იუზერ აიდის
# ის კი დამიბრუნებს ყველა ჩათრუმს სადაც მაგ იუზერს აქვს მონაწილეობა მიღებული
# ასევე, ვინაიდან ნუგო იძახებს ჩათრუმების სიას, მიმღების(recipient) ის ადგილას თუ ნუგო იქნება
# უნდა დამიბრუნდეს მეორე წევრის იუზერის დიქშენერი

# def get_user_chat_rooms():
#     user_id = int(input("userId: "))

#     user_chat_rooms = list(filter(
#         lambda chat_room: chat_room["createdBy"] == user_id or chat_room["recipient"][
#             "userId"] == user_id,
#         chat_rooms
#     ))

#     for chat_room in user_chat_rooms:
#         if chat_room['recipient']['userId'] == 2:
#             for user in Users:
#                 if user['userId'] == chat_room['createdBy']:
#                     chat_room['recipient'] = user

#     return(user_chat_rooms)


# result = get_user_chat_rooms()

# for chat in result:
#     print(chat)
"""53. დაწერეთ ფუნქცია რომელსაც გადაეცემა სია და რომელიც დააბრუნებს ახალ სიას რომელშიც იქნება ამ სიის მხოლოდ 
დადებითი ელემენტები დასორტირებულს კლებადობით"""

# def positive_sorted_elements(l = [-1,3 ,-5, 52, 7, 7, 3, 23, 42 ,223, -3, 11, 0, -24]):
#     print(l)
#     for i in l:
#         if i < 0:
#             l.remove(i)
#     l.sort()
#     print(l[::-1])
#
#
# print(positive_sorted_elements())

"""56. დაწერეთ ფუნქცია რომელსაც გადაეცემა სია და რიცხვი და იპოვის და დააბრუნებს პირველივე რიცხვს ამ სიაში 
რომელიც მეტია გადაცემულ რიცხვზე. თუ ვერცერთი ასეთი რიცხვი ვერ მოიძებნა (ანუ ყველა რიცხვი ნაკლებია ან ტოლი 
გადაცემულ რიცხვზე) მაშინ უნდა დააბრუნოს None."""

# def first_greater_number(l = [ -1, 3,-5, 52, 7, 7, 3, 23, 42 , 223, -3, 11, 0, -24], number = int(input("number : "))):
#     new_list = []
#     for i in l:
#         if i > number:
#             new_list.append(i)
#     if len(new_list) < 1:
#         return None
#     return new_list[0]
#
#
# print(first_greater_number())

"""57. დაწერეთ ფუნქცია რომელსაც გადაეცემა ორი მთელი რიცხვი და ამ რიცხვებს შორის იპოვის ისეთ რიცხვებს რომლის 
ყველა ციფრი ლუწია. უნდა დააბრუნოს ამ რიცხვების სია."""

# def numbers_with_even_digits(first_number = 1, second_number = 300):
#     even_numbers = []
#     for i in range(first_number, second_number + 1):
#         if i % 2 == 0:
#             even_numbers.append(i)
#     for_splited_lists = []
#     list_for_filtered = []
#     new_list = []
#     for i in even_numbers:
#         for_splited_lists.append(".".join(str(i)).split("."))
#     for i in for_splited_lists:
#         for j in i:
#             list_for_filtered.append(list(filter(lambda x: int(x) % 2 == 0, i)))
#     for i in list_for_filtered:
#         new_list.append(int(str(str(i).strip("['']")).replace("', '", "")))
#     for_sort = list(set(new_list))
#     for_sort.sort()
#     return for_sort
# print(numbers_with_even_digits())

"""58. დაწერეთ ფუნქცია, რომელიც დაითვლის გადაცემული მთელი რიცხვის ფაქტორიალს. n-ის ფაქტორიალი არის ყველა
 რიცხვის ნამრავლი რომელიც ნაკლებია ან ტოლია n-ზე. მაგალითად 5-ის ფაქტორიალი არის 1 * 2 * 3 * 4 * 5 = 120"""

# def calculate_factorial(n = int(input("Number: "))):
#     x = 1
#     for i in range(1,n+1):
#         x *= i
#     return f"{n}'is Faktoriali : {x}"
# print(calculate_factorial())


"""59. დაწერეთ ფუნქცია რომელიც დააბრუნებს გადაცემულ რიცხვზე ნაკლებ მარტივ რიცხვებს (მარტივი რიცხვი არის ისეთი
მთელი დადებითი რიცხვი რომელიც უნაშთოდ მხოლოდ ერთზე და თავის თავზე იყოფა, მაგალითებია 1, 3, 7, 11 და ა.შ.)"""

# def is_prime_number(value):
#     divisor_count = 0

#     # თუ რომელიმე ციფრზე (და არა რიცხვზე) იყოფა ვზრდით გამყოფთა რაოდენობას
#     for i in range(1, 11):
#         if value % i == 0:
#             divisor_count += 1


#     # თუ ათეულამდე თავის თავზე გაყოფა არ შესულებულა
#     # გამყოფად ვამატებთ თავისთავსაც
#     if value > 10:
#         divisor_count += 1

#     # თუ ორიგ გამყოფი აქვს არის მარტივი
#     # თუ არდა არა
#     if divisor_count == 2:
#         return True
#     else:
#         return False


# def prime_number_under(value):

#     prime_number_list = []

#     # ლუპით დავადგენთ ყველა მარტივ რიცხვს გადმოცემული value მდე
#     for i in range(value):
#         if i > 0 and is_prime_number(i):
#             prime_number_list.append(i)

#     return prime_number_list


# print(prime_number_under(int(input("number : "))))


"""60. დაწერეთ ფუნქცია რომელიც გამოითვლის და დააბრუნებს პირველ n ფიბონაჩის რიცხვს. ფიბონაჩის რიცხვები არის 
რიცხვების თანმიმდევრობა 0, 1, 1, 2, 3, 5, 8, 13, 21, .... სადაც ყოველი მომდევნო რიცხვი არის მისი წინა ორი 
რიცხვის ჯამი. მაგალითად n=5 უნდა დააბრუნოს 0, 1, 1, 2, 3, 5, 8, 13, 21, 34"""

# def fibonacci_number(n = int(input(" n : "))):
#     nextN = [0, 1]
#     next = 1
#     while next < n:
#         nextN.append(nextN[next - 1] + nextN[next])
#         next += 1
#     return nextN[-1]
#
#
# print(fibonacci_number())

"""Other Exercises"""

"""Palindrome """
# def palindrome(x = str(input("Give Me String : "))):
#     if x == x[::-1]:
#         return "This Is A Palindrome"
#     return "This Is Not A Palindrome"
# print(palindrome())

"""თუ გვინდა ვიპოვოთ რაღაცა რიცხვი, რომლის პროცენტი ვიცით"""
# number = int(input("რიხვი : "))
# while True:
#     procent = int(input("რამდენი პროცენტი გინდათ იყოს რაღაც რიცხვიდან %d : " % (number)))
#     if procent > 100:
#         print("არასწორი პროცენტი, ცადეთ თავიდან")
#         break
#     print("თქვენ გაინტერესებდათ რა რიცხვის %d პროცენტი არის %d " % (procent, number))
#     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#     print("ეს რიცხვი არის : ", (number*100)/procent)
#     break
"""თუ გვინდა ვიპოვოთ მოცემული რიცხვის რამდენი პროცენტია მოცემული რიცხვი"""
#     number = int(input("მიუთითეთ რიცხვი : "))
#     number1 = int(input("მიუთითეთ რიცხვი რომლის პროცენტი უნდა ვიპოვოთ %d დან : " % number))
#     print("თქვენ გაინტერესებდათ %d ის რამდენი პროცენტია %d\n" % (number, number1))
#     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
#     print("%d არის %d ის %s პროცენტი" % (number1, number, (number1/number)*100))

"""თუ გვინა ვიპოვოთ მოცემული რიცხვის მოცემული პროცენტი"""
# while True:
#     number = int(input("რიცხვი : "))
#     procent = int(input("%d ის რა პროცენტის პოვნა გინდათ? : " % number))
#     if procent > 100:
#         print("არასწორი რიცხვი ცადეთ თავიდან")
#         break
#     print("შენ გაინტერესებდა %d ის რამდენი პროცენტია %d \n" % (number, procent))
#     print("%d ის %d პროცენტი არის %s" % (number, procent, number*(procent/100)))

"""string replace method"""

# def replace_method(text = "Messi Is The Best Footballer In The World"):

#     print(text)
#     which_replaced = input("რისი შეცვლა გინდა? : ")
#     to_replaced = str(input("რითი ცვლი ? : "))
#     string_for_changed_string = ""
#     string_for_changed_letter = ""
#     x = text.split()

#     for i in x:
#         for j in i:
#             if j == which_replaced:
#                 l = []
#                 for t in text:
#                     l.append(t)
#                     if which_replaced == t:
#                         l[l.index(t)] = to_replaced
#                 for r in l:
#                     string_for_changed_letter += r
#         if i == which_replaced:
#              x[x.index(i)] = to_replaced
#     for i in x:
#         i += " "
#         string_for_changed_string += i
#     print(string_for_changed_letter)
#     print(string_for_changed_string)



# replace_method()
""""""
from random import sample
"""შეარჩევს 1000 -ს დადებით ნატურალურ რიცხვს [7, 7000] დიაპაზონიდან და შეინახავს შესაბამისად სიაში (list)
შემდეგ ეს 1000 რიცხვი გადაანაწილეთ 2 სიაშია, ერთი სიაში ჩაწერეთ მხოლოდ კენტები, მეორე სიაში ჩაწერეთ ლუწი რიცხვები.
შემდეგ დაითვალეთ თითოეულის სიის ელემენტების კვადრატების ჯამი და სხვაობა დაბეჭდეთ"""


# natural_number = sample(range(7, 7000), 1000)
# luwi = []
# kenti = []
# for i in natural_number:
#     if i % 2 == 0:
#         luwi.append(i)
#     else:
#         kenti.append(i)
# luwistvis = 1
# kentistvis = 1
# for i in luwi:
#     luwistvis += i**2
# for i in kenti:
#     kentistvis += i**2
# print(luwistvis - kentistvis)

""" 1)"""
# numbers = [1, 2, 3, 4, 5]
# sum = 0
# for i in numbers:
#     if i % 2 != 0:
#         sum += i
# print(sum)

"""2) გაცვალონ ადგილები key,value"""
# test_dict = {"a": "1", "b": "2", "c": "3"}
# l = []
# l1 = []
# for k, v in test_dict.items():
#     l.append(k)
#     l1.append(v)
# test_dict.clear()

# for_key = 0
# for value in l:
#     while for_key < len(l1):
#         test_dict[l1[for_key]] = l[for_key]
#         for_key += 1
# print(test_dict)


# test_dict = {"a":1,"b":2,"c":3}
# new_dict = {k:v for v,k in test_dict.items()}
# print(new_dict)

""" Check Student grade"""

# student_id = {"N123": 67, "N113": 95, "N145": 46, "N234": 32, "N156": 89, "N099": 51}
# def student_with_grade(Id = input("Give Me StudentId : ")):
#     if Id in student_id:
#         for k in student_id:
#             if Id == k:
#                 if 100 >= student_id[k] > 91:
#                     print(student_id[k], 'A')
#                 if 90 >= student_id[k] > 80:
#                     print(student_id[k], 'B')
#                 if 80 >= student_id[k] > 71:
#                     print(student_id[k], 'C')
#                 if 70 >= student_id[k] > 61:
#                     print(student_id[k], 'D')
#                 if 60 >= student_id[k] > 51:
#                     print(student_id[k], 'E')
#                 if 50 >= student_id[k] > 41:
#                     print(student_id[k], 'FX')
#                 if 40 >= student_id[k] > 0:
#                     print(student_id[k], 'F')
#     if Id not in student_id:
#         return student_with_grade(input("Give Me StudentId : "))
# student_with_grade()
""" Count Method """
# string = "დაწერეთ ფუნქცია რომელსაც გადაეცემა სია და რომელიც დააბრუნებს სიის ელემენტების სიხშირეს, ანუ"
# xmovani = "დ"
# count = 0
# for i in string:
#     if xmovani == i:
#         count += 1
# print(count)

"""დაწერეთ ფუნქცია my_power რომელსაც გადაეცემა ორი არგუმენტი base და exponent სადაც base არის არაუარყოფითი მთელი 
ან ათწილადი რიცხვი და exponent არის მთელი არაურყოფით რიცხვი. ამ ფუნქციამ უნდა დააბრუნოს base აყვანილი exponent 
ხარისხში.: """

# def my_power(base = float(input("Number : ")), exponent = int(input("Number : "))):
#     return "my_power(%d, %d) ----> %d" % (base, exponent, base**exponent)
# print(my_power())
""""""
# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
# d = {}
# for i in range(1, 16):
#     d[i] = i**2
# print(d)

"""Write a Python program to sort a given dictionary by key."""
# dict = {1: 1, 5: 25, 3: 9, 4: 16, 2: 4, 0: 10, 6: 22}
# list_for_key = []
# list_for_value = []
# for k, v in dict.items():
#     list_for_key.append(k)
#     list_for_key.sort()
#     list_for_value.append(v)
#     list_for_value.sort()
# print(dict)
# dict.clear()
# for_key = 0
# for value in list_for_value:
#     while for_key < len(list_for_key):
#         dict[list_for_key[for_key]] = list_for_value[for_key]
#         for_key += 1
# print(dict)
""""""
# Make a function to sum the numbers from 1 to 100 and place them in the list
# def sum_numbers():
#     list_for_sum = []
#     for i in range(1, 101):
#         list_for_sum.append(i)
#     return sum(list_for_sum)
# print(sum_numbers())

""""""
# Make a function to add 5 items in the list which will be randomly from 1 to 100
# def add_five_items(list_for_add):
#     for i in range(5):
#         list_for_add.append(random.randint(1, 100))
#     return list_for_add
# print(add_five_items([]))


"""Factorial"""
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

""""""
# Write a program that will check if the transmitted character is vowel or consonant
# def check_vowel_or_consonant(char):
#     if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
#         return "Vowel"
#     else:
#         return "Consonant"
# print(check_vowel_or_consonant("a"))

""""""

# Write a program that calculates the sum of all positive number cubes less than this number for a given number
# def sum_of_positive_number_cubes(n):
#     sum = 0
#     for i in range(1, n):
#         sum += i**3
#     return sum
# print(sum_of_positive_number_cubes(10))

""""""

# make our own list and ask user list size and add integers to it
# def list_for_user():
#     list_for_user = []
#     list_size = int(input("List size : "))
#     for i in range(list_size):
#         list_for_user.append(int(input("Number : ")))
#     return list_for_user
# print(list_for_user())

""""""

# make file and merge 3 lists in it
# def merge_lists(list_1, list_2, list_3):
#     file = open("merge_lists.txt", "w")
#     for i in range(len(list_1)):
#         file.write(str(list_1[i]) + " " + str(list_2[i]) + " " + str(list_3[i]) + "\n")
#     file.close()
# merge_lists([1, 2, 3], [4, 5, 6], [7, 8, 9])

"""calculator"""
# create file and make simple calculator in it with + - * / and % and ask user to enter numbers and operators and print the result
# def calculator():
#     file = open("calculator.txt", "w")
#     while True:
#         num1 = int(input("Number 1 : "))
#         num2 = int(input("Number 2 : "))
#         operator = input("Operator : ")
#         if operator == "+":
#             result = num1 + num2
#         elif operator == "-":
#             result = num1 - num2
#         elif operator == "*":
#             result = num1 * num2
#         elif operator == "/":
#             result = num1 / num2
#         elif operator == "%":
#             result = num1 % num2
#         else:
#             print("Invalid operator")
#             continue
#         file.write(str(num1) + " " + str(operator) + " " + str(num2) + " = " + str(result) + "\n")
#         print(result)
#         if input("Do you want to continue? (y/n) : ") == "n":
#             break
#     file.close()
# calculator()
""""""

# make function to sum all numbers in list
# def sum_list(list):
#     sum = 0
#     for x in list:
#         sum += x
#     return sum
# print(sum_list([1, 2, 3, 4, 5]))




"""1. რომლის კენტ ადგილზე მდგომი ციფრების ჯამი მეტია ლუწ ადგილზე მდგომი
ციფრების ჯამისა
2. რომელიც შეიცავს 3 კენტ ციფრს მაინც"""

# coding=utf-8
# import random
# import json
#
# #  ამოცანა 1
# id_numbers = ["".join(random.sample("00112233445566778899", 11)) for i in range(1000)]
#
#
# # kent adgilze mdgomi cifrebis jami metia luw adgilze mdgomebis jamze
# odd_sum_is_more = []
# for current_id in id_numbers:
#     odd_place_sum = 0
#     even_place_sum = 0
#
#     odd_place_sum += int(current_id[0])
#     odd_place_sum += int(current_id[2])
#     odd_place_sum += int(current_id[4])
#     odd_place_sum += int(current_id[6])
#     odd_place_sum += int(current_id[8])
#     odd_place_sum += int(current_id[10])
#
#     even_place_sum += int(current_id[1])
#     even_place_sum += int(current_id[3])
#     even_place_sum += int(current_id[5])
#     even_place_sum += int(current_id[7])
#     even_place_sum += int(current_id[9])
#
#     if odd_place_sum > even_place_sum:
#         odd_sum_is_more.append(current_id)
#
# print('ამოცანა 1 - 1: რომლის კენტ ადგილზე მდგომი ციფრების ჯამი მეტია ლუწ ადგილზე მდგომი ციფრების ჯამისა - ', len(odd_sum_is_more))
#
#
# # შეიცავს თუარა 3 კენტს მაინც
# id_with_odds = []
# for current_id in id_numbers:
#     odd_count = 0
#     odd_count += current_id.count('1')
#     odd_count += current_id.count('3')
#     odd_count += current_id.count('5')
#     odd_count += current_id.count('7')
#     odd_count += current_id.count('9')
#
#     if odd_count >= 3:
#         id_with_odds.append(current_id)
#
# print('ამოცანა 1 - შეიცავს 3 კენტს მაინც - ამდენი აიდი', len(id_with_odds))

""""""
# Implement a function which receives a string and replaces all `"` symbols with `'`.
# def replaces(string):
#     if '"' in string:
#         return string.replace('"', "'")
#     else:
#         return string.replace("'", '"')
# print(replaces(input("Enter a string: ")))
""""""

l = [   
    {"name": "John", "age": 21},
    {"name": "Jane", "age": 22},
    {"name": "Jack", "age": 22},
    {"name": "Jill", "age": 22},
    {"name": "Joe", "age": 21},
    {"name": "Jenny", "age": 21},
    {"name": "sdds", "age": 21},
    {"name": "sdaads", "age": 24},
    {"name": "Jasdgck", "age": 24},
    {"name": "Jigbvll", "age": 24},
    {"name": "Jadaoe", "age": 25},
    {"name": "Jeyunny", "age": 25}
]
# from pprint import pprint

# l1 = [] # 1 ხერხი
# for i in l:
#     l1.append(i["age"])
# for i in l1:
#     # l1 = list(set(l1))
#     while l1.count(i) > 1:
#         l1.remove(i)
        

# for count in range(len(l1)):
#     print({l1[count]: list(filter(lambda x: x["age"] == l1[count], l))})

# # 2
# def dicts(l , key):
#     new_dict = {}
#     for k in l:
#         if k[key] in new_dict:
#             new_dict[k[key]].append(k)
#         else:
#             new_dict[k[key]] = [k]
#     return new_dict


# pprint(dicts(l, "age"))
""" Simple game """


# capitals = {"georgia": "Tbilisi", "ukraine": "Kiev", "usa": "Washington","Brazil": "Brasilia"}
# question = random.choice(list(capitals.keys()))

# for i in capitals:
#     if i == question:
#         answer = input("What is the capital of {}? ".format(i))
#         if answer.lower() == capitals[i].lower():
#             print("Correct!")
#         else:
#             print("Wrong!")
#             print("The capital of {} is {}".format(i, capitals[i]))
        






































