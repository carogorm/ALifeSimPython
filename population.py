import organism
import random


class Population:

    """ Population Constructor """
    def __init__(self, pop_size, mutation_prob, num_cooperators, num_partials, num_defectors):

        self._REPRO_THRESHOLD = 10
        self.population = []
        self.pop_size = pop_size
        self.mutation_prob = mutation_prob

        self.num_cooperators = num_cooperators
        self.num_partials = num_partials
        self.num_defectors = num_defectors

        # create population of the specified size of randomly generated organisms
       # for i in range(0, pop_size):
        #    org = organism.Organism( self.mutation_prob , self.num_cooperators, self.num_partials, self.num_defectors)
         #   self.population.append(org)
        
        for _ in range(0, self.num_cooperators):
            org = organism.Organism( self.mutation_prob, 10  )
            self.population.append( org )
        for _ in range(0, self.num_partials):
            org = organism.Organism( self.mutation_prob, 5  )
            self.population.append( org )
        for _ in range(0, self.num_defectors):
            org = organism.Organism( self.mutation_prob, 0 )
            self.population.append( org )
    
    """ Public Methods"""
    # update the population 1 time step
    def update(self):
        child_list = []
        # loop through organisms to:
        # 1) update them by calling their update function,
        # 2) check to see if they have enough enough resource to reproduce, reproducing if it does
        # 3) reduce the population back down to it's original size by removing the least fit organism in the population
        #     for example, if you start with a pop of 5 and 3 reproduce, resulting in a pop of 8, remove the 3 least fit
        for i in range(len(self.population)):
            org = self.population[i]
            if org.update():
                left = i-1
                if left < 0:
                    left = len(self.population)-1
                self.population[left].add_resource(4)
                
                right = i +1
                if right == len(self.population):
                    right = 0
                self.population[right].add_resource(4)
                
                    
            if org.get_resource() > self._REPRO_THRESHOLD:
                new_child = org.reproduce()
                child_list.append(new_child)

        # Sorts population by fitness score, from least to most fit
        #self.population.sort()
        # Removes random n organisms 
        random.shuffle( self.population )
        
        self.population = self.population[len(child_list):]
        # Adds children to population
        for child in child_list:
            self.population.append(child)

    """ Getters & Setters """
    # calculates & returns population's mean fitness score
    def get_mean_cooperation(self):
        mean = 0
        for org in self.population:
            mean += org.coop_prob
        mean /= len(self.population)
        return mean

    """ Python Built-in Functions """
    def __getitem__(self, idx):
        return self.population[idx]


""" main function (for testing/debugging) """
'''if __name__ == '__main__':
    # create 1 population of size 5
    my_pop = Population(50)
    print("\n")
    print(my_pop.get_mean_cooperation())

    # update population n times to evolve the population
    for i in range(100):
        my_pop.update()

    print("\n")
    print(my_pop.get_mean_cooperation())'''


