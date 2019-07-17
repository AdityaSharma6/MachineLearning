import matplotlib.pyplot as plt

class Visualization():

    def pie_plot_sentiment(self, title, positive, negative, neutral):
        slice_labels = ["negative", "positive", "neutral"]
        slices = [negative, positive, neutral]
        colors = ["red", "green", "purple"]
        plt.pie(slices, labels = slice_labels, startangle = 90, colors = colors)
        plt.title(title)
        plot = plt.show()
        return plot
    
    def dashboard(self, plots):
        dashboard,axs = plt.subplots(2,1)
        axs[0,0].pie() = plots[0]
        axs[0,1].pie() = plots[1]
        plt.show()

        

    def plot_favorites(self):
        x = []
        y = []
        plt.xlabel("Dates")
        plt.ylabel("Favorites")
        plt.show()
    
    def execute(self):
        #self.pie_plot_sentiment(10,12,15)
        self.plot_favorites()


if __name__ == "__main__":
    trial = Visualization()
    trial.execute()