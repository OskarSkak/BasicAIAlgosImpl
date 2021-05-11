from local_search import queens_fitness as queen_lib
import random as random

p_mutation = 0.4
num_of_generations = 30
minimal_fitness = 28


def genetic_algorithm(population):

    generation = 0
    fittest_individual = get_fittest_individual(population)
    bool = True
    while queen_lib.fitness_fn_positive(fittest_individual) < minimal_fitness:
        if bool:
            print("Generation {}:".format(generation))
            print_population(population)
            print('Fittest Individual: ', str(queen_lib.fitness_fn_positive(fittest_individual)))

        new_population = []

        for i in range(len(population)):
            mother, father = random_selection(population)
            child = reproduce(mother, father)
            if random.uniform(0, 1) < p_mutation:
                child = mutate(child)
            new_population.append(child)

        fittest_individual = get_fittest_individual(population)

        bool = False

        for i in range(len(population)):
            if queen_lib.fitness_fn_positive(population[i]) < queen_lib.fitness_fn_positive(new_population[i]):
                population[i] = new_population[i]
                bool = True

        generation += 1

    print("Final generation {}:".format(generation))
    print_population(population)

    return fittest_individual


def getTotalFitness(population):
    total_fitness = 0
    for c in population:
        total_fitness += queen_lib.fitness_fn_positive(c)

    return total_fitness

def createInitialPop():
    population = []
    for pop in range(0, 8):
        representation = []
        population.append(representation)
        for column in range(0, 8):
            representation.append(random.randint(1, 8))

    return population


def main():
    initial_pop = createInitialPop()
    print_population(initial_pop)
    fittest = genetic_algorithm(initial_pop)
    print('Fittest Individual: ' + str(fittest))



def get_fittest_individual(iterable = set):
    max_fitness = iterable[0]
    for c in iterable:
        if queen_lib.fitness_fn_positive(max_fitness) < queen_lib.fitness_fn_positive(c):
            max_fitness = c

    return max_fitness


def random_selection(population):
    """
    Compute fitness of each in population according to fitness_fn and add up
    the total. Then choose 2 from sequence based on percentage contribution to
    total fitness of population
    Return selected variable which holds two individuals that were chosen as
    the mother and the father
    """

    # Python sets are randomly ordered. Since we traverse the set twice, we
    # want to do it in the same order. So let's convert it temporarily to a
    # list.

    wheel = []
    total_fitness = 0

    ordered_population = list(population)

    for i in ordered_population:
        total_fitness = queen_lib.fitness_fn_positive(i)
        for j in range(total_fitness):
            wheel.append(i)
    lenght = len(wheel) - 1
    mother = wheel[random.randint(0, lenght)]
    father = wheel[random.randint(0, lenght)]

    return mother, father


def mutate(individual):
    '''
    Mutate an individual by randomly assigning one of its bits
    Return the mutated individual
    '''
    random_col = random.randint(0, 7)
    random_row = random.randint(1, 8)

    individual[random_col] = random_row

    return individual



def reproduce(mother, father):
    '''
    Reproduce two individuals with single-point crossover
    Return the child individual
    '''

    single_point_crossover = random.randint(0, 6)
    childList = []
    for c in mother:
        childList.append(c)

    childList[single_point_crossover] = father[single_point_crossover]

    return childList


def print_population(population):
    for individual in population:
        fitness = queen_lib.fitness_fn_positive(individual)
        print("{} - fitness: {}".format(individual, fitness))



if __name__ == '__main__':

    main()