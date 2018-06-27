from cabocha.analyzer import CaboChaAnalyzer

analyzer = CaboChaAnalyzer()

sentences = [
            "形態素解析済みデータに対し, 文節の区切り情報が付与されます",
             "今日はごうきさんと一緒に語るのは結構時間が掛かりました",
             "郊外の地域では、終電後のタクシー乗り場に長蛇の列ができることが多い。",
             "革命政府は、民衆から兵を募って砲戦するとともに、共和政治を確立して、捉えていたルイ１６世を処刑しました"
            ]


def findParticlePair(chunk):
    for link in chunk.prev_links:
        print("particle of verb", link[link.func_pos])
        print("head of that particle", link[link.head_pos])


def parse(sentences):
    for sentence in sentences:
        tree = analyzer.parse(sentence)

        # Start chunk by chunk
        for chunk in tree:
            for token in chunk:
                if token.feature_list[0] == "名詞":
                    print("found noun", token)
                    findParticlePair(chunk)

                if token.feature_list[0] == "動詞":
                    print("found verb:", token)
                    findParticlePair(chunk)

                if token.feature_list[0] == "形容詞":
                    print("found adjective", token)
                    findParticlePair(chunk)

                if token.feature_list[0] == "副詞":
                    print("found adverb", token)


parse(sentences)

