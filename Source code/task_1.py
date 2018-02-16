print('UMKC Library and Book shop\n')
Dictionary = {'python':50,'web':30,'c':20,'java':40}
list_A = list(Dictionary.values())
list_B = []
list_C = []
print('Please provide your range:')
Low = int(input('Low price :'))
High = int(input('High price:'))
for i in range(Low,High+1):
 list_B.append(i)
for name, item in Dictionary.items():
 if item in list_B:
     list_C.append(name)
print('the books comes in your range are :',list_C)