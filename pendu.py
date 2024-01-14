import random


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

    def lettre_existe(self,lettre,mot_secret):
        return lettre in mot_secret

    def afficher_mot_masque(self,mot_secret,lettre_trouvees):
        mot_masque = "".join(lettre if lettre in lettre_trouvees else '_' for lettre in mot_secret)
        return mot_masque

    def enlever_tentative_si_faux(self,lettre,mot_secret,tentative_restantes):
        return tentative_restantes - (lettre not in mot_secret)

    def verifier_si_mot_decouvert(self,mot_secret,lettre_trouvees):
        return "_" not in self.afficher_mot_masque(mot_secret,lettre_trouvees)

    def verifier_si_lettre_devinee(self,lettre,lettre_trouvees):
        if lettre in lettre_trouvees:
            return True
        else:
            return False

    def pendu(self):
        mot_secret = self.choisir_mot()
        lettre_trouvees = []
        tentative_restantes = 10

        print("Bienvenue au jeu du pendu!")
        print("Mot actuel :", self.afficher_mot_masque(mot_secret,lettre_trouvees))

        while tentative_restantes > 0 and not self.verifier_si_mot_decouvert(mot_secret,lettre_trouvees):
            lettre = input("Devinez une lettre : ".lower())

            if self.verifier_si_lettre_devinee(lettre,lettre_trouvees):
                print("Vous avez déjà deviné cette lettre. Essayez en une autre.")
                continue

            lettre_trouvees.append(lettre)

            if self.lettre_existe(lettre,mot_secret):
                print("Bonne devinette !")
            else:
                print("Mauvaise devinette")
                tentative_restantes = self.enlever_tentative_si_faux(lettre,mot_secret,tentative_restantes)

            print("Mot actuel :", self.afficher_mot_masque(mot_secret,lettre_trouvees))
            print("Lettre déjà devinées :", "," .join(lettre_trouvees))
            print("Tentative restance :", tentative_restantes)

            if self.verifier_si_mot_decouvert(mot_secret,lettre_trouvees):
                print("Félicitations ! vous avez deviné le mot :", mot_secret)
            elif not self.verifier_si_mot_decouvert(mot_secret,lettre_trouvees) and tentative_restantes == 0:
                print("Désolé, vous avez épuisé toutes vos tentatives. Le mot était:", mot_secret)

if __name__ == '__main__':
    jeu_pendu = Pendu()
    jeu_pendu.pendu()