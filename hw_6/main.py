import json
tuples_list = []

#1
with open('nginx_logs.txt', 'r', encoding='utf-8') as file1:
    for line in file1:
        line = line.replace('"', '')
        line = line.replace('-', '')
        line_split = line.split()
        temp_addr = line_split[0]
        temp_req_type = line_split[3]
        temp_file_path = line_split[4]
        temp_tuple = (temp_addr, temp_req_type, temp_file_path)
        tuples_list.append(temp_tuple)




#3
with open('users.csv', 'r', encoding='utf-8') as file2:

    names_content = file2.read()
    names_content.replace(',', ' ')
    names = names_content.splitlines()

with open('hobby.csv', 'r', encoding='utf-8') as file3:

    hobbies_content = file3.read()

    hobbies = hobbies_content.splitlines()

i = 0
dict_data = {}
while i < len(names):
    if i > len(hobbies) - 1:
        temp_dict = {names[i]: None}
    else:
        temp_dict = {names[i] : hobbies[i]}
        dict_data.update(temp_dict)
    i += 1

dict_data_as_str = json.dumps(dict_data)

# with open('user-hobby.txt', 'w', encoding='utf-8') as f:
#     f.write(dict_data_as_str)




