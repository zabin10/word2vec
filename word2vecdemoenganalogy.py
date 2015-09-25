

import gensim
import os
import codecs
import io
import numpy as np
import os
from sklearn.cluster import MiniBatchKMeans as kmeans

#from ggplot import *
import sys


modeleng = gensim.models.Word2Vec.load_word2vec_format('eng300.bin', binary=True)

import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')



from matplotlib import pyplot as plt
from ggplot import *
import pandas as pd
from sklearn.decomposition import PCA





# words= ['langue','chien','éléphant', 'Ukraine','grammaire','anglais']

words= ['king','queen','man','woman']

matrixwords = [modeleng[w] for w in words]
pca = PCA(n_components=2)
wordspca = pca.fit_transform(matrixwords)
pcadf= pd.DataFrame(wordspca, columns=['1st principal component','2nd principal component'])
pcadf['wordlabels']= words
graphique=   ggplot(pcadf,aes(x='1st principal component',y='2nd principal component'))  + geom_point(colour='steelblue') +geom_text(aes(label='wordlabels'),hjust=0, vjust=0)

ggsave(graphique, "wordsinenglishanalogy.png")
