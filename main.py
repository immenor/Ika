from cabocha.analyzer import CaboChaAnalyzer
import POSLocator
analyzer = CaboChaAnalyzer()

sentences = [
            "形態素解析済みデータに対し, 文節の区切り情報が付与されます",
            "今日はゴウキさんと一緒に語るのは結構時間が掛かりました",
            "郊外の地域では、終電後のタクシー乗り場に長蛇の列ができることが多い。",
            "革命政府は、民衆から兵を募って砲戦するとともに、共和政治を確立して、捉えていたルイ１６世を処刑しました"
            ]


def parse(sentences):
    for sentence in sentences:
        tree = analyzer.parse(sentence)

        for chunk in tree:
            for token in chunk:

                if token.feature_list[0] == "動詞":
                    if token.feature_list[4] == "サ変・スル":

                        # Found us a suru verb, so we really should go grab its next token
                        for i in range(len(chunk.tokens)):
                            if chunk[i].feature_list[1] == "サ変接続":
                                print("Verb Root:", chunk[i])

                    print("Verb:", token.feature_list[6])
                    for link in chunk.prev_links:
                        nouns = POSLocator.locate_noun(link)
                        particles = POSLocator.locate_particle(link)

                        print("nouns of this verb ", nouns)
                        print("particles of this verb ", particles)

                    print("")


parse(sentences)

