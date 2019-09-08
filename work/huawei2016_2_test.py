# coding = gbk
# import sys
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))
#
# output_list = []
# filename_dict = {}
# while True:
#     s = input()
#     if s == '':
#         break
#     else:
#         s = list(s.split())
#         file_name = list(s[0].split('\\'))[-1]
#         filename = file_name + ' ' + s[1]
#         if filename not in filename_dict:
#             filename_dict[filename] = 1
#         else:
#             num = filename_dict[filename] + 1
#             filename_dict[filename] = num
#             if len(file_name) > 16:
#                 file_name = file_name[-16:]
#             output_list.remove(file_name + ' ' + s[1] + " " + str(filename_dict[filename]-1))
#         if len(file_name) > 16:
#             file_name = file_name[-16:]
#         output = file_name + ' ' + s[1] + " " + str(filename_dict[filename])
#         output_list.append(output)
#
# for i in range(len(output_list)):
#     print(output_list[i])

output_list = []
filename_dict = {}
import sys
for line in sys.stdin:
    if ord(line[0]) == 10:
        break
    else:
        s = list(line.split())
        file_name = list(s[0].split('\\'))[-1]
        filename = file_name + ' ' + s[1]
        if filename not in filename_dict:
            filename_dict[filename] = 1
        else:
            num = filename_dict[filename] + 1
            filename_dict[filename] = num
            if len(file_name) > 16:
                file_name = file_name[-16:]
            output_list.remove(file_name + ' ' + s[1] + " " + str(filename_dict[filename]-1))
        if len(file_name) > 16:
            file_name = file_name[-16:]
        output = file_name + ' ' + s[1] + " " + str(filename_dict[filename])
        output_list.append(output)

for i in range(len(output_list)):
    print(output_list[i])
