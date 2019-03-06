from Tkinter import *
import pickle

stack_list=[]
mem_list=[]
reg_list=[]
count=0





class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.master.title("PycodeIn")
       


        for r in range(6):
            self.master.rowconfigure(r, weight=1)    
       
        #self.master.columnconfigure(c, weight=1)
        



         
        Frame1 = Frame(master)
        scrollbar1=Scrollbar(Frame1)
        Frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S) 
        scrollbar1.pack(side=RIGHT,fill=Y)
        text1=Text(Frame1,width=100,height=35,yscrollcommand = scrollbar1.set)
 
        

        
        
      
         
         
        text1.insert(INSERT,"Python Code:"+'\n')
      
        temp_reverse=final_instr.reverse()
        temp_func_name=final_instr.pop()
        text1.insert(INSERT,temp_func_name+':\n')
        final_instr.pop()
        final_instr.reverse()
        print final_instr
       
        with open('write.py') as fi:
           final_ips=fi.readlines()
        final_ips.pop()
        print final_ips
        for i  in range(0,len(final_ips)):
           try:
              text1.insert(INSERT,final_ips[i]+"     "+final_instr[i]+"   "+'\n')
           except:
                pass
        
  
        text1.insert(END,"")
        
        text1.pack(side=LEFT)
       


        Frame3 = Frame(master)
        scrollbar3=Scrollbar(Frame3)
        scrollbar3.pack(side=RIGHT,fill=Y)
        text3=Text(Frame3,width=90,height=35,yscrollcommand = scrollbar3.set)
        text3.insert(INSERT,"Registers:"+"\n")
        global regis_local
      
        #text3.insert(INSERT,regis_list)
        text3.insert(END,"")
        text3.pack(side=LEFT)

       
        
        def key_up(event,reg_list):
             global count
            
             print (count)
        
          
             #print reg_list
             text3.delete("1.0",END)
             text3.insert(INSERT,"Register:"+"\n")
             
             print "pressed Up", repr(event.char)
             if count==0 or count < 0:
                  text3.insert(INSERT,reg_list[0])
                 
             elif count<len(reg_list):
                  text3.insert(INSERT,reg_list[count-1])
             
                  count=count-1
                    
            
             
             
        def key_down(event,reg_list):
             global count
             text3.delete("1.0",END)
             text3.insert(INSERT,"Register:"+"\n")
             
            
              
             print "pressed Down",repr(event.char)
             print (count,reg_list[count])
             if count==len(reg_list):
                   text3.insert(INSERT,reg_list[count-1])
               
                 
                   count=len(reg_list)-1
                   
             else:
               text3.insert(INSERT,reg_list[count])
              
               count=count+1
        global reg_list
        text1.bind("<Up>",lambda event:key_up(event,reg_list))
        text1.bind("<Down>",lambda event:key_down(event,reg_list))
        




root = Tk()

with open('timedebug.txt') as r:
          
           reg_list=r.read()
           reg_list=reg_list.split('##')

with open('write.py') as f:
          final_instr=f.readlines()



app = Application(master=root)
app.mainloop()
