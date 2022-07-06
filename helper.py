import string
import re
import unicodedata

string.punctuation
# defining the function to remove punctuation
import nltk
from nltk.tokenize import ToktokTokenizer

tokenizer = ToktokTokenizer()
stopword_list = nltk.corpus.stopwords.words('english')
# custom: removing words from list
stopword_list.remove('not')

from transformers import GPT2TokenizerFast

tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")


def remove_punctuation(text):
    punctuationfree = "".join([i for i in text if i not in string.punctuation])
    return punctuationfree


# storing the puntuation free text

# function to remove accented characters
def remove_accented_chars(text):
    new_text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return new_text


# call function
# imports

# function to remove special characters
def remove_special_characters(text):
    # define the pattern to keep
    pat = r'[^a-zA-z0-9.,!?/:;\"\'\s]'
    return re.sub(pat, '', text)


def remove_stopwords(text):
    # convert sentence into token of words
    tokens = tokenizer.tokenize(text)
    tokens = [token.strip() for token in tokens]
    # check in lowercase
    t = [token for token in tokens if token.lower() not in stopword_list]
    text = ' '.join(t)
    return text


# call function


# call function
def prepocessing(df):
    df['clean_combined'] = df['final_text'].apply(lambda x: remove_special_characters(x))
    df['clean_combined'] = df['clean_combined'].apply(lambda x: remove_accented_chars(x))
    df['clean_combined'] = df['clean_combined'].apply(lambda x: remove_punctuation(x))
    #df['clean_combined'] = df['clean_combined'].apply(lambda x: remove_stopwords(x))

    # remove reviews that are too long
    df['clean_combined_n_tokens'] = df.clean_combined.apply(lambda x: len(tokenizer.encode(x)))
    return df

