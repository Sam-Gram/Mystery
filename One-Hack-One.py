def hackOne(a, b):
   parts = []
   for i in range(1, b):
      parts.append(i)
   sum = 0
   for i in parts:
      sum = sum + i
   for i in parts:
      if i == a - sum or a - sum < 1:
         return "Error"
   parts.append(a - sum)
   print(parts)+
