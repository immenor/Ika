from cabocha.analyzer import CaboChaAnalyzer

analyzer = CaboChaAnalyzer()

sentences = [
            "形態素解析済みデータに対し, 文節の区切り情報が付与されます",
            "今日はゴウキさんと一緒に語るのは結構時間が掛かりました",
            "郊外の地域では、終電後のタクシー乗り場に長蛇の列ができることが多い。",
            "革命政府は、民衆から兵を募って砲戦するとともに、共和政治を確立して、捉えていたルイ１６世を処刑しました"
            ]


class Collocation:
    def __init__(self, root, func, head):
        self.root = root
        self.func = func
        self.head = head

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f'Head: "{self.head.surface}", Func: "{self.func.surface}" Root Word: "{self.root.feature_list[6]}")'


def find_particle_pair(token, chunk):

    collocations = []
    for link in chunk.prev_links:

        collocation = Collocation(
            token,
            link[link.func_pos],
            link[link.head_pos]
        )
        collocations.append(collocation)
    return collocations


def parse(sentences):
    for sentence in sentences:
        tree = analyzer.parse(sentence)

        for chunk in tree:
            for token in chunk:
                # if token.feature_list[0] == "名詞":
                #     print("found noun:", token)

                # Verbs working well
                if token.feature_list[0] == "動詞":
                    collocations = find_particle_pair(token, chunk)
                    print(collocations)

                # if token.feature_list[0] == "形容詞":
                #     print("found adjective:", token)

                # if token.feature_list[0] == "副詞":
                #     print("found adverb:", token)


parse(sentences)

