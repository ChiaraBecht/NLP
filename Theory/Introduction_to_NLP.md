# A gentle Introduction to Natural Language Processing (NLP)

## Natural Language Processing in daily Business
To date, many NLP tools are used on a daily basis. Some examples are given in the following:
- DeepL: full text translation tool for a broad range of languages
- Spam filtering which is a text classification task
- next word prediction for text editors
- automatic emotion detection and customer reviews via sentiment analysis 
- Chatbots which are powerful text generation tools that answer a broad range of user questions. They can be specialised to a specific topic or general

Generally, these tasks are quite complex and seem like magic to the user. This repository aims to dig deeper, understand and explain some core concepts as well as some important state-of-the-art models and further shows some custom use cases from own projects.

## How does the magic of NLP comes to life?
### What is NLP?
NLP is a branch of AI, linguistics and software engineering that aims to make machines understand human language. Generally it is an interdisciplinary field which makes it hard to grasp for newbies. Understanding of human language can be broken down in the following subtasks:
- detect the language (e.g. English, French, German, Dutch, Chinese) and can i understand this language?
- detect sentences within a text
- detect words within a sentence
- detect relationships between words
- detect meaning of indivudal words
- distinguish between questions and answers
- detect part-of-speech categories
- abstract the meaning of a sentence or document

All these tasks are conducted by humans seamless and all at once. For NLP models this is not possible, therefore the "understanding" task is broken down in smaller subtastks:
- Detect Language: Is the vocabulary known to the NLP model
- Tokenization: break down documents or sentences into meaningful units the tokens. Tokesn can be paragraphs, sentences or words. This task is non-trivial and highly language specific
- Text vectorization: generate numeric representation of word, sentences or documents. either via one-hot encoding (short-comings: high dimensional, semantic realtionships of words are lost) or embedding (= fixed length vector representations, dimensions may or may not have abstract meaning, semantic meanings are considered)

These three steps are general building blocks of basic models. Each model needs to handle these three steps in order to achieve its goal. These are called downstream tasks and are for example:

- Named Entity recognition (NER): Assign categories to entities in a text. Difficulties arise from words that can belong to different categories. E.g. depending on context Berkley can be an organisation or a location,  Paris can be a name of a person or a city
- Word-sense disambiguation: Identifying the intended sense of given word with multiple meanings
- Part-of-speech tagging: Tag each word in a sentence with its part of speech (noun, verb, adjective, adverb, pronoun, ...)
- Dependency tagging: tag each word in a sentence with its syntactical role (subject, predicate, object, ...)
- Chunking: Identify small phrases, such as noun phrases, that behave like a single unit
- Stemming and Lemmatization: Text normalisation aka reducing words to their base form. Simple approach cut off the pre- and/or suffixes (= stemming), Lemmatization considers context especially POS for distinguishing a base form

These downstream tasks are sequence tagging tasks.

- Text Classification: assign categories to texts, Applications: spam filtering, language identification, sentiment analysis, question answering.


### Text vectorization
Text vectorization describes the task of representing words in a numerical way that can be used as model input. To vectorize texts, all words that occur in that text or better that are important for a certain language need to be represented in a numerical fashion. The collection of words that we need to encode in order to allow a model handling a text in a certain language is called vocabulary. There are different ways of achieving numerical representations. One hot encodings assign vectors to each word in the vocabulary. These vecors are sparse and their dimensionality equals the number of words in the vocabulary. The vector has a 1 at the position of the vector the word stands in the vocabulary list all other entries are 0. This representation provides an unique word vector for each word in the vocabulary, however no conclusions about relationship among words can be drawn. 

Another way of deriving numerical representations are embeddings. This method uses properties of words to compute dense word vectors that capture relationships amongst words but as well provide an unique numerical representation for each word in the vocabulary. The length of the vectors is fixed and can be chosen by the user. The slideshow provides an example that explains this method more visually. The more words the vocabulary contains the more categories can be found but as well more annotation work is necessary. Therefore, this step shall be automated which is possible using neural networks. (I will keep technical details short here, maybe i will dig into this topic more when i have gained a better understanding).

For now I want to dig a bit more into the idea of embeddings in general and come back to the how we produce them later. Embeddings provide us with a fixed length dense vector for each word in vocabulary. When we study a couple of words such as woman, girl, boy, man, king and queen we find that the following equation holds:

**King - Man + Woman ~= Queen**

This equation is the Hello World of NLP and proves at the same time that models are able to find numerical representations that indeed cover some sort of properties that relate words. This equation can be rewritten into the following statement:

**Word A relates to Word B AS Word C relates to Word D**

One of the small NLP tools I have implemented (following the book about flair, see in the README references) is an analogy solver that computes Word D given an input of Word A, Word B and Word C. You can find the analogy solver in this repository.

Over time, many different embedding methods were published. One of the first embeddings (not the initial one) is Word2Vec by Mikolov et al. This strategy provides an embedding for every word in the vocabulary list. The embeddings are derived by comparing neighboring words and their relationships. So words that often co-occur do share a relationship that words that never co-occur don't. One of the limitations is that out of vocabulary words may occur. If the vocabulary does not cover all words of a language or new words can be created by pasting two existing words together there won't be an embedding for these words available. One embedding method that overcame this problem is the FastText method by Bojanowski et al. They extended the embeddings by creating subwords and adding embeddings for those. As for the previous method relationships between words are derived from neighboring words. One of the latest embedding methods is BERT embedding. These approach is completely different from the already mentioned ones. The embeddings are depending on context. This means that a word can have different embeddings depending on the context it occurs in. The embeddings are derived by comparing pairs of sentences.

### Powerful NLP models
Three models that are currently used (among others) are ELMO by Allen AI, BERT by Google and Open-GPT by OpenAI. Especially, BERT and GPT have revolutionized the field and yield performances that seem like magic to their users. The best known use case of GPT models is probably ChatGPT. 

In the following BERT and GPT are introduced and compared based on the model Architecture, the tasks they conduct, the training data and their output. 
|                      | BERT | GPT |
| ---------------------| :------: | :--:|
| Model Architecture   | bidirectiona Transformer model*  | undirectional (left-sided) Transformer model*  |
| Common tasks         | Supervised tasks such as text classification | unsupervised tasks, such as text generation |
| Training data        | masked language modelling, next sentence prediction | language modelling |
| Output               | fixed length embeddings for downstream NLP tasks | Sequence of tokens of variable length |

* Transformers: specific model architecture unit consisting of encoder decoder blocks (more details may follow)

As we see, the two models differ in the tasks and output they generate. GPT models are well known at the moment due to their surprisingly great performance on producing coherent text that answers all types of questions. BERT models are often used as well however the applications are not directly obvious to the broad mass of users.

### Application for my project
The project i was using NLP for is currently under embargo until it is published. I have conducted this project as my master thesis. The project aims to built a Knowledge Graph from all abstracts found on PubMed using NLP. In short I have worked on sentiment analysis based on verbs in the biomedical context. I have accomplished this with using spaCy and a custom algorithm. Furthermore, I have customized a model that classifies the authors confidence of reported findings. For this part I have worked with the flair library. More details can be requested.

## Concluding Remarks
### Limitations
The limitations concern the applications i have built for the project.

### My favourite NLP tools
- spaCy and ScispaCy: outstanding performance for Lemmatization, with ScispaCy models strong on Biomedical sequence tagging tasks
- flair: strong on embeddings, they have their own embedding method as well as many third party embeddings. Interface for third-party mmodels to be used especially for text classification
- TextBlob: state-of-the-art sentiment analyis
- NLTK: NLP library covering broad spectrum of NLP tasks
- GENSIM: topic modelling (special type of downstream task)
