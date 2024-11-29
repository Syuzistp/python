# ml = [10,20,30,40,0,50,60]
# for el in ml:
#     try:
#         print(120/el)
#     except ZeroDivisionError:
#         print("Can not divite in 0")
# print('End of the code')



# def get_content(filename):
#     try:
#         with open(filename, 'r') as file:
#             return file.readlines()
#     except FileNotFoundError:
#         print('please provide a file')
#         exit()
  
# def print_square(data):
#     for el in data:
#         tmp = el.replace('\n','')
#         try:
#             print(int(el)**2)
#         except ValueError:
#             pass

# def main():
#     filename = input()
#     cnt = get_content(filename)
#     print_square(cnt)

# if __name__ == "__main__":
#     main()


# def rupper(str):
#     if len(str) == 0:
#         return ""
#     return str[0].upper() + rupper(str[1:])
# print(rupper('dbhdbh'))


# def rreverse(str):
#     if not str:
#         return ""
#     return str[-1] + rreverse(str[0:-1])
# print(rreverse("Hello"))


# def rsum(numbers):
#     summ = 0
#     if numbers == 0:
#         return 0
#     return numbers%10 + rsum(numbers//10)
# print(rsum(12345))


# def f(mstr):
#     md = {}
#     for i in mstr:
#         if i.isalpha():
#             if i not in md:
#                 md[i] = 1
#             else:
#                 md[i] += 1
#     ml = list(md.items())
#     ml.sort(key=lambda x : x[1])
#     return ml[0], ml[-1]
# print(f('hello'))

popoxutyun
property