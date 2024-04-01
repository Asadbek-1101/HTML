# 1 - misol

# def teskari_tartib(listt):
#     teskari_juft = []
#     teskari_toq = []
#     for i in listt:
#         if i > 9 and i%2==0:
#             teskari_juft.append(int(str(i)[::-1]))
#         else:
#             teskari_toq.append(int(str(i)))

#     n = teskari_juft+teskari_toq
#     m = len(teskari_juft+teskari_toq)    

#     for el in range(m):
#         for j in range(0, m-1):
#             if n[j] > n[j+1]:
#                 n[j], n[j+1] = n[j+1], n[j]
#     return n


# print(teskari_tartib([1,21,48,21,48,56,764]))
#----------------------------------------------------------------------------
# 3 - masala

# def buble_sort(tartibsiz_list):
#     n = len(tartibsiz_list)

#     for i in range(n):
#         for j in range(0, n-1):
#             if tartibsiz_list[j] < tartibsiz_list[j+1]:
#                 tartibsiz_list[j+1], tartibsiz_list[j] = tartibsiz_list[j], tartibsiz_list[j+1] 
#     return tartibsiz_list
# print(buble_sort([2,4,5,6,1]))


#---------------------------------------------------------------------
# 4 - masala

# count = 0
# file = open("txt.txt", "r")
# reader = file.read()
# for i in reader.split():
#     i.isalpha()
#     count += 1

# print(count)
# file.close()

#------------------------------------------------------------------------
# 5 - masala

def f(x):
    if len(x)<=140 and x[0] == '#':    
        a = x.title()
        b = a.replace(' ', '')
        return b
    else:
        return False
print(f('# Hello world salom dunyo'))

























