mark=40

if 100 <= mark <=101:
 print("error")
if 75 <=mark <=100:
 print("Distinction")
elif 60 <= mark <75:
  print("pass")
elif 50 <= mark <69:
  print("credit")
elif 35 <= mark <49:
  print("almost")
elif 20 <= mark<35:
  print("fail")
elif 0 <= mark <20:
  print("ungraded")
else:
  print("error")