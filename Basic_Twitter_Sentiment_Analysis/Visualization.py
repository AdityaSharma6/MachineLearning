import matplotlib.pyplot as plt

class Sentiment():

    def plot_sentiment(self, negative, positive, neutral):
        slice_labels = ["negative", "positive", "neutral"]
        slices = [negative, positive, neutral]
        colors = ["red", "green", "purple"]
        plt.pie(slices, labels = slice_labels, startangle = 90, colors = colors)
        plt.show()
        
    
    def plot_favorites(self):
        x = []
        y = []
        plt.xlabel("Dates")
        plt.ylabel("Favorites")
        plt.show()
    
    def execute(self):
        self.plot_sentiment(10,12,15)
        self.plot_favorites()


if __name__ == "__main__":
    trial = Sentiment()
    trial.execute()