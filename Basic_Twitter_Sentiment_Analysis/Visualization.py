import matplotlib.pyplot as plt

class Visualization():

    def pie_plot_sentiment(self, title, positive, negative, neutral):
        slice_labels = ["Negative", "Positive", "Neutral"]
        slices = [negative, positive, neutral]
        colors = ["red", "green", "purple"]
        plt.pie(slices, labels = slice_labels, startangle = 90, colors = colors)
        plt.legend(title = "Sentiment", slice_labels, loc="upper right")
        plt.title(title)
        plt.show()


    def plot_favorites(self):
        x = []
        y = []
        plt.xlabel("Dates")
        plt.ylabel("Favorites")
        plt.show()

    
    def execute(self):
        self.pie_plot_sentiment("Trial",40,12,25)


if __name__ == "__main__":
    trial = Visualization()
    trial.execute()