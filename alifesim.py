import population
from matplotlib import pyplot as plt

class ALifeSim:

    """ constructs an Artificial Life Simulator"""
    def __init__(self, pop_size=5, num_iterations=5, mutation_prob=0.1, percent_coop = 1, percent_part = 0.0, percent_defec = 0.0):
        # Number of organisms in the population
        self.pop_size = pop_size
        
        #Error statement 
        if percent_part + percent_defec + percent_coop != 1:
            print("Your percents do not add up to 100.")
        
        #Number of cooperators, defectors and partials
        self.num_cooperators = int(pop_size * percent_coop) 
        self.num_defectors = int(pop_size * percent_defec) 
        self.num_partials = int(pop_size * percent_part) 
        
        # Number of iterations to evolve the population
        self.num_iterations = num_iterations
        # List of the mean cooperation probability score for each update
        self.mean_probability_scores = []
        # DONE construct a population with pop_size individuals
        self.pop = population.Population(self.pop_size, mutation_prob, self.num_cooperators, self.num_partials, self.num_defectors )
        # DONE evolve population for num_iterations
        self.__evolve()


    """ Private Methods """
    # Evolves the population
    def __evolve(self):
        # DONE update the population num_iterations, saving the population's mean fitness score each iteration
        #this method is called num_iteration times 
        for _ in range(self.num_iterations):
            self.pop.update()
            self.mean_probability_scores.append( self.pop.get_mean_cooperation() )
        
        

    """ Public Methods """
    def plot_results(self):
        plt.plot(self.mean_probability_scores)
        plt.xlabel('Update')
        plt.ylabel('Mean Probability Score')
        title = str(self.pop_size) + " Orgs Evolved " + str(self.num_iterations) + " Iterations"
        plt.title(title)
        plt.show()


""" main function """
if __name__ == '__main__':

    #  my_pop_size = 100
    #  my_iterations = 100
    #  my_alife_sim = ALifeSim(my_pop_size, my_iterations )
    #  my_alife_sim.plot_results()

     my_pop_size = 1000
     my_iterations = 1000
     my_alife_sim = ALifeSim(my_pop_size, my_iterations, 9.0 * 10**-5 )
     my_alife_sim.plot_results()

    #  my_pop_size = 1000
    #  my_iterations = 1000
    #  my_alife_sim = ALifeSim(my_pop_size, my_iterations, 0.5 )
    #  my_alife_sim.plot_results()


""" Tasks: 

1. Install the matplotlib package - Done
2. Complete the ALifeSim class TODOs - Done
3. Plot the results of: - Done
    a) small population, small num iterations
    b) small population, large num iterations
    c) large population, large num iterations
4. Refactor the code so that the organism's mutation rate is set by ALifeSim (the same way as pop size & num iterations) - Done
    problem- in organism.py when I print self.mutation_prob on line 9, it prints the mutation_prob for each
    organism in population (okay) followed by the genomes of the 10 organisms
5. Find the mutation rate of a virus (your choice) and of an animal (your choice) in nature 
    Polio - 9.0 × 10−5 substitutions per nucleotide
    Owl monkeys - 0.81 × 10−8 mutations per site ( steadily increased with age of father )
6. Regenerate the plots from step 2 with each of the mutation rates you found. Do you see any differences?
    When mutation_prob = 9.0 e -5, the plot has more spikes and dips than when mutation_prob = 0.1

"""