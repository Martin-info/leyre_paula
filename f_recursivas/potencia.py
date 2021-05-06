from timeit import default_timer as timer

start = timer()




B=987654321 # base
E=100000 # exponente
p=1 # potencia


for i in range(E):
	p*=B   # multiplico E la Base

op=timer()-start
print(p)

end = timer()

print()
print("prog= ",end - start," seconds")
print("op= ",op," seconds")