# -*- coding: utf-8 -*-

"""PageDraw Simple Storage helper functions.

Author:
    Rodrigo Leme de Mello
    lemerodrigo@gmail.com

Version:
    1.0

Last revision:
    Sunday, April 23rd, 2017

"""

def is_number(arg):
    """Checks if the passed argument is a number or not

    Return:
        True|False    
    """
    try:
        float(arg)
        return True
    except ValueError:
        return False