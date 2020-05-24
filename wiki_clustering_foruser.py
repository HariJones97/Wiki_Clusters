#parameters for scraping
seed_url = 'https://en.wikipedia.org/wiki/London'  #url of wikipedia page used to generate the corpus     

Nbranches = 50                                 #number of branch links to read. 
                                                #These are the most time consuming aspect of the code, selecting over 200 will take considerable time (~5-10 mins)
                                                #selecting a large number of these will also require a large number of clusters to keep them "tidy"         

random_branch_url_selection = True              #if left "False", branch links will be read in the order they appear on the page. If "True", they will be randomly selected
                                                #random branch selection leads to more interesting results but less tidy clusters.

save_corpus_csv = True                          #option to save the corpus dataframe as a .csv. 


#obtaining the corpus: a dataframe of titles and corresponding abstracts from wikipedia entries.
import corpus_collector_func
corpus = corpus_collector_func.corpus_collect(seed_url,Nbranches,random_branch_url_selection,save_corpus_csv)
#import pandas as pd
#corpus = pd.read_csv('corpus.csv')

#parameters for clustering
k = 10                                           #number of clusters to be produced. 
                                                #I find that around Nbranches/5 produces the tidiest results

plot_dimensions = 3                             #takes either 2 or 3. choose to plot cluster distribution on 2d or 3d scatter plot

annotate_plot = False                           #can annotate the scatter plot with article titles, however this becomes messy for larger Nbranches values

save_directory = 'wiki_clusters.csv'            #clusters are outputted as a .csv, define file save location here. 


#cluster the corpus to k clusters, saves a .csv file as the output. 
import wiki_clustering_func
wiki_clustering_func.wikiclust(corpus,k,plot_dimensions,annotate_plot,save_directory)