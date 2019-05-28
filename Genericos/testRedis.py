import redis

r = redis.Redis(host='localhost', port=6379, db=0)

print(r.dbsize())
print(r.get('7184117397522948903'))


'''
Gravando ---> -7644587761339335200 perdida
Gravando ---> 3961670822273285179 jair
Gravando ---> 7184117397522948903 ninguém
Gravando ---> -3417428495642995507 leva
Gravando ---> 5290547034749459385 prêmio
Gravando ---> 3270537663299164062 r
Gravando ---> -6954870016360024157 milhões
Gravando ---> 3168009086822546073 números
Gravando ---> 7342722555472129675 sorteados
'''
