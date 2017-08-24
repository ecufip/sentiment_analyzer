import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        self.positives = [x.strip() for x in open(positives,'r').readlines() 
                          if x.startswith(";") == False and x.strip() != ""]
        self.negatives = [x.strip() for x in open(negatives,'r').readlines() 
                          if x.startswith(";") == False and x.strip() != ""]

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        
        # instantiate tokenizer
        tokenizer = nltk.tokenize.TweetTokenizer()
        
        # tokenize text and loop through, updating score per sentiment
        tokens = tokenizer.tokenize(text)
        score = 0
        for word in tokens:
            if word.lower() in self.positives:
                score += 1
            elif word.lower() in self.negatives:
                score -= 1
        return score

