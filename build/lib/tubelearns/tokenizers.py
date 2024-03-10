class Tokenization:
    def __init__(self) -> None:
        pass
    
    def TokenizeRaw(self, path):
        import spacy
        nlp = spacy.load("en_core_web_sm")
        tokens_sentences = nlp(path)
        sentences = [sent.text for sent in tokens_sentences.sents]
        return sentences
    
    def TokenizeRawLower(self, path):
        from num2words import num2words
        import spacy
        nlp = spacy.load("en_core_web_sm")
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
    
    def ConjunctSplit(self, sentences, word):
        result = []
        for sentence in sentences:
            if sentence.strip():  
                splitted_sentence = sentence.split(" ")
                
                if word in splitted_sentence:
                    place = splitted_sentence.index(word)
                    left_part = " ".join(splitted_sentence[:place])
                    right_part = " ".join(splitted_sentence[place+1:])
                    left_parts = self.ConjunctSplit([left_part], word)  
                    right_parts = self.ConjunctSplit([right_part], word) 

                    if left_parts:
                        result.extend(left_parts)
                    if right_parts:
                        result.extend(right_parts)
                else: 
                    result.append(sentence)
        return result
    
    def ConjunctSplitList(self, sentences, conjunctions):
        result = []
        for sentence in sentences:
            if sentence.strip():  
                splitted_sentence = sentence.split(" ")
                for word in conjunctions:
                    if word in splitted_sentence:
                        place = splitted_sentence.index(word)
                        left_part = " ".join(splitted_sentence[:place])
                        right_part = " ".join(splitted_sentence[place+1:])
                        left_parts = self.ConjunctSplitList([left_part], conjunctions)
                        right_parts = self.ConjunctSplitList([right_part], conjunctions)

                        if left_parts:
                            result.extend(left_parts)
                        if right_parts:
                            result.extend(right_parts)
                        break
                else: 
                    result.append(sentence)
        return result


class Cleaning:
    def __init__(self) -> None:
        pass
    
    def PunctList(self, path_to_list):
        import spacy
        nlp = spacy.load("en_core_web_sm")
        import string
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
                if cleaned_word: 
                    cleaned_words_2.append(cleaned_word)
            cleaned_sentence_2 = " ".join(cleaned_words_2)
            cleaning_2.append(cleaned_sentence_2)
        return cleaning_2
    
    def PunctRaw(self, path_to_list):
        import spacy
        nlp = spacy.load("en_core_web_sm")
        import string
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
                if cleaned_word:  
                    cleaned_words_2.append(cleaned_word)
            cleaned_sentence_2 = " ".join(cleaned_words_2)
            cleaning_2.append(cleaned_sentence_2)
        cleaning_2 = "".join(cleaning_2)
        return cleaning_2
    
    def Lemmatizer(self, path):
        import spacy 
        nlp = spacy.load("en_core_web_sm")
        lemmatized_sentence = []
        for sentence in path:
            document = nlp(sentence)
            lemmetized_tokens = " ".join([tokens.lemma_.lower() for tokens in document])
            lemmatized_sentence.append(lemmetized_tokens)
        return lemmatized_sentence
    
    def OneLetter(self, list):
        tokens_cleaned_2 = []
        single_letter_words = ["i","a"]
        for sentence in list:
            words = sentence.split(" ")
            tempo = []
            for word in words:
                if len(word) > 1:
                    word = tempo.append(word)
                elif len(word) == 1 and word in single_letter_words:
                    word = tempo.append(word)
                else:
                    pass

        final = " ".join(tempo)
        tokens_cleaned_2.append(final)
        return tokens_cleaned_2
