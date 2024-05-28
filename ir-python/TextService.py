# Service to process text

import re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import PorterStemmer


def preprocess_text(text):
    """
    Preprocesses text by tokenizing, stemming, removing stopwords,
    casefolding, filtering tokens, preserving special cases, and
    handling punctuation and digits.

    Args:
        text (str): The input text to be preprocessed.

    Returns:
        list: A list of preprocessed tokens.
    """
    # Load stopwords
    stop_words = stopwords.words("english")

    # Create stemmer for reducing words to their root forms
    stemmer = PorterStemmer()

    # Define regular expressions for email and URL patterns
    email_regex = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    url_regex = r"https?://[^\s]+"

    # Define a function to handle punctuation and digits
    def clean_token(token):
        if re.match(email_regex, token) or re.match(url_regex, token):
            return token  # Preserve emails and URLs
        else:
            return re.sub(
                r"[^a-zA-Z0-9]", "", token
            )  # Remove all non-alphanumeric characters

    # Split text into words (considering special cases)
    tokens = []
    for word in re.findall(r"(?:" + email_regex + r"|" + url_regex + r"|\S+)", text):
        tokens.append(clean_token(word))

    # Preprocess tokens:
    processed_tokens = []
    for token in tokens:
        # Convert to lowercase (excluding emails and URLs)
        if not re.match(email_regex, token) and not re.match(url_regex, token):
            token = token.lower()
            token = re.sub(r"\d", "", token)  # Drop digits from the token

        # Retain tokens containing at least one alphabetic character
        if any(c.isalpha() for c in token):
            if len(token) > 2:  # Exclude short tokens
                stemmed_token = stemmer.stem(token)  # Reduce word to root form
                if stemmed_token not in stop_words:  # Exclude stopwords
                    processed_tokens.append(stemmed_token)

    return " ".join(processed_tokens)
