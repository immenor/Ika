import unittest
from ika import CollocationGenerator
from cabocha.analyzer import CaboChaAnalyzer


class CollocationGeneratorSpec(unittest.TestCase):
    analyzer = CaboChaAnalyzer()

    def test_can_build_noun_particle_verb_collocation_with_a_verb(self):
        tree = self.analyzer.parse("朝から日本語を勉強する")
        tokens = tree[2]

        collocations = CollocationGenerator.build_noun_particle_verb_collocations(tokens)

        self.assertEqual(collocations[0].np[0].surface, "朝")
        self.assertEqual(collocations[0].pp[0].surface, "から")
        self.assertEqual(collocations[0].vp[1].surface, "勉強")
        self.assertEqual(collocations[0].vp[0].surface, "する")

        self.assertEqual(collocations[1].np[0].surface, "日本語")
        self.assertEqual(collocations[1].pp[0].surface, "を")
        self.assertEqual(collocations[1].vp[1].surface, "勉強")
        self.assertEqual(collocations[1].vp[0].surface, "する")

    def test_can_build_adverb_verb_collocation_with_verb(self):
        tree = self.analyzer.parse("徐々に進んでいる")
        tokens = tree[1]

        collocations = CollocationGenerator.build_adverb_verb_collocations(tokens)

        self.assertEqual(collocations[0].vp[0].feature_list[6], "進む")
        self.assertEqual(collocations[0].ap[0].surface, "徐々に")

    def test_can_build_adjective_verb_collocation_with_noun(self):
        tree = self.analyzer.parse("美味しいケーキを食べる")
        tokens = tree[1]

        collocations = CollocationGenerator.build_adjective_noun_collocations(tokens)

        self.assertEqual(collocations[0].adjp[0].surface, "美味しい")
        self.assertEqual(collocations[0].np[0].surface, "ケーキ")


if __name__ == '__main__':
    unittest.main()
