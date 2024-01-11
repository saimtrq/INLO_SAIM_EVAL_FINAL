import random
import numpy as np


class Pendu:
    def choisir_mot(self):
        mots = [
            "chat", "soleil", "arbre", "maison", "fleur",
            "plage", "oiseau", "lune", "étoile", "route",
            "fraise", "montagne", "rivière", "pont", "pomme",
            "voiture", "école", "ballon", "livre", "nuage",
            "jardin", "arc-en-ciel", "café", "cœur", "chocolat",
            "cerise", "papillon", "nuage", "fenêtre", "porte",
            "poisson", "ciel", "chapeau", "chien", "chaton",
            "piano", "danse", "oiseau", "ballon", "forêt",
            "gâteau", "rue", "église", "vélo", "train",
            "avion", "bateau", "poème", "histoire", "musique",
            "amour", "bonheur", "rêve", "sourire", "rire",
            "pluie", "neige", "étoile filante", "hiver", "printemps",
            "été", "automne", "famille", "ami", "voyage",
            "sable", "pieds", "fenêtre", "porte", "ordinateur",
            "internet", "écran", "clavier", "souris", "table",
            "chaise", "lampe", "coussin", "couverture", "tapis",
            "cadeau", "carte", "lettre", "merci", "santé",
            "bonjour", "au revoir", "silence", "couleur", "joie",
            "tristesse", "douceur", "câlin", "bisou", "nuit",
            "jour", "moment", "instant", "tranquillité", "tendresse",
            "jouet", "musée", "photo", "parc", "rue",
            "manger", "boire", "dormir", "lire", "écrire",
            "dessiner", "jouer", "courir", "marcher", "écouter",
            "regarder", "sentir", "goûter", "aimer", "partager",
            "rêver", "penser", "espérer", "vivre", "grandir"
        ]
        return random.choice(mots)

    def lettre_existe(self,lettre_trouve,mot_secret):
        liste_mot_secret = list(mot_secret)
        pos = np.where(np.array(liste_mot_secret) == lettre_trouve)[0]

        return pos

    def demasque_mot(self, lettre_trouve, mot_secret, mot_masque):
        indice_lettre_trouver = self.lettre_existe(lettre_trouve, mot_secret)
        for i in range(len(indice_lettre_trouver)):
                mot_masque[indice_lettre_trouver[i]] = lettre_trouve[i]

        return mot_masque



if __name__ == '__main__':
    jeu_pendu = Pendu()
    lettre_trouver = "o"
    lettre_trouver = lettre_trouver.lower()
    mot_secret = "soleil"
    mot_masque = ["_"]*len(mot_secret)
    print(jeu_pendu.demasque_mot(lettre_trouver,mot_secret,mot_masque))