class Population:
    def __init__(self):
        self.genotypes = []

    def generate_initial(self):
        for i in range(POPULATION_SIZE):
            member = Genotype()
            member.generate()
            self.genotypes.append(member)

    def  stochastic_universal_sampling(self):   # Stochastic Universal Sampling
        total_fitness = self.compute_total_fitness()
        point_distance = total_fitness / NUMBER_OF_PARENTS
        start_point = uniform(0, point_distance)
        points = [start_point + i * point_distance for i in range(NUMBER_OF_PARENTS)]

        parents = set()
        while len(parents) < NUMBER_OF_PARENTS:
            shuffle(self.genotypes)
            i = 0
            while i < len(points) and len(parents) < NUMBER_OF_PARENTS:
                j = 0
                while j < len(self.genotypes):
                    if self.get_subset_sum(j) > points[i]:
                        parents.add(self.genotypes[j])
                        break
                    j += 1
                i += 1

        return list(parents)

    def compute_total_fitness(self):
        # total_fitness = 0
        # for member in self.genotypes:
        #     total_fitness += member.get_fitness()
        # return total_fitness

        f = lambda geno: sum([member.get_fitness() for member in geno])
        return f(self.genotypes)

    def crossover(self, parents):
        shuffle(parents)
        for i in range(0, NUMBER_OF_PARENTS, 2):
            parents[i], parents[i + 1] = self.generate_crossover_children(parents[i], parents[i + 1])

    def generate_crossover_children(self, parent_1, parent_2):    # Single Point Crossover
        crossover_point = randrange((4 * NUMBER_OF_POLYGONS) / 10, (6 * NUMBER_OF_POLYGONS) / 10 + 1)
        child_1, child_2 = Genotype(), Genotype()
        f = lambda par, child, i: child.polygons.append(par.polygons[i])
        for i in range(crossover_point):
            f(parent_1, child_1, i)
            f(parent_2, child_2, i)
        for i in range(crossover_point, NUMBER_OF_POLYGONS):
            f(parent_1, child_2, i)
            f(parent_2, child_1, i)
        child_1.mutate()
        child_2.mutate()
        return child_1, child_2

    def mutate(self):
        for genotype in self.genotypes:
            if random() < PROBABILITY_MUTATION:
                genotype.mutate()

    def elitism(self):
        # 8 fittest genotypes are carried forward to the next generation. The remaining members are randomly chosen.
        self.genotypes.sort(key=lambda f: f.get_fitness(), reverse=False)
        self.genotypes = self.genotypes[:ELITISM_NUMBER] + sample(self.genotypes[ELITISM_NUMBER:], POPULATION_SIZE - ELITISM_NUMBER)

    def get_subset_sum(self, end, start=0):
        subset_sum, i = 0.0, start
        while i <= end:
            subset_sum += self.genotypes[i].get_fitness()
            i += 1
        return subset_sum

    def get_best(self):
        return np.argmin([g.get_fitness() for g in self.genotypes])

    def get_best_fitness(self):
        return min([g.get_fitness() for g in self.genotypes])


def generate_color():
    return [randrange(0, 256) for i in range(4)]


def generate_point(x_max, y_max):   # Include offset.
    x, y = randrange(0, x_max + 1), randrange(0, y_max + 1)
    return [x, y]


def make_tuple(vertices):
    return [tuple(vertex) for vertex in vertices]


def get_image_error(image1):
    error = 0.0
    for x in range(IMAGE_WIDTH):
        for y in range(IMAGE_HEIGHT):
            # rgb1, rgb2 = image1.getpixel((x, y)), image2.getpixel((x, y))
            rgb1, rgb2 = image1.getpixel((x, y)), IMAGE_MATRIX[x][y]
            delta = 0.0
            for i in range(3):
                delta += pow(rgb1[i] - rgb2[i], 2)
            error += float(sqrt(delta))

    return error


def initialize_global_vars(image):
    global INPUT_IMAGE, IMAGE_WIDTH, IMAGE_HEIGHT, IMAGE_MATRIX
    INPUT_IMAGE = image
    IMAGE_WIDTH, IMAGE_HEIGHT = image.size
    IMAGE_MATRIX = []
    for x in range(IMAGE_WIDTH):
        current_row = []
        for y in range(IMAGE_HEIGHT):
            current_row.append(INPUT_IMAGE.getpixel((x, y)))
IMAGE_MATRIX.append(current_row)
