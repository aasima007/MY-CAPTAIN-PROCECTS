most_frequent = "Mississippi"
x={}
for keys in most_frequent:
   x[keys] = x.get(keys,0)+1
   sorted_x_reverse=(sorted(x.items(),reverse=True))
print(sorted_x_reverse)
