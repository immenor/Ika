import unittest
from ika import POSLocator
from cabocha.analyzer import CaboChaAnalyzer


class POSLocatorTests(unittest.TestCase):
    analyzer = CaboChaAnalyzer()

    def test_can_find_a_particle(self):
        tree = self.analyzer.parse("今日は石山さんと一緒に語るのは結構時間が掛かりました")
        jikan_ga = tree.chunks[5]
        particles = POSLocator.locate_particle(jikan_ga)
        self.assertEqual(particles[0].surface, "が")

    def test_can_find_a_particle_combo(self):
        tree = self.analyzer.parse("僕には無理です")
        boku_wa = tree.chunks[0]
        particles = POSLocator.locate_particle(boku_wa)
        self.assertEqual(particles[0].surface, "に")
        self.assertEqual(particles[1].surface, "は")

    def test_can_find_a_noun(self):
        tree = self.analyzer.parse("今日は果物を買います")
        kudamono_wo = tree.chunks[1]
        nouns = POSLocator.locate_noun(kudamono_wo)
        self.assertEqual(nouns[0].surface, "果物")

    def test_can_find_an_adv(self):
        tree = self.analyzer.parse("ゆっくり歩く")
        yukkuri = tree.chunks[0]
        adverbs = POSLocator.locate_adverb(yukkuri)
        self.assertEqual(adverbs[0].surface, "ゆっくり")

    def test_can_find_an_adj(self):
        tree = self.analyzer.parse("美味しいケーキを食べる")
        oishii = tree.chunks[0]
        adjectives = POSLocator.locate_adjective(oishii)
        self.assertEqual(adjectives[0].surface, "美味しい")

    def test_can_find_suru_verb(self):
        tree = self.analyzer.parse("ファイルを添付しました")
        tempu_shimashita = tree.chunks[1]
        verbs = POSLocator.locate_verb(tempu_shimashita)
        self.assertEqual(verbs[0].feature_list[6], "する")
        self.assertEqual(verbs[1].surface, "添付")


if __name__ == '__main__':
    unittest.main()
