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



def get_tasks():
    md = {
        'TO DO': ['Task 2', 'Task 4', 'Task5'],
        'IN PROGRESS': ['Task 1', 'Task 6'],
        'REVIEW': ['Task 3'],
        'DONE': []
    }
    return md

print("Which tasks do you want to see?")
answer1 = input("TO DO, IN PROGRESS, REVIEW, DONE or ALL: ").upper()
for k,v in get_tasks().items():
    if answer1 == k:
        print(get_tasks()[k])
    elif answer1 == "ALL":
        print(get_tasks()[k])
        
print("Which tasks do you want to deal with?")
answer2 = input("TO DO, IN PROGRESS, REVIEW or DONE: ")
for k,v in get_tasks().items():
    if answer2 == k:
        print(get_tasks()[k])
        answer2_2 = input('Choose Task: ')


