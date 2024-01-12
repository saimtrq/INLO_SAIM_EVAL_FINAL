from pendu import Pendu
import numpy as np
import unittest

class TestPendu(unittest.TestCase):


    def test_mot_choisis_est_string(self):
        jeu_pendu = Pendu()
        self.assertIsInstance(jeu_pendu.choisir_mot(), str)

    def test_si_lettre_existe_dans_mot(self):
        jeu_pendu = Pendu()
        lettre = "l"
        mot_secret = "soleil"
        self.assertTrue(jeu_pendu.lettre_existe(lettre, mot_secret))

    def test_si_lettre_existe_pas_dans_mot(self):
        jeu_pendu = Pendu()
        lettres_trouvees = "z"
        mot_secret = "soleil"
        self.assertFalse(jeu_pendu.lettre_existe(lettres_trouvees, mot_secret))

    def test_si_mot_se_demasque_une_lettre(self):
        jeu_pendu = Pendu()
        lettres_trouvees = "s"
        mot_secret = "soleil"
        self.assertEqual(jeu_pendu.afficher_mot_masque(mot_secret, lettres_trouvees,),"s_____")

    def test_si_mot_se_demasque_deux_lettre(self):
        jeu_pendu = Pendu()
        lettres_trouveese = "l"
        mot_secret = "soleil"
        self.assertEqual(jeu_pendu.afficher_mot_masque(mot_secret, lettres_trouveese,),"__l__l")
    def test_si_mot_se_demasque_aucune_lettre(self):
        jeu_pendu = Pendu()
        lettres_trouveese = "z"
        mot_secret = "soleil"
        self.assertEqual(jeu_pendu.afficher_mot_masque(mot_secret, lettres_trouveese,),"______")


    def test_si_tentative_echoue_enleve_nombre(self):
        jeu_pendu = Pendu()
        lettre= "a"
        mot_secret = "soleil"
        tentatives_restantes = 10
        self.assertEqual(jeu_pendu.enlever_tentative_si_faux(lettre, mot_secret,tentatives_restantes), 9)

    def test_si_tentative_echoue_enleve_pas_nombre(self):
        jeu_pendu = Pendu()
        lettre = "s"
        mot_secret = "soleil"
        tentatives_restantes = 10
        self.assertEqual(jeu_pendu.enlever_tentative_si_faux(lettre, mot_secret, tentatives_restantes), 10)

    def test_si_mot_decouvert(self):
        jeu_pendu = Pendu()
        mot_secret = "soleil"
        lettres_trouvees = ["i","e","l","s","o"]
        self.assertTrue(jeu_pendu.verifier_si_mot_decouvert(mot_secret,lettres_trouvees))
    def test_si_mot_pas_decouvert(self):
        jeu_pendu = Pendu()
        mot_secret = "soleil"
        lettres_trouvees = ["y","a","l","s","o"]
        self.assertFalse(jeu_pendu.verifier_si_mot_decouvert(mot_secret,lettres_trouvees))
    def test_si_lettre_deja_devine(self):
        jeu_pendu = Pendu()
        lettre = "s"
        lettres_trouvees = ["s","b","c"]
        self.assertTrue(jeu_pendu.verifier_si_lettre_deja_devine(lettre,lettres_trouvees))
    def test_si_lettre_jamais_devine(self):
        jeu_pendu = Pendu()
        lettre = "a"
        lettres_trouvees = ["s","b","c"]
        self.assertFalse(jeu_pendu.verifier_si_lettre_deja_devine(lettre,lettres_trouvees))










if __name__ == '__main__':
    unittest.main()