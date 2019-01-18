import keyword
file_data=open('input.txt').readlines()
file_name_line={}
func_or_express=False
#print (file_data)

for li in file_data:
    #print li.fi
   # print(li[li.find('(')+1:li.find(')')])

   # print("Filename",li[:li.find('(')])
    line_number=int(li[li.find('(')+1:li.find(')')])
    #print(line_number)
    for keywords in keyword.kwlist:
        if (keywords+' ' in li) or (keywords+':' in li):
            #print (keywords,li)
            temp_list=[]
            temp_list.append(li[:li.find('(')])
            temp_list.append('keyword')
            file_name_line[line_number]=temp_list
    #print (li)
        else: 
            temp_list=[]
            temp_list.append(li[:li.find('(')])
            temp_list.append('statement')
            file_name_line[line_number]=temp_list

    #print ()
print(file_name_line)