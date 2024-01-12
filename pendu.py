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

    def lettre_existe(self, lettre, mot_secret):
        if lettre in mot_secret:
            return True
        else:
            return False

    def afficher_mot_masque(self,mot_secret, lettres_trouvees):
        mot_masque = ""
        for lettre in mot_secret:
            if lettre in lettres_trouvees:
                mot_masque += lettre
            else:
                mot_masque += "_"
        return mot_masque

    def enlever_tentative_si_faux(self, lettre, mot_secret,tentatives_restantes):
        mot_list = list(mot_secret)
        if lettre not in mot_list:
            tentatives_restantes -= 1
        return tentatives_restantes

    def verifier_si_mot_decouvert(self,mot_secret,lettres_trouvees):
        if "_" in self.afficher_mot_masque(mot_secret,lettres_trouvees):
            return False
        else:
            return True

    def verifier_si_lettre_deja_devine(self,lettre,lettres_trouvees):
        if lettre in lettres_trouvees:
            return True
        else:
            return False

    def pendu(self):
        mot_secret = self.choisir_mot()
        lettres_trouvees = []
        tentatives_restantes = 10

        print("Bienvenue au jeu du pendu!")
        print("Mot actuel :", self.afficher_mot_masque(mot_secret, lettres_trouvees))

        while tentatives_restantes > 0 and "_" in self.afficher_mot_masque(mot_secret, lettres_trouvees):
            lettre = input("Devinez une lettre : ").lower()

            if self.verifier_si_lettre_deja_devine(lettre,lettres_trouvees):
                print("Vous avez déjà deviné cette lettre. Essayez une autre.")
                continue

            lettres_trouvees.append(lettre)

            if self.lettre_existe(lettre,mot_secret):
                print("Bonne devinette !")
            else:
                print("Mauvaise devinette.")
                tentatives_restantes = self.enlever_tentative_si_faux(lettre, mot_secret, tentatives_restantes)

            print("Mot actuel :", self.afficher_mot_masque(mot_secret, lettres_trouvees))
            print("Lettres déjà devinées :", ", ".join(lettres_trouvees))
            print("Tentatives restantes :", tentatives_restantes)

        if self.verifier_si_mot_decouvert(mot_secret,lettres_trouvees):
            print("Félicitations ! Vous avez deviné le mot :", mot_secret)
        elif not self.verifier_si_mot_decouvert(mot_secret,lettres_trouvees) and tentatives_restantes == 0 :
            print("Désolé, vous avez épuisé toutes vos tentatives. Le mot était :", mot_secret)


if __name__ == '__main__':
    jeu_pendu = Pendu()
    jeu_pendu.pendu()
