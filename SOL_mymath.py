def add(x,y):
    """Fonction d'addition, permet d'ajouter 2 valeurs.

    :param x: premiere valeur
    :param y: deuxieme valeur
    :type x: int, float
    :type y: int, float
    :returns: x+y
    :rtype: int, float

    .. warning:: les entrees doivent etre numeriques uniquement
    """
    if not isinstance(x, (int, float)) and not isinstance(y, (int, float)):
        raise TypeError('un des parametres n\'est pas un nombre')

    return x+y

def substract(x,y):
    """Fonction de soustraction, permet de soustraire 2 valeurs.

    :param x: premiere valeur
    :param y: deuxieme valeur
    :type x: int or float
    :type y: int or float
    :returns: x-y
    :rtype: int or float

    .. warning:: les entrees doivent etre numeriques uniquement
    """
    if not isinstance(x, (int, float)) and not isinstance(y, (int, float)):
        raise TypeError('un des parametres n\'est pas un nombre')

    return x-y

def multiply(x,y):
    """Fonction de multiplication, permet de multiplier 2 valeurs.

    :param x: premiere valeur
    :param y: deuxieme valeur
    :type x: int, float
    :type y: int, float
    :returns: x*y
    :rtype: int, float

    .. warning:: les entrees doivent etre numeriques uniquement
    """
    if not isinstance(x, (int, float)) and not isinstance(y, (int, float)):
        raise TypeError('un des parametres n\'est pas un nombre')

    return x*y

def divide(x,y):
    """Fonction de division, permet de diviser 2 valeurs.

    :param x: premiere valeur
    :param y: deuxieme valeur
    :type x: int, float
    :type y: int, float
    :returns: x/y
    :rtype: int, float

    .. warning:: les entrees doivent etre numeriques uniquement.
    .. warning:: y doit etre different de zero.
    """
    if not isinstance(x, (int, float)) and not isinstance(y, (int, float)):
        raise TypeError('un des parametres n\'est pas un nombre')
    else:
        if y == 0:
            raise ValueError('division par O impossible')
        else:
            return x//y
