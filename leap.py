
leap1=[]
leap2=[]
for year in range(1800,2400):


  if (year % 4) == 0:  
    if (year % 100) == 0:  
      if (year % 400) == 0:  
        print(f"{year} is a leap year")
        leap1.append(year)
      else:  
        print(f"{year} is not a leap year")  
    else:  
      print(f"{year} is a leap year")
      leap2.append(year)
  else:  
    print(f"{year} is not a leap year")

total=leap2+leap1
print(len(total))  