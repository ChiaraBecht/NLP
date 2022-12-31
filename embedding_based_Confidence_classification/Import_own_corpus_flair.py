import flair
print(flair.__version__)

# load own corpus
from flair.data import Corpus
from flair.datasets import CSVClassificationCorpus
from pathlib import Path

# this is the folder in which train, test and dev files reside
data_folder = r'C:\\Data_Science_for_Life_Sciences_MASTER\\masterthesis\\Quota_workaround\\NLP\\embedding_based_Confidence_classification\\test_corpus'
#print(data_folder)
column_name_map = {0: "text", 1:"label"}  
label_type = "label" 

corpus = CSVClassificationCorpus(data_folder, 
                                        column_name_map, 
                                        skip_header=True, 
                                        delimiter="|",
                                        #train_file= 'train.csv',
                                        dev_file= 'dev.csv',
                                        #test_file= 'test.csv', 
                                        label_type=label_type)

print(corpus)