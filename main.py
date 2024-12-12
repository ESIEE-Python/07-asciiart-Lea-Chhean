#### Imports et définition des variables globales
"""permet de limiter le nombre de récursions"""
import sys
sys.setrecursionlimit(10000)

#### Fonctions secondaires
def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères
     passée en argument selon un algorithme itératif
    Args:
        s (str): la chaîne de caractères à encoder
    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    chaine = []
    compteur = 1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            compteur+= 1
        else:
            chaine.append((s[i-1],compteur))
            compteur = 1
    chaine.append((s[-1],compteur))
    return chaine

def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères
        passé en argument selon un algorithme récursif
    Args:
        s (str): la chaîne de caractères à encoder
    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    # cas de base
    if not s:
        return []
    # recherche nombre de caractères identiques au premier
    compteur = 1
    while compteur<len(s) and s[0]==s[compteur]:
        compteur+=1
    return [(s[0],compteur)] + (artcode_r(s[compteur:]))
    # appel récursif

#### Fonction principale
def main():
    """Fonction qui permet d'encoder une chaîne de caractères
    en liste de tuples
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
