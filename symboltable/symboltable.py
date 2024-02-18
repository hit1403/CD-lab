import random
file = open("file5.txt","r")


GstartAdr = [[]]
Gdefinition = {}
Grefered = [[]]
p=0
linec=0
hex_diff = lambda x,y : hex(int(x,16) - int(y,16))
hex_sum = lambda x,y : hex(int(x,16) + int(y,16))
for line in file.readlines():
  print(line[0])
  linec+=1
  if(line=='\n'):
    GstartAdr.append([])
    Grefered.append([])
    p+=1
    continue
  ll = line.split("_")
  if(ll[0]=='H'):
    GstartAdr[p].append(ll[2][2:])
  elif(ll[0]=='D'):
    c=1
    if p not in Gdefinition:
      Gdefinition[p]={}
    while(c<len(ll)):
      if(ll[c+1][-1]=="\n"):
        ll[c+1]=ll[c+1][:-1]
      Gdefinition[p][ll[c]] = hex_diff(ll[c+1],GstartAdr[p][0])
      c+=2
  elif(ll[0]=='R'):
    c=1
    while(c<len(ll)):
      if(ll[c][-1] == "\n"):
        ll[c]=ll[c][:-1]
      Grefered[p].append(ll[c])
      c+=1

Grefered.pop(-1)
GstartAdr.pop(-1)
print(GstartAdr)
print(Gdefinition)
print(Grefered)


for i,j in Gdefinition.items():
  rno = random.randrange(0,65535)

  for k,l in j.items():
    listref=[]
    print("\n",k,"\t\t","program",i,"\t",GstartAdr[i][0],"\t",hex_sum(GstartAdr[i][0],l)[2:],"\t",hex(rno)[2:],"\t",hex_sum(hex(rno),l)[2:],"\t",end="\t")
    for ind,al in enumerate(Grefered):
      if k in al:
        listref.append(ind)
    for z in listref:
      print("program ",z,end=" ")