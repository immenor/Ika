from cabocha.analyzer import CaboChaAnalyzer
from ika import CollocationGenerator

analyzer = CaboChaAnalyzer()

sentences = [
            "形態素解析済みデータに対し, 文節の区切り情報が付与されます",
            "今日は石山さんと一緒に語るのは結構時間が掛かりました",
            "郊外の地域では、終電後のタクシー乗り場に長蛇の列ができることが多い。",
            "革命政府は、民衆から兵を募って砲戦するとともに、共和政治を確立して、捉えていたルイ１６世を処刑しました",
            "ゆっくり相手に近づける",
            "昨日食べた美味しいたこ焼きは最高でした"
            ]


def parse(sentences):
    for sentence in sentences:
        print("----------------")
        print(sentence)
        print("----------------")

        tree = analyzer.parse(sentence)
        for chunk in tree:
            npv_collocations = CollocationGenerator.build_noun_particle_verb_collocations(chunk)
            if len(npv_collocations) > 0:
                print(f"{len(npv_collocations)} NPVs: ", npv_collocations)

            av_collocations = CollocationGenerator.build_adverb_verb_collocations(chunk)
            if len(av_collocations) > 0:
                print(f"{len(av_collocations)} AVs Found: ", av_collocations)

            adjn_collocations = CollocationGenerator.build_adjective_noun_collocations(chunk)
            if len(adjn_collocations) > 0:
                print(f"{len(adjn_collocations)} ADJNs Found: ", adjn_collocations)


parse(sentences)

