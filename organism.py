import random
import copy


class Organism:

    """ Organism Constructor """
    def __init__(self, mutation_prob=0.1, num_starting_ones = 7, parent=None ):
        self.mutation_prob = mutation_prob
        self.resource = 0
        self.coop_prob = 0
        # If this organism does not have a parent, randomly generates the genome
        if parent is None:
            self.genome = []
            for i in range(num_starting_ones):
                self.genome.append(1)
            for i in range( 10 - len(self.genome) ):
                self.genome.append(0)
        
        # If this organism has a parent, make an exact copy of the parent's genome
        #   then mutate based on the organism's mutation probability
        else:
            
            self.genome = copy.deepcopy(parent.genome)
            for i in range(0, 10):
                if self.mutation_prob >= random.uniform(0, 1.0):
                    if self.genome[i] == 0:
                        self.genome[i] = 1
                    else:
                        self.genome[i] = 0
        self.__calc_coop_prob()

    """ Private Methods """
    # Calculates the organism's coop_prob score based on the number of 1's in its genome
    def __calc_coop_prob(self): 
        self.coop_prob = 0 
        for bit in self.genome:
            if bit == 1:
                self.coop_prob += 1
        self.coop_prob /= len(self.genome)

    """ Public Methods """
    # Updates the organism 1 time.
    def update(self):
        if self.coop_prob >= random.uniform(0,1):
            self.resource -=1 #loses one energy unit
            return True   
        else:
            self.resource += 1
            return False 
    
    def add_resource(self, val_to_add):
        self.resource += val_to_add
            

    # Reproduce organism (asexual)
    def reproduce(self):
        return Organism(self.mutation_prob, parent=self)

    """ Getters & Setters """
    # Returns the amount of resource the organism currently has
    def get_resource(self):
        return self.resource

    # Returns the organism's coop_prob score
    def get_coop_prob(self):
        return self.coop_prob

    # Prints organism's genome to terminal
    def print_genome(self):
        print(self.genome)

    """ Python Built-in Functions """
    def __repr__(self):
        return str(self.genome)

    def __getitem__(self, idx):
        return self.genome[idx]

    def __lt__(self, rhs):
        if self.coop_prob < rhs.coop_prob:
            return True
        else:
            return False


""" main function (for testing/debugging) """
if __name__ == '__main__':
    # create 1 parent organism
    parent = Organism()
    print('parent: ')
    parent.print_genome()

    print("PARENT cooperation probability: ", parent.get_coop_prob())

    # reproduce asexually
    child = parent.reproduce()
    print('child: ')
    child.print_genome()
    print("CHILD cooperation probability: ", child.get_coop_prob())

    print('parent after reproducing: ')
    parent.print_genome()



