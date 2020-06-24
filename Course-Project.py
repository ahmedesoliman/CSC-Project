'''
Final Project - CSC 101 0502[66785] (Borough of Manhattan CC)

Student Name - Ahmed Soliman
'''

def remove_new_line_char_from_list (lst):
  i= 0
  while i<len (lst):
    if lst[i] == '\n':
      lst.pop(i)
    else:
      i += 1

def remove_new_line_char_from_string(lst):
  for i in range(len(lst)):
    lst[i] = lst[i].replace('\n','')

def modify_name(lst, your_name):
  for i in range(len(lst)):
    if lst[i] == 'name':
      lst[i] = your_name

def main():
  try:
    file=open('info.txt','r')
  except:
    print('File not found')
    exit(0)

  data=file.readlines()
  file.close()
  print(data)
  
  remove_new_line_char_from_list(data)
  print(data)
  remove_new_line_char_from_string(data)
  print(data)
  modify_name(data,'Ahmed Soliman')
  print(data)

main()
