import pickle
import os
import pickle
# os.mkdir("D:\\filedirectory")
os.chdir("D:\\filedirectory")

list1 = ["a","b","c"]
file = open("D:\\filedirectory\\file.txt","wb+")
# os.remove("D:\\filedirectory\\file.pdf")
pickle.dump(list1,file)
file.seek(2,0)
print(file.tell())
with open("file.txt","rb") as file1:
   load_list = pickle.load(file1)
   print(load_list)
