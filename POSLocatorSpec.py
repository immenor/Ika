import unittest
import POSLocator
from cabocha.analyzer import CaboChaAnalyzer


class POSLocatorTests(unittest.TestCase):
    analyzer = CaboChaAnalyzer()

    def test_can_find_a_particle(self):
        tree = self.analyzer.parse("今日は石山さんと一緒に語るのは結構時間が掛かりました")
        particles = POSLocator.locate_particle(tree.chunks[5])
        self.assertEqual(particles[0].surface, "が")

    def test_can_find_a_particle_combo(self):
        tree = self.analyzer.parse("僕には無理です")
        particles = POSLocator.locate_particle(tree.chunks[0])
        self.assertEqual(particles[0].surface, "に")
        self.assertEqual(particles[1].surface, "は")

    def test_can_find_a_noun(self):
        tree = self.analyzer.parse("今日は果物を買います")
        nouns = POSLocator.locate_noun(tree.chunks[1])
        self.assertEqual(nouns[0].surface, "果物")

    def test_can_find_an_adv(self):
        tree = self.analyzer.parse("ゆっくり歩く")
        nouns = POSLocator.locate_adverb(tree.chunks[0])
        self.assertEqual(nouns[0].surface, "ゆっくり")


if __name__ == '__main__':
    unittest.main()
