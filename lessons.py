# # ml = [10,20,30,40,0,50,60]
# # for el in ml:
# #     try:
# #         print(120/el)
# #     except ZeroDivisionError:
# #         print("Can not divite in 0")
# # print('End of the code')



# # def get_content(filename):
# #     try:
# #         with open(filename, 'r') as file:
# #             return file.readlines()
# #     except FileNotFoundError:
# #         print('please provide a file')
# #         exit()
  
# # def print_square(data):
# #     for el in data:
# #         tmp = el.replace('\n','')
# #         try:
# #             print(int(el)**2)
# #         except ValueError:
# #             pass

# # def main():
# #     filename = input()
# #     cnt = get_content(filename)
# #     print_square(cnt)

# # if __name__ == "__main__":
# #     main()


# # def rupper(str):
# #     if len(str) == 0:
# #         return ""
# #     return str[0].upper() + rupper(str[1:])
# # print(rupper('dbhdbh'))


# # def rreverse(str):
# #     if not str:
# #         return ""
# #     return str[-1] + rreverse(str[0:-1])
# # print(rreverse("Hello"))


# # def rsum(numbers):
# #     summ = 0
# #     if numbers == 0:
# #         return 0
# #     return numbers%10 + rsum(numbers//10)
# # print(rsum(12345))


# # def f(mstr):
# #     md = {}
# #     for i in mstr:
# #         if i.isalpha():
# #             if i not in md:
# #                 md[i] = 1
# #             else:
# #                 md[i] += 1
# #     ml = list(md.items())
# #     ml.sort(key=lambda x : x[1])
# #     return ml[0], ml[-1]
# # print(f('hello'))


# # ml1 = [1, 2, 4, 5, 6]
# # ml2 = [2, 3, 4, 5, 6]

# # not_in = []
# # is_in = []
# # for i in ml1:
# #     if i not in ml2:
# #         not_in.append(i)
# #     else:
# #         is_in.append(i)
# # for j in ml2:
# #     if j in ml1 and j not in kan:
# #         is_in.append(j)
# #     elif j not in ml1:
# #         not_in.append(j)
# # print(not_in)
# # print(is_in)

# # ml1 = set(ml1)
# # ml2 = set(ml2)



# def get_content(fname):
#     try:
#         with open(fname) as f:
#             return f.readlines()
#     except FileNotFoundError:
#         print("Provide real file")
#         exit()

# def create_list(ml):
#     md = {}
#     for line in ml:
#         md[line.strip()] = "voted"
#         return md
    
# def allow_voting(md, fulln, fname):
#     if fulln in md:
#         print("Arrest")
#     else:
#         write_into_file(fname, fulln)

# def write_into_file(fname, fulln):
#     with open(fname, "a") as f:
#         f.write(fulln + "\n")

# def main():
#     filename = "votes.txt"
#     voted = get_content(filename)
#     voters = create_list(voted)
#     name = input()
#     surname = input()
#     full_name = name + " " + surname
#     allow_voting(voters, full_name, filename)
# main()

# def f():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5

##variant 1
# a = f()
# print(next(a))
# print(next(a))

##variant 2
# for el in a:
#     print(el)


# def f(mstr):

#     for el in mstr:
#         if el.isalpha():
#             yield el.upper()

# mstr = "Hello 1234 world"
# for el in f(mstr):
#     print(el)



# def roman_to_integer(str):
#     roman_to_int = {
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000
#     }


# mstr = input()
# while "()" in mstr or "[]" in mstr or "{}" in mstr:
#     mstr = mstr.replace("()", "")
#     mstr = mstr.replace("{}", "")
#     mstr = mstr.replace("[]", "")
# if len(mstr) == 0:
#     print("True")
# else:
#     print("False")



# md = {
#     'TO DO': ['Task 2', 'Task 4', 'Task5'],
#     'IN PROGRESS': ['Task 1', 'Task 6'],
#     'REVIEW': ['Task 3'],
#     'DONE': []
#     }


# print("Which tasks do you want to see?")
# answer1 = input("TO DO, IN PROGRESS, REVIEW, DONE or ALL: ").upper()
# if answer1 == "ALL":
#     for k,v in md.items():
#         print(f"{k} : {v}")
# else:
#     print(f"{answer1} : {md[answer1]}")

# print("Which tasks do you want to deal with?")
# answer2 = input("TO DO, IN PROGRESS, REVIEW or DONE: ").upper()
# print(f"{answer2} : {md[answer2]}")
# answer2_2 = input('Choose Task: ')

# answer3 = input("Where to move: ").upper() 
# if answer2.upper() == answer3.upper():
#     print(f"{answer2_2} in {answer2}")
#     answer3 = input("Choose another task: ")
# else:
#     md[answer2].remove(answer2_2)
#     md[answer3].append(answer2_2)
# print(md)

# filname = 'tasks.txt'
# with open(filname, 'w') as file:
#     for k, v in md.items():
#         file.write(k + "    " + "\n")
#         for i in v:
#             file.write(i + "    " + "\n")


##############################################


# class Human:
#     def __init__(self, n, s, b):
#         self.name = n
#         self.surname = s
#         self.birth_year = b
#     def speak(self, mstr = "hello"):
#         print(mstr)
#     def __str__(self):
#         return self.name + " " + self.surname

# h1 = Human("John", "Smith", 1999)
# print(h1)

##############################################


# class Human:
#     def __init__(self, n):
#         self.name = n
#         self.age = 18
#     def __repr__(self):
#         return self.name 

#     def __gt__(self, other):
#         return self.age>other.age

# h1 = Human("John")
# h2 = Human("James")
# h3 = Human("Bella")
# # if h1>h2:
# #     print(h1.name)
# # else:
# #     print(h2.name) 

# humans = [h1, h2, h3]
# humans.sort()
# print(humans)

##############################################


# class Number:
#     def __init__(self, n=0):
#         self.__num = n

#     @property
#     def num(self):
#         return self.__num

#     @num.setter
#     def num(self, n):
#         self.__num = n

#     def __add__(self, other):
#         return Number(self.__num + other.__num)
#     def __str__(self):
#         return str(self.__num)
#     def __sub__(self, other):
#         return Number(self.__num - other.__num)
#     def __gt__(self, other):
#         return self.__num > other.__num


# if __name__=="__main__":
#     n1 = Number(10)
#     n2 = Number(20)
#     n3 = n1 + n2
#     print(n3)
#     n3 = n1 - n2
#     print(n3)
#     print(n1>n2)



##############################################





# class Stack:
#     def __init__(self, c):
#         self.count = c
#         self.ml = []

#     def __str__(self):
#         return str(self.ml)

#     def push(self, num):
#         if len(self.ml) >= self.count:
#             print("No space for new element")
#         else:
#             self.ml.append(num)
    
#     def pop(self):
#         if not self.ml:
#             print("No element to remove")
#         else:
#             return self.ml.pop()


# s = Stack(5) 
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4) 
# s.push(5)
# print(s)
# print(s.pop()) 
# print(s.pop())  
# print(s.pop()) 
# print(s.pop()) 
# print(s.pop()) 

##############################################

# import time
# import random

# count = int(input("Enter working time"))
# i = 0
# md = {}
# while i < count:
#     num = random.randint(1, 91)
#     print(num)
#     if num in md:
#         md[num] += 1
#     else:
#         md[num] = 1
#     time.sleep(1)
#     i += 1
# ml = list(md.items())
# ml.sort(key=lambda x:x[1])
# print(ml[-1][0])




##################################

# class University:
#     def __init__(self, n, l, y, c):
#         self.name = n
#         self.location = l
#         self.setup_year = int(y)
#         self.student_count = int(c)

#     def __repr__(self):
#         return f"{self.name}    {self.location}    {self.setup_year}    {self.student_count:,}"


# def read_universities(file_path):
#     universities = []
#     with open(file_path, "r") as file:
#         for line in file:
#             parts = line.strip().split("    ")
#             if len(parts) == 4:
#                 universities.append(University(*parts))
#     return universities


# def write_sorted_universities(file_path, universities):
#     with open(file_path, "w") as file:
#         for uni in universities:
#             file.write(str(uni) + "\n")


# def sort_universities(universities, key):
#     return sorted(universities, key=lambda x: getattr(x, key))


# def main():
#     input_file = "university.txt"
#     output_file = "sorted_university.txt"
    
#     universities = read_universities(input_file)
    
#     sort_key = input("Enter sorting key (name, location, setup_year, student_count): ")
#     if sort_key not in ["name", "location", "setup_year", "student_count"]:
#         print("Invalid key.")
    
#     universities = sort_universities(universities, sort_key)
#     write_sorted_universities(output_file, universities)
#     print("Sorting complete. Check sorted_university.txt")


# if __name__ == "__main__":
#     main()

# #############################


# class Stack:
#     def __init__(self, c):
#         self.count = c
#         self.ml = []
#         self.index = 0  

#     def __str__(self):
#         return str(self.ml[self.index:])  

#     def push(self, num):
#         if len(self.ml) - self.index >= self.count:
#             print("No space for new element")
#         else:
#             self.ml.append(num)  

#     def pop(self):
#         if self.index == len(self.ml):
#             print("No element to remove")
#         else:
#             val = self.ml[self.index] 
#             self.index += 1  
#             return val


# q = Stack(5)
# q.push(1)
# q.push(2)
# q.push(3)
# print(q)

# q.push(4)
# print(q)
# q.push(5)
# print(q)
# print(q.pop()) 
# print(q) 
# print(q.pop()) 
# print(q) 
# print(q.pop())  
# print(q.pop())  
# print(q.pop())  


################################


# class Human:
#     def __init__(self, a):
#         self.__age = a

#     def get_age(self):
#         return self.__age

#     def set_age(self, a):
#         if type(a) != int or (a > 160 or a<0):
#             self.__age = 1
#         else:
#             self.__age = a

# h1 = Human(30)
# h1.set_age(90)
# print(h1.get_age())




# class Human:
#     def __init__(self, a):
#         self.__age = a

#     @property
#     def age(self):
#         return self.__age

#     @age.setter
#     def age(self, a):
#         if type(a) != int or (a > 160 or a<0):
#             self.__age = 1
#         else:
#             self.__age = a

# h1 = Human(18)
# h1.age = 35
# print(h1.age)
# h1.age = 3500
# print(h1.age)


########################################

# class MString:
#     def __init__(self, mstr):
#         self.string = mstr

#     def split(self):
#         result = []
#         word = ''
        
#         for i in self.string:
#             if i == ' ':
#                 if word: 
#                     result.append(word)
#                     word = ''
#             else:
#                 word += i
        
#         if word:
#             result.append(word)
        
#         return result

# mstr = MString("Hello world")
# print(mstr.split()) 


# class MString:
#     def __init__(self, string):
#         self.s = string
    
#     def upper(self):
#         result = ""
#         for i in self.s:
#             if 'a' <= i <= 'z': 
#                 result += chr(ord(i) - 32) 
#             else:
#                 result += i  
#         return result

# mstr = MString("hello")
# print(mstr.upper())  


# class MString:
#     def __init__(self, string):
#         self.s = string
    
#     def lower(self):
#         result = ""
#         for i in self.s:
#             if 'A' <= i <= 'Z':  
#                 result += chr(ord(i) + 32)  
#             else:
#                 result += i  
#         return result

# mstr = MString("HELLO")
# print(mstr.lower())  


# class MString:
#     def __init__(self, string):
#         self.s = string
    
#     def is_digit(self):
#         digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        
#         if not self.s:
#             return False
        
#         for i in self.s:
#             if i not in digits:
#                 return False
        
#         return True

# print(MString("123").is_digit())  
# print(MString("123a").is_digit()) 


# class MString:
#     def __init__(self, string):
#         self.s = string
    
#     def is_alpha(self):
#         alphabets = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
#                      'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
        
#         if not self.s:
#             return False
        
#         for i in self.s:
#             if i not in alphabets:
#                 return False
        
#         return True

# print(MString("abc").is_alpha())
# print(MString("abc123").is_alpha()) 


# class MString:
#     def __init__(self, t):
#         self.text = t
    
#     def count(self, x):
#         count = 0
        
#         for i in range(len(self.text) - len(x) + 1):
#             if self.text[i:i + len(x)] == x:
#                 count += 1
#         return count

# my_string = MString("hello world, hello")
# x = "hello"
# print(my_string.count(x))


# class MString:
#     def __init__(self, t):
#         self.text = t

#     def replace(self, x1, x2):
#         result = ""
#         i = 0
#         while i < len(self.text):
#             if self.text[i:i+len(x1)] == x1:
#                 result += x2
#                 i += len(x1)  
#             else:
#                 result += self.text[i]
#                 i += 1
#         return result

# my_string = MString("I like apples")
# x1 = "apples"
# x2 = "bananas"
# print(my_string.replace(x1, x2))


# class MString:
#     def __init__(self, t):
#         self.text = t

#     def endswith(self, x):
#         if self.text[len(self.text)-len(x):] == x:
#             return True
#         else:
#             return False

# my_string = MString("Hello, welcome to my world.")
# x = "my world."
# print(my_string.endswith(x))


# class Polygon:
#     def __init__(self, *args):
#         self.sides = list(args)

#     def perimeter(self):
#         return sum(self.sides)

#     def area(self):
#         pass


# class Rectangle(Polygon):
#     def __init__(self, *args):
#         if len(args) != 2:
#             self.sides = [1,1]
#         else:
#             super().__init__(*args)

#     def perimeter(self):
#         return 2 * sum(self.sides)

#     def area(self):
#         return self.sides[0]*self.sides[1]


# class Triangle(Polygon):
#     def __init__(self, *args):
#         if len(args) != 3:
#             self.sides = [1,1,1]
#         else:
#             super().__init__(*args)

#     def area(self):
#         a,b,c = self.sides[0], self.sides[1], self.sides[2]
#         p = (a + b + c) // 2
#         return pow(p*(p-a)*(p-b)*(p-c),0.5)

        
# r1 = Rectangle(10, 20)
# print(r1.perimeter())
# print(r1.area())
# t1 = Triangle(15, 20, 30)
# print(t1.perimeter())
# print(t1.area())
        
