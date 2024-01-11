from pendu import Pendu
import numpy as np
import unittest

class TestPendu(unittest.TestCase):


    def test_mot_choisis_est_string(self):
        jeu_pendu = Pendu()
        self.assertIsInstance(jeu_pendu.choisir_mot(), str)

    def test_si_lettre_existe_dans_mot(self):
        jeu_pendu = Pendu()
        lettre_trouver = "l"
        mot_secret = "soleil"
        self.assertTrue(np.array_equal(jeu_pendu.lettre_existe(lettre_trouver, mot_secret), [2, 5]))

    def test_si_lettre_existe_pas_dans_mot(self):
        jeu_pendu = Pendu()
        lettre_trouver = "z"
        mot_secret = "soleil"
        self.assertTrue(np.array_equal(jeu_pendu.lettre_existe(lettre_trouver, mot_secret), []))

    def test_si_mot_se_demasque_une_lettre(self):
        jeu_pendu = Pendu()
        lettre_trouver = "s"
        mot_secret = "soleil"
        mot_masque =[]
        self.assertEqual(jeu_pendu.demasque_mot(lettre_trouver, mot_secret, mot_masque),"s_____")

    def test_si_mot_se_demasque_deux_lettre(self):
        jeu_pendu = Pendu()
        lettre_trouver = "l"
        mot_secret = "soleil"
        mot_masque =[]
        self.assertEqual(jeu_pendu.demasque_mot(lettre_trouver, mot_secret, mot_masque),"s_____")
    def test_si_mot_se_demasque_aucune_lettre(self):
        jeu_pendu = Pendu()
        lettre_trouver = ""
        mot_secret = "soleil"
        mot_masque =[]
        self.assertEqual(jeu_pendu.demasque_mot(lettre_trouver, mot_secret, mot_masque),"s_____")









if __name__ == '__main__':
    unittest.main()