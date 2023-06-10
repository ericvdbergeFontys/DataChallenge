class ReviewViewModel:
    def __init__(self, text, sentiment, emotion, cluster):
        self.text = text
        self.sentiment = sentiment
        self.emotion = emotion
        self.cluster = cluster