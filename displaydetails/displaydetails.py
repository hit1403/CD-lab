

file = open("filea6.txt","r")
#symbols=[]
variable ={}
function = {}
array = {}
#datatype=[]
bytesalloc ={"int":4 ,"char":1 , "float":4 ,"double":8}
flag=0
for line in file.readlines():
  #print(line)
  if("}" in line[0]):
    flag=0
    continue
  if("int main() {" in line):
    flag=1
    continue
  if flag==1:
    #print(line)
    ll = line.strip().split(" ")
    #print(ll)
    #print("lalalalla:::::  ",ll[0])
    #print("variables: ",ll[1])
    if ll[0]=="int":
      # datatype , bytesalloc , initialvalue
      flagarray=0
      for i in range(len(ll)):
        #print("lllll: ",ll[i])
        if "[" in ll[i]:

          ind = ll[i].index("[")
          #print("ind",ind)
          flagarray = 1
      if flagarray==1:
        if len(ll)>3:
          length = len(ll[3].split(","))
          array[ll[1][:ind]] = ["int",length,ll[3][:-1]]
        else:
          array[ll[1][:ind]] = ["int","NONE","{}"]
        print(array)

      elif flagarray==0:
        if len(ll)>3:
          variable[ll[1]] = ["int",bytesalloc[ll[0]],int(ll[3][:-1])]
        else:
          variable[ll[1]] = ["int",bytesalloc[ll[0]],"NONE"]
    if ll[0]=="char":
      flagarray=0
      for i in range(len(ll)):
        #print("lllll: ",ll[i])
        if "[" in ll[i]:

          ind = ll[i].index("[")
          #print("ind",ind)
          flagarray = 1
      if flagarray==1:
        if len(ll)>3:
          length = len(ll[3].split(","))
          array[ll[1][:ind]] = ["char",length,ll[3][:-1]]
        else:
          array[ll[1][:ind]] = ["char","NONE","{}"]
        print(array)

      elif flagarray==0:
        if len(ll)>3:
          variable[ll[1]] = ["char",bytesalloc[ll[0]],ll[3][:-1]]
        else:
          variable[ll[1]] = ["char",bytesalloc[ll[0]],"NONE"]

    if ll[0]=="float":
      flagarray=0
      for i in range(len(ll)):
        #print("lllll: ",ll[i])
        if "[" in ll[i]:

          ind = ll[i].index("[")
          #print("ind",ind)
          flagarray = 1
      if flagarray==1:
        if len(ll)>3:
          length = len(ll[3].split(","))
          array[ll[1][:ind]] = ["float",length,ll[3][:-1]]
        else:
          array[ll[1][:ind]] = ["float","NONE","{}"]
        print(array)

      elif flagarray==0:
        if len(ll)>3:
          variable[ll[1]] = ["float",bytesalloc[ll[0]],float(ll[3][:-1])]
        else:
          variable[ll[1]] = ["float",bytesalloc[ll[0]],"NONE"]
    if ll[0]=="double":
      flagarray=0
      for i in range(len(ll)):
        #print("lllll: ",ll[i])
        if "[" in ll[i]:

          ind = ll[i].index("[")
          #print("ind",ind)
          flagarray = 1
      if flagarray==1:
        if len(ll)>3:
          length = len(ll[3].split(","))
          array[ll[1][:ind]] = ["double",length,ll[3][:-1]]
        else:
          array[ll[1][:ind]] = ["double","NONE","{}"]
        print(array)

      elif flagarray==0:
        if len(ll)>3:
          variable[ll[1]] = ["double",bytesalloc[ll[0]],float(ll[3][:-1])]
        else:
          variable[ll[1]] = ["double",bytesalloc[ll[0]],"NONE"]

  if flag==0:
    func = line.strip().split(" ")
    if(func[0]=="int"):
      #print(line)
      openInd = line.index("(")
      argline = line[openInd+1:-4]
      #print("argline: ",argline)
      arglist = argline.split(",")
      numarg = len(arglist)
      #print(numarg)
      argDatatype =[]
      argVariable =[]
      for arg in arglist:
        l1 = arg.strip().split(" ")
        argDatatype.append(l1[0])
        argVariable.append(l1[1])
      function[line[4:openInd]] = [numarg , argVariable, argDatatype, func[0]]
    elif(func[0]=="void"):
      #print(line)
      openInd = line.index("(")
      argline = line[openInd+1:-4]
      #print("argline: ",argline)
      arglist = argline.split(",")
      numarg = len(arglist)
      #print(numarg)
      argDatatype =[]
      argVariable =[]
      for arg in arglist:
        l1 = arg.strip().split(" ")
        argDatatype.append(l1[0])
        argVariable.append(l1[1])
      function[line[5:openInd]] = [numarg , argVariable, argDatatype, func[0]]
    elif(func[0]=="float"):
      #print(line)
      openInd = line.index("(")
      argline = line[openInd+1:-4]
      #print("argline: ",argline)
      arglist = argline.split(",")
      numarg = len(arglist)
      #print(numarg)
      argDatatype =[]
      argVariable =[]
      for arg in arglist:
        l1 = arg.strip().split(" ")
        argDatatype.append(l1[0])
        argVariable.append(l1[1])
      function[line[6:openInd]] = [numarg , argVariable, argDatatype, func[0]]
# function name,number of arguments,list of arguments,data type of arguments,return data type.
#print(variable)
#print(function)

print("VARIABLES\n")
print("nameOfVariable\tdatatype\tbytesalloc\tinitialvalue\n")
for k,v in variable.items():
  print(f"{k}\t\t{v[0]}\t\t{v[1]}\t\t{v[2]}")

print("\n\nARRAYS\n")
print("nameOfArray\tdatatype\tsizeOfArray\tinitialvalue\n")
for k,v in array.items():
  print(f"{k}\t\t{v[0]}\t\t{v[1]}\t\t{v[2]}")

print("\n\nFUNCTIONS\n")
print("function name\tnumber of arguments\tlist of arguments\tdata type of arguments\treturn data type\n")
for k,v in function.items():
  print(f"{k}\t\t{v[0]}\t\t\t{v[1]}\t\t{v[2]}\t\t{v[3]}")




