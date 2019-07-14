import matplotlib.pyplot as plt

class Sentiment():

    def plot_sentiment(self):
        x = [1,2,3,4,5,6,7,8,9,10,11,12]
        y = [1,2,3,4,5,6,7,8,9,10,110,12]
        plt.plot(x,y, label = "Graph")
        plt.xlabel("Dates")
        plt.ylabel("Sentiment")
        plt.legend()
        plt.show()
        
    
    def plot_favorites(self):
        x = []
        y = []
        plt.xlabel("Dates")
        plt.ylabel("Favorites")
        plt.show()
    
    def execute(self):
        self.plot_sentiment()
        self.plot_favorites()


if __name__ == "__main__":
    trial = Sentiment()
    trial.execute()