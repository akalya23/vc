s1=input()
count=0
for i in s1:
  if (i.isnumeric()!=True and i.isalpha()!=True):
    count=count+1
print(count)
