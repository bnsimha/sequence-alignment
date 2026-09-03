from lingpy import *
from lingpy.algorithm import squareform

languages = ['Norwegian','Swedish','Icelandic','Dutch','English']

distances = squareform([0.5,0.67,0.8,0.2,0.4,0.7,0.6,0.8,0.8,0.3])

tree = neighbor(distances,languages)
print(tree)
'(((Norwegian:0.18,(Swedish:0.12,Icelandic:0.28):0.21):0.17,Dutch:0.31):-0.01,English:-0.01);'

tree = Tree(tree)
print(tree.asciiArt())