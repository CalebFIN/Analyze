
import sys
import nltk
import emoji
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

def preprocess_text(text):  ## Not functional yet
    text = emoji.demojize(text)
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    processed_text = ' '.join([lemmatizer.lemmatize(word.lower()) for word in text.split() if word.lower() not in stop_words])
    return processed_text

def calculate_similarity(text1, text2):
    nltk.download('stopwords', quiet=True)
    nltk.download('wordnet', quiet=True)
    processed_text1 = preprocess_text(text1)
    processed_text2 = preprocess_text(text2)
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([processed_text1, processed_text2])
    similarity_score = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]
    similarity_percentage = similarity_score * 100
    return similarity_percentage

def perform_sentiment_analysis(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)
    return sentiment_scores

def perform_topic_modeling(texts):
    processed_texts = [preprocess_text(text) for text in texts]
    vectorizer = CountVectorizer()
    dtm = vectorizer.fit_transform(processed_texts)
    lda = LatentDirichletAllocation(n_components=5, random_state=42)
    lda.fit(dtm)
    top_words_per_topic = []
    feature_names = vectorizer.get_feature_names_out()
    for topic_idx, topic in enumerate(lda.components_):
        top_words = [feature_names[i] for i in topic.argsort()[:-6:-1]]
        top_words_per_topic.append(top_words)
    return top_words_per_topic

def analyze_text_conversation(reference_texts, new_text):
    reference_text = ' '.join(reference_texts)
    similarity = calculate_similarity(reference_text, new_text)
    sentiment_scores = perform_sentiment_analysis(new_text)
    topics = perform_topic_modeling([reference_text, new_text])

    print("Reference Texts:")
    for text in reference_texts:
        print(text)
    print()
    print("New Text:")
    print(new_text)
    print(f"Similarity: {similarity:.2f}%")
    print("Sentiment scores:")
    print(f"Negative: {sentiment_scores['neg']:.2f}")
    print(f"Neutral: {sentiment_scores['neu']:.2f}")
    print(f"Positive: {sentiment_scores['pos']:.2f}")
    print(f"Compound: {sentiment_scores['compound']:.2f}")
    print("Top words per topic:")
    for i, topic in enumerate(topics):
        print(f"Topic {i+1}: {', '.join(topic)}")


if __name__ == "__main__":
    if len(sys.argv) > 2:
        filename = sys.argv[1]
        with open(filename, 'r') as file:
            reference_texts = file.readlines()
        new_text = sys.argv[2]
        analyze_text_conversation(reference_texts, new_text)
    else:
        print("Please provide the filename and new text as command-line arguments.")
