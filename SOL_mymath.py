def add(x,y):
    """Fonction d'addition, permet d'ajouter 2 valeurs.

    :param x: première valeur
    :param y: deuxième valeur
    :type x: int, float
    :type y: int, float
    :returns: x+y
    :rtype: int, float

    .. warning:: les entrées doivent être numériques uniquement
    """
    if not isinstance(x, (int, float)) and not isinstance(y, (int, float)):
        raise TypeError('un des paramètres n\'est pas un nombre')

    return x+y

def substract(x,y):
    """Fonction de soustraction, permet de soustraire 2 valeurs.

    :param x: première valeur
    :param y: deuxième valeur
    :type x: int or float
    :type y: int or float
    :returns: x-y
    :rtype: int or float

    .. warning:: les entrées doivent être numériques uniquement
    """
    if not isinstance(x, (int, float)) and not isinstance(y, (int, float)):
        raise TypeError('un des paramètres n\'est pas un nombre')

    return x-y

def multiply(x,y):
    """Fonction de multiplitcation, permet de multiplier 2 valeurs.

    :param x: première valeur
    :param y: deuxième valeur
    :type x: int, float
    :type y: int, float
    :returns: x*y
    :rtype: int, float

    .. warning:: les entrées doivent être numériques uniquement
    """
    if not isinstance(x, (int, float)) and not isinstance(y, (int, float)):
        raise TypeError('un des paramètres n\'est pas un nombre')

    return x*y

def divide(x,y):
    """Fonction de division, permet de diviser 2 valeurs.

    :param x: première valeur
    :param y: deuxième valeur
    :type x: int, float
    :type y: int, float
    :returns: x/y
    :rtype: int, float

    .. warning:: les entrées doivent être numériques uniquement.
    .. warning:: y doit être différent de zéro.
    """
    if not isinstance(x, (int, float)) and not isinstance(y, (int, float)):
        raise TypeError('un des paramètres n\'est pas un nombre')
    else:
        if y == 0:
            raise ValueError('division par O impossible')
        else:
            return x/y
