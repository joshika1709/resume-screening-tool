from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(resume, jd):
    tfidf = TfidfVectorizer(stop_words='english')
    vectors = tfidf.fit_transform([resume, jd])
    return float(cosine_similarity(vectors[0:1], vectors[1:2])[0][0])
