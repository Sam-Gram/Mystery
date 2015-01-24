def breakdownHack(A, B):
  var1 = math.floor(A/B)
  var2 = math.floor(B/2)
  pieces = list(); 
  total = 0
  var3 = var1 - var2
  if(var3 <= 0):
  	print “Does not work”
  else:
    for i in range(0, B):
    		pieces.append(var3)
    		total = total + var3
    		var3 = var3 + 1
    		if(total < A):
    		  pieces[B - 1] = pieces[B-1] + (A - total)
    print(pieces)

def randomBreakDown(A, B):
	largestNum = A - ((B - 1) * B)) / 2
	sum = 0
	if(math.floor(A/B) - math.floor(B/2) <= 0):
		print “Does not work”
	else:
  	while(sum != A):
  		nums = list()
  		sum = 0
      for i in range(1, B):
    	  valid = false
        while(valid == false):
          val = random.randrange(1, largestNum + 1)
          if val not in nums:
            valid = true
          	sum += val
          	nums.append(val)
    print(nums)





	

			
			
		
			

