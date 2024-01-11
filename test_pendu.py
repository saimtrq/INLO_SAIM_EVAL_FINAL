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
        mot_masque =["_"]*len(mot_secret)
        self.assertEqual(jeu_pendu.demasque_mot(lettre_trouver, mot_secret, mot_masque),['s', '_', '_', '_', '_', '_'])

    def test_si_mot_se_demasque_deux_lettre(self):
        jeu_pendu = Pendu()
        lettre_trouver = "l"
        mot_secret = "soleil"
        mot_masque =["_"]*len(mot_secret)
        self.assertEqual(jeu_pendu.demasque_mot(lettre_trouver, mot_secret, mot_masque),['_', '_', 'l', '_', '_', 'l'])
    def test_si_mot_se_demasque_aucune_lettre(self):
        jeu_pendu = Pendu()
        lettre_trouver = ""
        mot_secret = "soleil"
        mot_masque =["_"]*len(mot_secret)
        self.assertEqual(jeu_pendu.demasque_mot(lettre_trouver, mot_secret, mot_masque),['_', '_', '_', '_', '_', '_'])


    def test_si_tentative_echoue_enleve_nombre(self):
        jeu_pendu = Pendu()
        lettre_trouver = "v"
        mot_secret = "soleil"
        mot_masque = ["_"] * len(mot_secret)
        nombre_tentative = 10
        self.assertEqual(jeu_pendu.enlever_tentative_si_faux(lettre_trouver, mot_secret, mot_masque,nombre_tentative), 9)

    def test_si_tentative_echoue_enleve_pas_nombre(self):
        jeu_pendu = Pendu()
        lettre_trouver = "s"
        mot_secret = "soleil"
        mot_masque = ["_"] * len(mot_secret)
        nombre_tentative = 10
        self.assertEqual(jeu_pendu.enlever_tentative_si_faux(lettre_trouver, mot_secret, mot_masque, nombre_tentative),10)

    def test_si_mot_decouvert(self):
        jeu_pendu = Pendu()
        mot_secret = "soleil"
        mot_masque = ["soleil"]
        self.assertTrue(jeu_pendu.verifier_si_mot_decouvert(mot_masque,mot_secret))
    def test_si_mot_pas_decouvert(self):
        jeu_pendu = Pendu()
        mot_secret = "sole"
        mot_masque = ["soleil"]
        self.assertFalse(jeu_pendu.verifier_si_mot_decouvert(mot_masque, mot_secret))
    def test_si_lettre_deja_devine(self):
        jeu_pendu = Pendu()
        lettres_trouvee = "s"
        lettres_devinee = ["s","b","c"]
        self.assertTrue(jeu_pendu.verifier_si_lettre_deja_devine(lettres_trouvee,lettres_devinee))
    def test_si_lettre_jamais_devine(self):
        jeu_pendu = Pendu()
        lettres_trouvee = "a"
        lettres_devinee = ["s","b","c"]
        self.assertFalse(jeu_pendu.verifier_si_lettre_deja_devine(lettres_trouvee,lettres_devinee))










if __name__ == '__main__':
    unittest.main()