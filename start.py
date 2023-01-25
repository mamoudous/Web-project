class Voiture:

    def __int__(self, p_couleur, p_marque):
        self.couleur = p_couleur
        self.marque = p_marque
        self.vitesse = 0

voiture_bleu = Voiture('blue', 'Toyota')
voiture_rouge = Voiture("Rouge", "BMW")

print(voiture_bleu.couleur)
print(voiture_bleu.marque)
print(voiture_rouge.marque)
print(voiture_rouge.couleur)