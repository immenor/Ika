from ika import POSLocator
from collections import namedtuple


class NPVCollocation(namedtuple("NPVCollocation", ["np", "pp", "vp"])):
    def __str__(self):
        return str(f"{self.np} {self.pp} {self.vp}")


class AVCollocation(namedtuple("AVCollocation", ["ap", "vp"])):
    def __str__(self):
        return str(f"{self.ap} {self.vp}")


class ADJNCollocation(namedtuple("ADJNCollocation", ["adjp", "np"])):
    def __str__(self):
        return str(f"{self.adjp} {self.np}")


def build_noun_particle_verb_collocations(chunk):
    collocations = []

    for token in chunk:
        if token.feature_list[0] == "動詞":
            for link in chunk.prev_links:
                np = POSLocator.locate_noun(link)
                pp = POSLocator.locate_particle(link)
                vp = POSLocator.locate_verb(chunk)

                if len(np) > 0 and len(pp) > 0 and len(vp) > 0:
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

                if len(ap) > 0 and len(vp) > 0:
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

                if len(adjp) > 0 and len(np) > 0:
                    collocations.append(
                        ADJNCollocation(adjp, np)
                    )

    return collocations
