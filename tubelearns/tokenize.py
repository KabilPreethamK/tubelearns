import spacy
from num2words import num2words
import string

nlp = spacy.load("en_core_web_sm")

class Tokenization:
    def __init__(self) -> None:
        
        pass
    
    def tokenize_raw(self,path):
        tokens_sentences = nlp(path)
        sentences = [sent.text for sent in tokens_sentences.sents]
        return sentences
    
    def tokenize_rawlower(self,path):
        tokens_sentences = nlp(path)
        sentences = [sent.text for sent in tokens_sentences.sents]
        
        cleaning_1 = []
        for token_sentence in sentences:
            cleaned_sentence = []
            for word_token in token_sentence:
                if word_token.isnumeric():
                    
                    cleaned_word = num2words(word_token).lower()
                else:
                    
                    cleaned_word = word_token.lower()
                
                cleaned_sentence.append(cleaned_word)  
        
            cleaned_sentence = "".join(cleaned_sentence)
            cleaning_1.append(cleaned_sentence)
        return cleaning_1

class Cleaning:
    def __init__(self) -> None:
        
        pass
    
    def punct_raw(self,path_to_list):
        punctuation = set(string.punctuation)



        cleaning_2 = []

        for sentence in path_to_list:
            sentence = nlp(sentence)
            cleaned_words_2 = []
            for token in sentence:
                clean_char = []
                for char in token.text:
                    if char not in punctuation:
                        clean_char.append(char)
                cleaned_word = "".join(clean_char)
                if cleaned_word:  # Check if the cleaned word is not empty
                    cleaned_words_2.append(cleaned_word)
            cleaned_sentence_2 = " ".join(cleaned_words_2)
            cleaning_2.append(cleaned_sentence_2)
        return cleaning_2
    


