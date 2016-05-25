##################################################
## adamPluth					##
## apluth@crimson.ua.edu			##
## project2					##
## data orginization				##
## 2/2/15					##
##################################################
import sys
import operator

def main(args):
  
  rows=[]
  sortKeys=[None]*3
  with open(args[1],'r') as f:
    stuff=(f.readline().split(','))
    stuff[-1]=stuff[-1][:-1]
    for line in f:
      l=line.split(',')
      l[-1]=l[-1][:-1]
      data={s:l[stuff.index(s)] for s in stuff}
      rows.append(data)

  with open(args[2],'r')as f:
    sortKeys[0]=f.readline().split(',',)
    sortKeys[0][-1]=sortKeys[0][-1][:-1]
    sortKeys[1]=f.readline().split(',')
    sortKeys[1][-1]=sortKeys[1][-1][:-1]
    sortKeys[2]=f.readline().split(',')
    sortKeys[2][-1]=sortKeys[2][-1][:-1]
  if len(sortKeys[-1])==3:
    a,b,c=sortKeys[0][0],sortKeys[1][0],sortKeys[2][0]#catagory
    x,y,z='descend' in sortKeys[0],'descend' in sortKeys[1],'descend' in sortKeys[2]
    h,k,j=sortKeys[0][2],sortKeys[1][2],sortKeys[2][2]
  elif len(sortKeys[-1])==2:
    a,b,c=sortKeys[0][0],sortKeys[1][0],sortKeys[1][0]#catagory
    x,y,z=sortKeys[0][1]=='descend',sortKeys[1][1]=='descend',sortKeys[1][1]=='descend'
    h,k,j=sortKeys[0][2],sortKeys[1][2],sortKeys[1][2]
  else:
    a,b,c=sortKeys[0][0],sortKeys[0][0],sortKeys[0][0]#catagory
    x,y,z=sortKeys[0][1]=='descend',sortKeys[0][1]=='descend',sortKeys[0][1]=='descend'
    h,k,j=sortKeys[0][2],sortKeys[0][2],sortKeys[0][2]
  for item in rows:
    for key, value in item.items():
      if item[key][0].isupper() or item[key][0].islower():
        continue
#      elif '000000'or'111111'or'22222'or'33333'or'4444444'or'555555'or'666666'or'77777'or'88888'or'99999' in value:
      elif key =='cwid':
        continue
      try:  
        item[key]=int(value)
      except ValueError:
        item[key]=float(value)
  if x:
    newRows=sorted(rows,key=lambda k: (k[c]),reverse=True)
  else:
    newRows=sorted(rows,key=lambda k: (k[c]))#,reverse=True)
  if y:
    newRows=sorted(newRows,key=lambda k: (k[b]),reverse=True)
  else:
    newRows=sorted(newRows,key=lambda k: (k[b]))#,reverse=True)
  if z:  
    newRows=sorted(newRows,key=lambda k: (k[a]),reverse=True)
  else:
    newRows=sorted(newRows,key=lambda k: (k[a]))#,reverse=True)
  printout(newRows,stuff,args)

def printout(rows,stuff,args):
 with open(args[3],'w')as f:
    c=''
    for s in range(len(stuff)):
      c+=stuff[s]+','
    f.write(c[:-1]+'\n')
    for l in rows:
      for li in range(len(l)):
        temp=str(l[stuff[li]])
        f.write(temp)
        if li !=len(l)-1:
          f.write(',')
      f.write('\n')

if __name__=='__main__':
  sys.exit(main(sys.argv))
