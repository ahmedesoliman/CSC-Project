'''
Final Project - CSC 101 0502[66785] (Borough of Manhattan CC)

Student Name - Ahmed Soliman
'''
#method to remove '\n' characters from a list
def remove_new_line_char_from_list(data):
    i=0
    #looping until i exceeds the last index
    while i<len(data):
        #if element at i is '\n', popping it
        if data[i]=='\n':
            data.pop(i)
        #otherwise incrementing i
        else:
            i+=1

#method to remove new line character from each string in the list
def remove_new_line_char_from_string(data):
    #looping through each index
    for i in range(len(data)):
        #replacing '\n' with empty string and assigning to original string
        data[i]=data[i].replace('\n','')


#method to modify element with value = 'name' to new_name
def modify_name(data, new_name):
    # looping through each index
    for i in range(len(data)):
        #if current element is 'name', changing it to new_name
        if data[i]=='name':
            data[i]=new_name


#main method
def main():
    #using try-except, opening info.txt in read mode
    try:
        file=open('info.txt','r')
    except:
        #exception occurred, displaying error and quitting
        print('File not found')
        exit(0)
    #if no exception occurred, reading lines into a list and closing file
    lines=file.readlines()
    file.close()
    #printing the list
    print('list of lines:',lines)
    #removing '\n' and printing the list
    remove_new_line_char_from_list(lines)
    print('after removing newlines:',lines)
    # removing '\n' from each string and printing the list
    remove_new_line_char_from_string(lines)
    print('after removing newline characters from each string:', lines)
    # changing 'name' to 'Oliver Queen' (change as you like) and printing the list
    modify_name(lines,'Oliver Queen')
    print('after replacing "name" with "Oliver Queen":', lines)


#calling main()
main()


Second answer
# data1 = []
# try:
#   myfile = open("info.txt")
#   data1 = myfile.readlines()
#   myfile.close()
# except: 
#   print("File not found")
# print (data1)

# def remove_new_line_char_from_list (lst):
#   i = 0
#   ls = lst
#   while i < len(ls):
#     if ls[i] == '\n':
#       ls.pop(i)
#     i += 1
#   print(data1)

# remove_new_line_char_from_list (data1)

# data2 = []
# def remove_new_line_char_from_string (lst):
#   for element in lst:
#     data2.append(element.strip())
#   print (data2)

# remove_new_line_char_from_string (data1)

# data3 = []
# def modify_name (lst, your_name):
#   for string in data2:
#     data3.append(string.replace("name", your_name))
#   print(data3)

# modify_name (data2, "Ahmed Soliman")
