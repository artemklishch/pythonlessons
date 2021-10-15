# import os

# root_folder = os.getcwdb()
# folder = []


# def create_files():
#     if not os.path.isdir('folder1'):
#         os.mkdir('folder1')
#         os.mkdir('folder1/folder11')
#         text_file1 = open('folder1/folder11/text11.txt', 'w')
#         text_file1.write("number 11")
#         os.mkdir('folder1/folder12')
#         text_file2 = open('folder1/folder12/text12.txt', 'w')
#         text_file2.write("number 12")
#         tree = os.walk(root_folder)
#         for i in tree:
#             print(i)
#     else:
#         tree = os.walk(root_folder)
#         for rootfolder in tree:
#             [a, b, c] = rootfolder
#             print(a.decode("utf-8") )
#             if len(b) > 0:
#                 for nestedfolder in b:
#                     print(a.decode("utf-8") + "/" +
#                           nestedfolder.decode("utf-8"))
#             if len(c) > 0:
#                 for file in c:
#                     print(a.decode("utf-8") + "/" + file.decode("utf-8"))


# create_files()
import os


def read_dir(folder):
    for root, dirs, files in os.walk(folder):
        level = root.count(os.sep)
        indent = ' ' * 4 * level
        print(f'{indent}[{os.path.basename(root)}]')
        sub_indent = ' ' * 4 * (level + 1)
        for file in files:
            print(f'{sub_indent}[{file}]')
        # print(root, files, level)


read_dir('folder2')
# tree1 = os.walk('folder2')
# for files in tree1:
#     print(files)
