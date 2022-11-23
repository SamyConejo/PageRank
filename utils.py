
def vector_format(vector):
    temp_vector = vector
    vector = list(vector)
    vector.sort()
    nodo = 0
    for x in temp_vector:
        print('N-'+str(nodo),' ',round(x,4),'\t\t\t',vector.index(x))
        nodo +=1
    print('----------------')

