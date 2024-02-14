from morsecodelist import morse_code_list

user_input = input("Please, enter the text you want to convert into morse code: ").upper()
print("Warning: '/' indicates the spaces between words.")
# print(user_input)
user_input_list = []
for letter in user_input:
    if letter == " ":
        letter = "/"
        user_input_list.append(letter)
    else:
        user_input_list.append(letter)
# Control statement
# print(user_input_list)
morse_code_item = []
morse_code_value = []
morse_code = []
i = 0
for item, value in morse_code_list.items():
    # print("{} = {}".format(item,value))
    morse_code_item.append(item)
    morse_code_value.append(value)


for i in range(0, len(user_input_list)):
    for index_num in range(0, len(morse_code_item)):
        if user_input_list[i] == morse_code_item[index_num]:
            if user_input_list[i] == "/":
                morse_code.append(user_input_list[i])
                morse_code.append(" ")
            else:
                morse_code.append(morse_code_value[index_num])
                morse_code.append(" ")

# control statement
# print(morse_code)
morse_input = "".join(morse_code)
print(f"Result = {morse_input}.")
