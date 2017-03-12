#!/usr/bin/env python3.3 -m doctest -v

def sqrt(a):
    '''
        Calcul la racine carré d'un nombre
        
        Calcul la racine carré d'un nombre en utilisant la méthode de Héron aussi appelé méthode babylonienne.
        Cette méthode n'hésite plusieur itération (10 dans notre cas) et converge en un temps quadratique.
    
        :param a: Valeur dont on veut la racine
        :type a: float
        :return: la racine de a
        :rtype: float
        
        >>> sqrt(1)
        1.0
        >>> sqrt(2)
        1.414213562373095
        
        .. note:: Cette fonction est dépréciée. Utilisez plutôt sqrt de la librairie math.
        .. todo:: Ajouter un paramètre pour changer le nombre d'itération de la méthode.
    '''
    res=1
    for i in range(10):
        res=(res+a/res)/2
    return res

def det(a,b,c):
    '''
        Renvoit le determinant du polynome de degre 2 ax^2+bx+c
    
        :param a: coefficient de degre 2
        :type a: float
        :param b: coefficient de degre 1
        :type b: float
        :param c: coefficient de degre 0
        :type c: float
        :return: la valeur b^2-4ac
        :rtype: float
        
        >>> x=1
        >>> y=1
        >>> z=1
        >>> racPoly2(x,y,z)
        ()
        
        .. seealso:: racPoly2(a,b,c)
    '''
    return b**2-4*a*c


def racPoly2(a,b,c):
    '''Calcul la racine d'un polynome et renvoit le résultat dans un tuple'''
    d=det(a,b,c)
    if d<0:
        return ()
    elif d==0:
        return (-b/2*a,)#ne pas oublier la virgule sinon ce n'est pas un tuple
    else:
        x1=(-b-sqrt(d))/2*a
        x2=(-b+sqrt(d))/2*a
        return (x1,x2)

#print(racPoly2(1,0,1))
#print(racPoly2(1,2,1))
#print(racPoly2(1,0,-1))

#help(sqrt)
#print(sqrt.__doc__)
