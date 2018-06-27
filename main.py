from cabocha.analyzer import CaboChaAnalyzer

analyzer = CaboChaAnalyzer()
tree = analyzer.parse("日本語")
for chunk in tree:
    for token in chunk:
        print(token)
