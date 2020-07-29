#Python3  code to demonstrate

#swap of key and value no

#initializing dictionary

old_dict={21:"FTP",22:"SSH",23:"telnet",80:"http"}
          
new_dict=dict([(value,key)for key,value in old_dict.items()])
          
#Printing original dictionary
print("original dictionary is:")
          
print(old_dict)
          
print()
#Printing new dictionary after swapping keys and values
print("dictionary after swapping is :")  
          
print("keys:values")
for i in new_dict:
          print(i,":",new_dict[i])
          
          
   
#OUTPUT   
original dictionary is:
{21: 'FTP', 22: 'SSH', 23: 'telnet', 80: 'http'}

dictionary after swapping is :
keys:values
FTP : 21
SSH : 22
telnet : 23
http : 80