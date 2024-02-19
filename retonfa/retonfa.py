#re = input("Enter regular expression: ")
re = "(a.b)*"
r = {}
obracket = []
cbracket = []
star = []
dot = []
plus = []

symbols = set()
subexplist = []
for ind,i in enumerate(re):
  if i=="(":
    obracket.append(ind)
  elif i==")":
    cbracket.append(ind)
  elif i=="*":
    star.append(ind)
  elif i==".":
    dot.append(ind)
  elif i=="|":
    plus.append(ind)

  #symbols
  elif 97<=ord(i)<=122:
    symbols.add(i)

symbols = sorted(list(set(symbols)))
symDict = {}
c = 1
for ch in symbols:
  symDict["r"+str(c)] = ch
  c+=1
"""
for ind,i in enumerate(cbracket):
  subexplist.append(re[obracket[ind]+1:i])
  if i+1 in star:
    subexplist.append(re[obracket[ind]:i+2])
"""
def indrange(ind2):
  for i1 in range(len(obracket)):
    if obracket[i1]<=ind2<=cbracket[i1]:
      return False
  return True

"""
for ind,i in enumerate(re):
  if i==")":
    ind1 = cbracket.index(ind)
    subexplist.append(re[obracket[ind1]+1:ind])
    if ind+1!=len(re) and ind+1 in star:
        subexplist.append(re[obracket[ind1]:ind+2])
  elif re[ind] in symbols and indrange(ind):
    temp = ind
    st=""
    while(temp!=len(re) and re[temp]!="("):
      st+=re[temp]
      temp+=1
    subexplist.append(st)
"""
ind = 0
while(ind<len(re)):
  i=re[ind]
  if i==")":
    ind1 = cbracket.index(ind)
    subexplist.append(re[obracket[ind1]+1:ind])
    ind+=1
    if ind!=len(re) and ind in star:
        subexplist.append(re[obracket[ind1]:ind+1])
        ind+=1
  elif((i in symbols) and indrange(ind)):
    temp = ind
    st=""
    while(temp!=len(re) and re[temp]!="("):
      st+=re[temp]
      temp+=1
    ind += (temp-ind)
    subexplist.append(st)
  else:
    ind+=1

seDict = {}
for ch in subexplist:
  seDict["r"+str(c)] = ch
  c+=1

print("seDict: ",seDict)
print("symDict: ",symDict)



#########################

symbols.insert(0,"ep")
print("symbols",symbols)
overall = {}
for s,v in symDict.items():
  x=[]
  y=[]
  for i in range(len(symbols)):
    x.append([])
    y.append([])
  overall[s] = {"0-"+s:x,"1-"+s:y}

c = 1


list1 = list(overall)
print(list1)
count = 0
for d1 in overall.values():
  for s,v in d1.items():
    if(s[0]=="0"):

      v[c].append("1-"+s[-2:])

      count+=1
  c+=1
print("overall: ",overall)

def Merge(dict1, dict2):
    return(dict2.update(dict1))

for s,v in seDict.items():
  flag=0
  if(v[-1]!="*"):
    list1.append(s)
    if (v[1]=="|"):
      ind1 = symbols.index(v[0]) -1
      m1 = list1[ind1]
      ind2 = symbols.index(v[2]) - 1
      m2 = list1[ind2]
      flag=1

    elif (v[1]=="."):
      ind1 = symbols.index(v[0]) -1
      m1 = list1[ind1]
      ind2 = symbols.index(v[2]) - 1
      m2 = list1[ind2]
      flag=2
    #print("m1 : ",m1,"m2 : ",m2)
    if flag==2:
      overall[s] = {}
      Merge(overall[m1],overall[s])
      Merge(overall[m2],overall[s])
      overall[s]["0-"+m1][1]=["0-"+m2]
      print(f"overall[{s}]",overall[s])
    if flag==1:
      overall[s] = {}
      x=[]
      y=[]
      for i in range(len(symbols)):
        x.append([])
        y.append([])
      overall[s] = {"0-"+s:x}

      Merge(overall[m1],overall[s])
      Merge(overall[m2],overall[s])
      #print(f"overall[{s}]",overall[s])

      x = []
      y = []
      for i in range(len(symbols)):
        x.append([])
        y.append([])
      overall[s]["1-"+s]=y
      #print(f"overall[{s}]",overall[s])

      
      overall[s]["0-"+s][0].extend(["0-"+m1,"0-"+m2])
    #print(f"overall[{s}]",overall[s])
      overall[s]["1-"+m1][0].extend(["1-"+s])
      overall[s]["1-"+m2][0].extend(["1-"+s])
      print(f"overall[{s}]",overall[s])

"""
  else:
    overall[s]={}
    x=[]
    y=[]
    for i in range(len(symbols)):
      x.append([])
      y.append([])
    overall[s] = {"0-"+s:x}
    
    Merge(overall[list1[-1]],overall[s]) 

    x = []
    y = []
    for i in range(len(symbols)):
      x.append([])
      y.append([])
    overall[s]["1-"+s]=y
    #print(f"overall[{s}]: ",overall[s])
    overall[s]["0-"+s][0].extend(["0-"+list1[-1],"1-"+s])
    overall[s]["1-"+list1[-1]][0].extend(["0-"+list1[-1],"1-"+s])
    print(f"overall[{s}]: ",overall[s])





"""






######################


from prettytable import PrettyTable
mytab = PrettyTable()
mytab.field_names = ["","ep","a","b"]
for k,v in overall.items():
  mytab = PrettyTable()
  for k1,v1 in v.items():
    temp = []
    temp.extend([k1])
    for i in range(len(symbols)):
      temp.append(v1[i])
    mytab.add_row(temp)
  print(mytab)