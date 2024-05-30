import string

positive_words = ["happy", "good", "love", "fantastic"]
negative_words = ["sad", "bad", "hate", "terrible"]

def pre_process_text(text):
    """
    This function pre-processes text for sentiment analysis (lowercase, remove punctuation)

    Args:
        text: The text to pre-process.

    Returns:
        The pre-processed text.
    """
    no_punct = ''.join([char for char in text if char not in string.punctuation])  # Remove punctuation
    processed_text = no_punct.lower()
    return processed_text


def lexicon_based_sentiment(text):
    """
    This function analyzes sentiment using a lexicon-based approach with pre-processing.

    Args:
        text: The text to analyze.

    Returns:
        "positive" if more positive words, "negative" if more negative words,
        "neutral" otherwise.
    """
    processed_text = pre_process_text(text)
    positive_count = 0
    negative_count = 0
    for word in processed_text.split():
        if word in positive_words:
            positive_count += 1
        elif word in negative_words:
            negative_count += 1

    if positive_count > negative_count:
        return "positive"
    elif negative_count > positive_count:
        return "negative"
    else:
        return "neutral"

def analyze_sentiment(text):
    """
    Analyze sentiment using lexicon-based approach.

    Args:
        text: The text to analyze.

    Returns:
        A string indicating sentiment (positive, negative, neutral).
    """
    return lexicon_based_sentiment(text)
