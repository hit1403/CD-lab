file = open("file4.txt","r")
dictop = {'LDA':'00','STA':'0C','LDCH':'50','STCH':'54'}
FINL=[]
nmeonic =[]
address = ['ABCD']
hexadecimal_sum = lambda a,b : hex(int(a, 16) + int(b, 16))
for line in file.readlines():
  listSIC = line.strip().split(" ")
  FINL.append(listSIC)
print(FINL)
for i in FINL:
  if(len(i)==2):
    nmeonic.append(i[0])
    if i[0]=='BYTE' or i[0]=='RESB':
      addr = hexadecimal_sum(str(address[-1]),"1")
      address.append(addr.upper()[2:])
    else:
      addr = hexadecimal_sum(str(address[-1]),"3")
      address.append(addr.upper()[2:])
  if(len(i)==3):
    nmeonic.append(i[1])
    if i[1]=='BYTE' or i[1]=='RESB':
      addr = hexadecimal_sum(str(address[-1]),str(len(i[2])))
      address.append(addr.upper()[2:])
    else:
      addr = hexadecimal_sum(str(address[-1]),"3")
      address.append(addr.upper()[2:])

address.pop(-1)

#print(nmeonic)
#print(address)
MachineCode = []
for i in FINL:
  if len(i)==2:
    find = i[1]
    for ind,j in enumerate(FINL):
      if(j[0]==find):
        MachineCode.append(dictop[i[0]]+address[ind])
  if len(i)==3:
    if i[1]!='RESW' and i[1]!='RESB':
      var = i[2]
      if var=='Z':
        MachineCode.append((6-len(var))*"0" + var)
      else:
        hvar = hex(int(var,16))
        lvar = len(str(hvar)[:-2])
        MachineCode.append((6-lvar)*"0" + hvar[2:])
    else:
      MachineCode.append(" ")

for i in range(len(FINL)):
  if(len(FINL[i])==2):
    #output_file.write(str(address[i])+"\t"+"\t"+"\t"+"\t"+FINL[i][0]+"\t"+FINL[i][1]+"\t"+MachineCode[i]+"\n")
    print(address[i],"\t","\t",FINL[i][0],"\t",FINL[i][1],"\t",MachineCode[i])
  else:
    #output_file.write(str(address[i])+"\t"+FINL[i][0]+"\t"+FINL[i][1]+"\t"+FINL[i][2]+"\t"+MachineCode[i]+"\n")
    print(address[i],"\t",FINL[i][0],"\t",FINL[i][1],"\t",FINL[i][2],"\t",MachineCode[i])