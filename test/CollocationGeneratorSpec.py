import unittest
from ika import CollocationGenerator
from cabocha.analyzer import CaboChaAnalyzer


class CollocationGeneratorSpec(unittest.TestCase):
    analyzer = CaboChaAnalyzer()

    def test_can_build_noun_particle_verb_collocation_with_a_verb(self):
        tree = self.analyzer.parse("朝から日本語を勉強する")
        benkyo_suru = tree[2]

        collocations = CollocationGenerator.build_noun_particle_verb_collocations(benkyo_suru)

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
        susundeiru = tree[1]

        collocations = CollocationGenerator.build_adverb_verb_collocations(susundeiru)

        self.assertEqual(collocations[0].vp[0].feature_list[6], "進む")
        self.assertEqual(collocations[0].ap[0].surface, "徐々に")

    def test_can_build_adjective_noun_collocation_with_noun(self):
        tree = self.analyzer.parse("美味しいケーキを食べる")
        keekiwo = tree[1]

        collocations = CollocationGenerator.build_adjective_noun_collocations(keekiwo)

        self.assertEqual(collocations[0].adjp[0].surface, "美味しい")
        self.assertEqual(collocations[0].np[0].surface, "ケーキ")

    def test_only_builds_complete_npv_collocation(self):
        tree = self.analyzer.parse("めっちゃ食べる")
        taberu = tree[1]

        incomplete_npv = CollocationGenerator.build_noun_particle_verb_collocations(taberu)

        self.assertEqual(len(incomplete_npv), 0)

    def test_only_builds_complete_advv_collocation(self):
        tree = self.analyzer.parse("ケーキを食べる")
        taberu = tree[1]

        incomplete_advv = CollocationGenerator.build_adverb_verb_collocations(taberu)

        self.assertEqual(len(incomplete_advv), 0)

    def test_only_builds_complete_adjn_collocation(self):
        tree = self.analyzer.parse("昨日食べた美味しいたこ焼きは最高でした")
        saikou = tree[4]

        incomplete_adjn = CollocationGenerator.build_adjective_noun_collocations(saikou)
        print(incomplete_adjn)

        self.assertEqual(len(incomplete_adjn), 0)


if __name__ == '__main__':
    unittest.main()
