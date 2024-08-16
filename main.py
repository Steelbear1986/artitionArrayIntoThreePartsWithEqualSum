s=sum(arr)//3
        for i in range(1,len(arr)):
              if sum(arr[:i])==s:
                    for j in range(1,len(arr[i:])):
                        if sum((arr[i:])[:j])==s:
                                     return sum((arr[i:])[j:])==s
        return False



2
n = len(arr)
total_sum = sum(arr)
s = sum(arr) // 3

if total_sum != 3 * s:
    return False
first_sum = 0
count = 0
for i in range(n - 1):
    first_sum += arr[i]
    if first_sum == s:
        count += 1
        first_sum = 0

    if count == 2:
        return True
return False