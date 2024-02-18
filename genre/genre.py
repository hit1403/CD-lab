import random
import collections
symbols = ['a','b']
reg = "(a|b)*.(a.b)"
tot_exp = []
starind = []
dotind = []
pipeind = []
exp = []
star_exp_ind = []
cl = []
op = []
pipe_exp = {}
reg = reg.replace(".","")
for i,r in enumerate(reg):
  if r=="(":
    op.append(i)
  elif r==")":
    cl.append(i)
  elif r=="*":
    starind.append(i)
for i,r in enumerate(op):
  exp.append(reg[r+1:cl[i]])

print(exp)

for i,v in enumerate(starind):
  if v-1 in cl:
    star_exp_ind.append(cl.index(v-1))
print(star_exp_ind)


for i0,e in enumerate(exp):
  temp = [0]
  for i,v in enumerate(e):
    if v=="|":
      temp.append(i)
  temp.append(i+1)
  pipeind.append(temp)
print(pipeind)

for i,v in enumerate(pipeind):
  if len(v)==2:
    continue
  else:
    tempe = exp[i]
    pipetemp = []
    for inn,indi in enumerate(v):
      if indi==0:
        continue
      else:
        if inn==1:
          pipetemp.append(tempe[v[inn-1]:indi])
        else:
          pipetemp.append(tempe[v[inn-1]+1:indi])
    pipe_exp[i] = pipetemp
print(pipe_exp)

for i,v in enumerate(exp):
  if i in star_exp_ind:
    if "|" in v:
      temp = pipe_exp[i]
      texp = []
      for j in range(10):
        tempstr = ""
        times = random.randrange(1,6)
        #charac = random.randrange(0,len(temp)-1)
        for j1 in range(times):
          charac_ind = random.randrange(0,len(temp))
          tempstr+=temp[charac_ind]
        texp.append(tempstr)
      tot_exp.append(texp)

    else:
      texp1 =[]
      for j in range(10):
        tempstr1 = ""
        times = random.randrange(0,6)
        tempstr1 += times*v
        texp1.append(tempstr1)
      tot_exp.append(texp1)
  else:
    if "|" in v:
      temp = pipe_exp[i]
      texp2 = []
      for j in range(10):
        tempstr = ""
        charac_ind = random.randrange(0,len(temp))
        tempstr = temp[charac_ind]
        texp2.append(tempstr)
      tot_exp.append(texp2)

    else:
      texp3= []
      for j in range(10):
        texp3.append(v)
      tot_exp.append(texp3)


print(tot_exp)

fstring = []
for i in range(10):
  strt=""
  for j in range(len(tot_exp)):
    strt+=(tot_exp[j][i])
  fstring.append(strt)
print(fstring)




















