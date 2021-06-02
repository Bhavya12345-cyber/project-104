import csv 

with open('height.csv', newline = '') as f:
    fileReader = csv.reader(f)
    file_data = list(fileReader)

file_data.pop(0)
new_data = []

for i in range(len(file_data)):
    num = file_data[i][2]
    new_data.append(float(num))

total = 0
for x in new_data:
    total = total+x

mean = total/len(new_data)
print("mean(Average)="  +  str(mean))



with open('data1.csv', newline = '') as f:
    fileReader = csv.reader(f)
    file_data = list(fileReader)

file_data.pop(0)
new_data = []

for i in range(len(file_data)):
 num = file_data[i][2]
new_data.append(float(num))

n = len(new_data)
new_data.sort()

#for even obs.
if n%2 == 0:
    firstmedian = float(new_data[n//2])
    secondmedian = float(new_data[n//2-1])

    finalmedian =  (firstmedian + secondmedian)//2

else:
    finalmedian = new_data[n//2]

print("median = " + str(finalmedian))
