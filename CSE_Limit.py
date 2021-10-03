import csv
#dictionary to store all limit
dailyLimit = {}

with open('CSE_Limit_Data/cse_daily_limit.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        dailyLimit[row[0]] = row[1]


for code in dailyLimit:
    print(dailyLimit[code])


cash = {}

rbsCash = []
with open('CSE_Limit_Data/RBSL#cash.txt') as f:
    rbsCash = f.readlines()

for line in rbsCash:
    splitedLine = line.split("|")
    # if splitedLine[0] != "DL1":
    #     cash[splitedLine[0]] = float(splitedLine[1])
    cash[splitedLine[0]] = float(splitedLine[1])

    print("Code "+ splitedLine[0]+" has "+ "{:.2f}".format(float(splitedLine[1])))

del cash['DL1']
   

print(cash)

# rbsStock = []
# with open('the-zen-of-python.txt') as f:
#     rbsStock = f.readlines()



# fsCash = []
# with open('the-zen-of-python.txt') as f:
#     fsCash = f.readlines()


# fsStock = []
# with open('the-zen-of-python.txt') as f:
#     fsStock = f.readlines()


# jbCash = []
# with open('the-zen-of-python.txt') as f:
#     jbCash = f.readlines()


# jbStock = []
# with open('the-zen-of-python.txt') as f:
#     jbStock = f.readlines()