from better_profanity import profanity

def censurer_texte(texte):
    censure = profanity.censor(texte)
    return censure

# Exemple 1
texte1 = "Ce type est vraiment un imbécile, je ne peux pas le supporter !"
resultat1 = censurer_texte(texte1)
print("Exemple 1:")
print("Texte original:", texte1)
print("Texte censuré:", resultat1)
print()

# Exemple 2
texte2 = "Je n'aime pas quand les choses ne fonctionnent pas correctement, c'est vraiment frustrant."
resultat2 = censurer_texte(texte2)
print("Exemple 2:")
print("Texte original:", texte2)
print("Texte censuré:", resultat2)
