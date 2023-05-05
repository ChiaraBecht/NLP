# A gentle Introduction to Natural Language Processing (NLP)

## Natural Language Processing in daily Business
To date, many NLP tools are used on a daily basis. Some examples are given in the following:
- DeepL: full text translation tool for a broad range of languages
- Spam filtering which is a text classification task
- next word prediction for text editors
- automatic emotion detection and customer reviews via sentiment analysis 
- Chatbots which are powerful text generation tools that answer a broad range of user questions. They can be specialised to a specific topic or general

Generally, these tasks are quite complex and seem like magic to the user. This repository aims to dig deeper, understand and explain some core concepts as well as some important state-of-the-art models and further shows some custom use cases from own projects.

## What is NLP? / How does the magic of NLP comes to life?
NLP is a branch of AI, linguistics and software engineering that aims to make machines understand human language. Understanding of human language can be broken down in the following subtasks:
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
- Text Classification: assign categories to texts, Applications: spam filtering, language identification, sentiment analysis.
