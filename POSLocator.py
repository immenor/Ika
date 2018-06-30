def locate_particle(chunk):
    particles = []
    func = chunk[chunk.func_pos]
    if func.feature_list[0] == "助詞":

        for i in range(len(chunk.tokens)):
            if chunk[i].feature_list[0] == "助詞":
                particles.append(chunk[i])

    return particles


def locate_noun(chunk):
    nouns = []
    func = chunk[chunk.head_pos]

    if func.feature_list[0] == "名詞":
        for i in range(len(chunk.tokens)):
            if chunk[i].feature_list[0] == "名詞":
                nouns.append(chunk[i])

    return nouns

def locate_adverb(chunk):
    adverbs = []
    func = chunk[chunk.head_pos]

    if func.feature_list[0] == "副詞":
        for i in range(len(chunk.tokens)):
            if chunk[i].feature_list[0] == "副詞":
                adverbs.append(chunk[i])

    return adverbs
