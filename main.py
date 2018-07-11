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


def print_collocations(title, collocations):
    if len(collocations) > 0:
        print(f"{len(collocations)} {title} ", collocations)


def parse(sentences):
    for sentence in sentences:
        print("----------------")
        print(sentence)
        print("----------------")

        tree = analyzer.parse(sentence)
        for chunk in tree:
            print_collocations("NPV", CollocationGenerator.build_noun_particle_verb_collocations(chunk))
            print_collocations("AV", CollocationGenerator.build_adverb_verb_collocations(chunk))
            print_collocations("ADJN", CollocationGenerator.build_adjective_noun_collocations(chunk))

parse(sentences)
