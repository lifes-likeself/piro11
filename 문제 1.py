a = input()
a = a.strip("'][").split("', '")
for i in range(len(a[0])):
  amount = 0
  front = a[0][0:len(a[0]) - i - 1]
  for j in a:
    if front == j[0:len(a[0]) - i - 1]:
      amount += 1

    if amount == len(a[0]):
      result = front
      break

print(result)
