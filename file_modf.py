import pickle
def readpy_file():
    file_read=open('libssh.py')
    return file_read.readlines()

def line_sequencer(lines_in_file):
    file_pickle_load=open('parser_dump','rb')
    pickle_data=pickle.load(file_pickle_load)
    print (pickle_data)
    new_codetow=[]
    for key in pickle_data:
       for li in list(pickle_data[key]):
           print(li)
           try:
               print ("Indentation:",int(li[1]),"LineNo:",int(li[0]),"Code:",lines_in_file[int(li[0])-1])
               indentation=int(li[1])
               line_number=int(li[0])
               code=lines_in_file[int(li[0])-1]
               if indentation==2:
                   lines_in_file[int(li[0])-1]=lines_in_file[int(li[0])-1]+'\n'+'print(locals())\n'
                   #new_codetow.append(code)
               else:
                   lines_in_file[int(li[0])-1]=lines_in_file[int(li[0])-1]+'\n'+" "*(indentation-2)+'print(locals())\n' 
                  # new_codetow.append(code)   
           except:
               pass
    return lines_in_file

def writepy_file(new_codetow):
    file_write=open("write.py",'w')
    file_write.writelines(new_codetow)
    file_write.close()




lines_in_file=readpy_file()    
new_codetow=line_sequencer(lines_in_file)
writepy_file(new_codetow)
