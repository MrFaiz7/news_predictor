def process_text(text):
    import re
    import nltk
    nltk.data.path.append('C/Users/lenovo/PycharmProjects/NewsClassifier/nltk_data')

    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize

    text = text.lower().replace('\n', ' ').replace('\r', '').strip()
    text = re.sub(' +', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)

    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    text = " ".join(filtered_sentence)
    return text
