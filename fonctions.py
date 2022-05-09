#ce fichier enregistre les fonctions dont on a besoin
import numpy as np

def readFile(nom_file):
    data=open(nom_file,'r')
    next(data)
    #l = [[float(num) for num in line.split()] for line in data]
    #return np.asarray(l)
    for line in data:
    	print(len(data))
    data.close()