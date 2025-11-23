final = 343 
maxStart = 0 

for k in range(1001):  
    startZeros = final + k - 1  
    if startZeros <= 999: 
        maxStart = max(maxStart, startZeros) 

print(maxStart) 

