from .Generaldistribution import Distribution
import math
import matplotlib.pyplot as plt

class Gaussian(Distribution):
    """
    Gaussian distribution class for visualising gaussian distributions
    
    Attributes:
        mean (float) - mean value of the distribution
        stdev (float) - standard deviation of the distribution
        data_list (list of floats) - list of floats extracted from a datafile
    
    """
    def __init__(self, mu=0, sigma=1):
        
        Distribution.__init__(self, mu, sigma)

    def calculate_mean(self):
        """
        Method to calculate the mean of the data set.

        Args:
            none

        Returns:
            float: mean of the data set       
        """
        avg = 1 * sum(self.data_list)/len(self.data_list)
        self.mean = avg
        return self.mean
    
    def calculate_stdev(self, sample=True):
        """
        Method to calculate the standard deviation of the dataset

        Args:
            Sample (bool) - Whether the data represents a sample or a population       

        Returns: 
            float: standard deviation of the data set
        """
        if sample:
            n = len(self.data_list) - 1
        else:
            n = len(self.data_list)

        mean = self.mean
        sigma = 0
        for data in self.data_list:
            sigma += (data - mean) ** 2

        sigma = math.sqrt(sigma/n)

        self.stdev = sigma

        return sigma


    def  read_data_file(self, file_name, sample=True):
        """
        Differs from parent class as it also calculates mean and stdev.

        Args:
            file_name (str) - name of file to be read in
            sample (bool) - Whether the data is a sample or a population

        Returns:
            none
        """
        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()

        self.data_list = data_list
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev(sample)


    def pdf(self, x):
        """
        Probability density function calculator for gaussian function

        Args:
            x (float) - point for calculating pdf

        Returns:
            float - probability distribution function output
        """
        return (1.0 / (self.stdev * math.sqrt(2*math.pi))) * math.exp(-0.5*((x 
                - self.mean) / self.stdev) ** 2)


    def plot_histogram(self):
        """
        Draws a histogram plot of the data

        Args:
            none

        Returns:
            none
        """
        plt.hist(self.data_list)
        plt.title('Histogram of Data')


    def plot_histogram_pdf(self, n_spaces=50):
        """
        Draws normalised histogram of the data and plot pdf along same range

        Args:
            n_spaces (int) - number of data points

        Returns:
            list - x values for pdf plot
            list - y values for pdf plot
        """

        min_range = min(self.data_list)
        max_range = max(self.data_list)

            # calculates the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces

        x = []
        y = []

        # calculate the x values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval*i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # make the plots
        fig, axes = plt.subplots(2,sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data_list, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density')
        plt.show()

        return x, y


    def __add__(self, other):
        """
        Adds two Gaussian objects together

        Args:
            other (Gaussian) - Guassian instance

        Returns:
            Gaussian - Gaussian distribution
        """
        results = Gaussian()
        results.mean = self.mean + other.mean
        results.stdev = math.sqrt(self.stdev ** 2 + other.stdev ** 2)

        return results


    def __repr__(self):
        """
        Outputs characteristic of the instance

        Args:
            none

        Returns:
            str - characteristics of instance
        """
        return "Mean: {}, Standard Deviation: {}".format(self.mean, self.stdev)