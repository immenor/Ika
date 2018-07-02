from cabocha.analyzer import CaboChaAnalyzer
from ika import POSLocator
from collections import namedtuple
NPVCollocation = namedtuple(
    "NPVCollocation",
    "np pp vp"
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



