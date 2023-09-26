n = 2489
p = [i for i in range (2,n)if all (i%j != 0 for j in range (2,i))]
print(p)




