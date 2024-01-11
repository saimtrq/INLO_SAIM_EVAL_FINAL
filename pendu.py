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

    def lettre_existe(self,lettre_trouvee,mot_secret):
        liste_mot_secret = list(mot_secret)
        pos = np.where(np.array(liste_mot_secret) == np.array(list(lettre_trouvee)))[0]
        return pos

    def demasque_mot(self, lettre_trouvee, mot_secret, mot_masque):
        indice_lettre_trouvee = self.lettre_existe(lettre_trouvee, mot_secret)
        for i in range(len(indice_lettre_trouvee)):
                mot_masque[indice_lettre_trouvee[i]] = lettre_trouvee

        return mot_masque

    def enlever_tentative_si_faux(self, lettre_trouvee, mot_secret, mot_masque,nombre_tentative):
        indice_lettre_trouvee = self.lettre_existe(lettre_trouvee, mot_secret)
        if len(indice_lettre_trouvee) == 0:
            nombre_tentative -= 1
        return nombre_tentative

    def verifier_si_mot_decouvert(self,mot_masque,mot_secret):
        if mot_secret in mot_masque:
            return True
        else:
            return False

    def verifier_si_lettre_deja_devine(self,lettre_trouvee,toutes_lettres_devinee):
        if lettre_trouvee in toutes_lettres_devinee:
            return True
        else:
            return False

    def pendu(self):
        mot_secret = "jouet"
        mot_masque = ["_"]*len(mot_secret)
        nombre_tentative = 10
        lettre_trouvee = []
        toutes_lettres_devinee = []
        print("Bienvenue au jeu du pendu!")
        print("Mot actuel :", "_"*len(mot_secret))

        while nombre_tentative > 0 and "_" in mot_masque:
            lettre = input("Devinez une lettre : ").lower()

            if self.verifier_si_lettre_deja_devine(lettre_trouvee,toutes_lettres_devinee):
                print("Vous avez déjà deviné cette lettre. Essayez une autre.")
                continue

            toutes_lettres_devinee.append(lettre)

            if self.lettre_existe(lettre_trouvee,mot_secret):
                print("Bonne devinette !")
            else:
                print("Mauvaise devinette.")
                self.enlever_tentative_si_faux(lettre_trouvee, mot_secret, mot_masque,nombre_tentative)


if __name__ == '__main__':
    jeu_pendu = Pendu()
    jeu_pendu.pendu()
