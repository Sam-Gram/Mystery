checkedSolutions = list()

def isSolutionUsed(solution, usedSolutions):
    index = 0
    numSame = 0
    for i in checkedSolutions:
        for j in i:
            if(solution[index] == j)
               numSame = numSame + 1
    if(numSame == solution.size()):
      return true
    return false

def generateSolution(list, usedSolutions):
   solutionUsed = true
   while(solutionUsed):
        index = 0
        for i in range(0, 26):
            list[i] = random(1, size + 1)
        if(!isSolutionUsed(list, usedSolutions)):
            solutionUsed = false
   return solutionUsed

def findAnswer(words, word):
   usedSolutions = list()
   isValid = false
   while(isValid == false):                 
      solution = generateSolution(list, usedSolutions)
      usedSolutions.appendSolution()
      isValid = isValidSolution(solution, words)
   sum = 0
   for let in word:
       sum += solution[ord[let] - 97]
   return sum

def isValidSolution(solution, words)
{
   for key, word in words:
       sum = 0
       for let in key:
           sum += solution[ord[let] - 97]
       if(sum != words[key]):
              return false
   return true 
}
   
