import keyword
import re
file_data=open('input.txt').readlines()
file_name_line={}

#print (file_data)
try:
 for keywords in keyword.kwlist:
    for li in file_data:
        if (keywords+' ' in li) :
          if (li.replace('\n','').replace(' ','').endswith(':')):  
            temp_list=[]
            line_number=int(li[li.find('(')+1:li.find(')')])
            temp_list.append(li[:li.find('(')])
            temp_list.append('keyword')
            file_name_line[line_number]=temp_list
except:
    pass            

key=file_name_line.keys()
regex = r":\s{1,}"
try:
 for li in file_data:
    try:
     line_number=int(li[li.find('(')+1:li.find(')')])
    except:
        pass 
    if line_number not in key:
        temp_list=[]
        matches = re.finditer(regex, li, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            indentation=match.end()-match.start()
            #print (li)
            #print (indentation)
            inject_code="print (lol)"
            print(li+" "*match.end()+inject_code)
            temp_list.append(indentation)
             
       
        temp_list.append(li[:li.find('(')])
        temp_list.append('statement')
        file_name_line[line_number]=temp_list
except Exception as e:
    print(e)       







            

print(file_name_line)

#for i  in range(0,len(file_data)):
    #print li.fi
   # print(li[li.find('(')+1:li.find(')')])

   # print("Filename",li[:li.find('(')])
   # line_number=int(file_data[i][file_data[i].find('(')+1:file_data[i].find(')')])
    #print(file_data[i]ne_number)
   # for keywords in keyword.kwlist:
   #     if (keywords+' ' in file_data[i]) or (keywords+':' in file_data[i]):
            #print (keywords,file_data[i])
   #         temp_list=[]
   #         temp_list.append(file_data[i][:file_data[i].find('(')])
   #         temp_list.append('keyword')
   #         file_name_line[line_number]=temp_list
   #         i=i+1
    #print (li)
    # else: 
    #        temp_list=[]
    #        temp_list.append(li[:li.find('(')])
    #        temp_list.append('statement')
    #        file_name_line[line_number]=temp_list

    #print ()
#print(file_name_line)