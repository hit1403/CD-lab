import collections
f = open("file3.txt","r",encoding='utf-8')
count=0
dict_res = collections.defaultdict(list)

for line in f.readlines():
  #print(line)
  if line == "main()\n":
    break

  storeList = line.split(" ")
  #print(line[-2])
  if line[-2] == "\\":
    if line[0:7]=="#define":

      len_variable = len(storeList[1])
      macro_variable = line[8:8+len_variable]
      remres = line[8+len_variable:].strip("\\\n")
      dict_res[macro_variable].append(remres)
      count+=1
    else:
      remres = line[:-1]
      dict_res[macro_variable].append(remres)
      count+=1
  else:
    if line[0:7]=="#define":
      len_variable = len(storeList[1])
      macro_variable = line[8:8+len_variable]
      remres = line[8+len_variable:]
      dict_res[macro_variable].append(remres)
      count+=1
    else:
      dict_res[macro_variable].append("}")
      count+=1

print(dict_res)
modified_lines = []
modified_file = open("modified_program.txt", "w",encoding='utf-8')
f = open("file3.txt","r",encoding='utf-8')
line=f.readlines()
line1 = line[count:]
#print(line1)
c=0
macro_variable=[]
content_lines=[]
for n,c in dict_res.items():
  macro_variable.append(n)
  content_lines.append(c)

#print("macro.....",macro_variable)
#print("content...",content_lines)
print(line1)
for line in line1:
  flag=0
  for i,n in enumerate(macro_variable):

    if n in line:
      flag=1
      pos=i
      res_index = line.index(n)
      cou=0
      for j in content_lines[pos]:
        if(len(content_lines[pos])==1):
          modified_file.write(line[:res_index]+j+line[res_index+len(j)-2:]+"\n")
        elif(cou==0):
          modified_file.write(line[:res_index]+j+"\n")
        else:
          if j[-1:]=="\\":
            modified_file.write(line[:res_index]+j[:-1]+"\n")
        cou+=1
  if flag==0:
    modified_file.write(line[:])

modified_file.close()
f.close()