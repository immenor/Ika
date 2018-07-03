from cabocha.analyzer import CaboChaAnalyzer
from ika import POSLocator
from collections import namedtuple
NPVCollocation = namedtuple(
    "NPVCollocation",
    "np pp vp"
)

AVCollocation = namedtuple(
    "AVCollocation",
    "ap vp"
)

ADJNCollocation = namedtuple(
    "ADJNCollocation",
    "adjp np"
)

analyzer = CaboChaAnalyzer()


def build_noun_particle_verb_collocations(chunk):
    collocations = []

    for token in chunk:
        if token.feature_list[0] == "動詞":
            for link in chunk.prev_links:
                np = POSLocator.locate_noun(link)
                pp = POSLocator.locate_particle(link)
                vp = POSLocator.locate_verb(chunk)

                collocations.append(
                    NPVCollocation(np, pp, vp)
                )

    return collocations


def build_adverb_verb_collocations(chunk):
    collocations = []

    for token in chunk:
        if token.feature_list[0] == "動詞":
            for link in chunk.prev_links:
                ap = POSLocator.locate_adverb(link)
                vp = POSLocator.locate_verb(chunk)

                collocations.append(
                    AVCollocation(ap, vp)
                )

    return collocations


def build_adjective_noun_collocations(chunk):
    collocations = []

    for token in chunk:
        if token.feature_list[0] == "名詞":
            np = POSLocator.locate_noun(chunk)

            for link in chunk.prev_links:
                adjp = POSLocator.locate_adjective(link)

                collocations.append(
                    ADJNCollocation(adjp, np)
                )

    return collocations

