from cabocha.analyzer import CaboChaAnalyzer
import POSLocator
analyzer = CaboChaAnalyzer()

sentences = [
            "形態素解析済みデータに対し, 文節の区切り情報が付与されます",
            "今日は石山さんと一緒に語るのは結構時間が掛かりました",
            "郊外の地域では、終電後のタクシー乗り場に長蛇の列ができることが多い。",
            "革命政府は、民衆から兵を募って砲戦するとともに、共和政治を確立して、捉えていたルイ１６世を処刑しました",
            "ゆっくり相手に近づける"
            ]


def parse(sentences):
    for sentence in sentences:
        tree = analyzer.parse(sentence)

        for chunk in tree:
            for token in chunk:

                if token.feature_list[0] == "動詞":

                    print("Verb ", POSLocator.locate_verb(chunk))

                    for link in chunk.prev_links:
                        nouns = POSLocator.locate_noun(link)
                        particles = POSLocator.locate_particle(link)
                        adverbs = POSLocator.locate_adverb(link)

                        print("nouns of this verb ", nouns)
                        print("particles of this verb ", particles)
                        print("adverbs of this verb", adverbs)

                    relative_clause_nouns = POSLocator.locate_noun(tree[chunk.link])
                    print("relative clause nouns", relative_clause_nouns)
                    print("===========================================")


parse(sentences)

