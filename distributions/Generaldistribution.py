class Distribution:

    def __init__(self, mu=0, sigma=1):
        """
        Generic parent class for statistical distribution functions. 

        Attributes:
            mean (float) - mean value of the distribution
            stdev (float) - standard deviation of the distribution
            data_list (list of floats) - list of floats extracted from a datafile
        
        """
        self.mean = mu
        self.stdev = sigma
        self.data_list = []

    
    def read_data_file(self, file_name):
        """
        Reads in a data file and stores in the data_list attribute

        Args:
            file_name (str) - name of data file to be read from

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