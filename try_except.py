# # 1-masala
# def count_passing_students(grades, passingGrade):
#     count=0
#     for ball in grades:
#         try:
#             if ball<0: 
#                 raise ValueError("ball musbat bo'lishi kerak!")
#             elif ball>100:
#                 raise ValueError("ball<=100")
#             elif ball >= passingGrade:
#                 count+=1
#         except ValueError as xato:
#             print(xato)


#     return count


# grades = [45, 60, 75, 30, -100,90]
# passingGrade = 60
# print(count_passing_students(grades, passingGrade))
# # Output: 3

# 2-masala

# def ends_with_gram(words):
#     natija=[]
#     for word in words:
#         try:
#             if type(word)==int or type(word)==float:
#                 raise ValueError("so'z bo'ishi kerak!")
#             if word.lower().endswith("gram"):
#                 natija.append(word)
#         except ValueError as xato:
#             print(xato)
#     return natija
# words = ["telegram", "Instagram", "hello", "program", "diagram", "world"]
# print(ends_with_gram(words))
# # Output: ['telegram', 'Instagram', 'program', 'diagram']

#  3talikdan 1-masala

# def find_top_three_numbers_sorted(data):

#     natija=[]
#     for guruh in data:
#         try:
#             if type(guruh)==int or type(guruh)==str:
#                 raise ValueError(f"tuple bo'lishi kerak {guruh}")
#             else:
#                 lst=list(guruh)
#                 tartiblangan=sorted(lst, reverse=True)
#                 tartiblangan=tuple(tartiblangan[:3])
#                 natija.append(tartiblangan)
#         except ValueError as xato:
#             print(xato)
#     return natija


# data = [(10, 20, 30, 11), (5, 15), (40,), (7, 8, 50, 3)]
# print(find_top_three_numbers_sorted(data))
# # Output: [(30, 20, 11), (15, 5), (40,), (50, 8, 7)]

#  3talikdan 4-masala

# def calculate_painting_time(pattern):
#     vaqt=0
#     for i in range(len(pattern)):
#         try:
#             if type(pattern[i])==int or type(pattern[i])==float:
#                 raise ValueError("rang str bo'lishi shart!")
#             else:
#                 if i==0:
#                     vaqt+=2
#                 else:
#                     if pattern[i]!=pattern[i-1]:
#                         vaqt+=3
#                     else:
#                         vaqt+=2

#         except ValueError as error:
#             print(error)
#     return vaqt        



# pattern = ["Red", "Blue", "Red", "Blue", "Red","Blue","Blue",21] 
# print(calculate_painting_time(pattern)) 
# # Output: 14

