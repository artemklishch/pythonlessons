f1 = open('file1.txt', 'r', encoding='utf-8')
# text1 = f1.read(1)
# text2 = f1.read(8)
print(f1.encoding)
text3 = f1.read()
f1.close()

# print(text1)
# print(text2)
print(text3)

print('\n')
# f2 = open('file2.txt', 'a', encoding='utf-8')
# text4 = f2.write("New String\n")
# f2.close()
# print(text4)

# lines = ['New strin 1', "New string 2"]
# f3 = open('file2.txt', 'a', encoding='utf-8')
# # for str in lines:
# #     f3.write(str + '\n')
# # f3.writelines(lines)
# f3.writelines(f'{i}\n' for i in lines)
# f3.close()

f4 = open('file2.txt', 'r', encoding='utf-8')
# for line in f4:
#     print(line.replace("\n", ""))
text5 = f4.readlines()
# text6 = f4.readline()
print(text5)
# print(text6)
f4.close()
