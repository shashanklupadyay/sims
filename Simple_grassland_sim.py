

class Sun:
    def __init__(self):
        self.energy = float('inf')  # Infinite energy source

    def provide_energy(self):
        energy_provided = 500  # Sun provides a fixed amount of energy each time unit
        return energy_provided


class Grass:
    def __init__(self):
        self.energy = 0
        self.population = 1000  # Increased initial grass population

    def photosynthesize(self, sun_energy):
        # Grass converts sun energy into its own energy
        self.energy += sun_energy * 0.01  # Conversion rate of 1%
        # Increase population with available energy (capped to avoid unrealistic explosions)
        growth = min(self.energy / 20, 20)  # Increased growth rate and cap
        self.population += int(growth)
        return self.energy


class Grasshopper:
    def __init__(self):
        self.energy = 0
        self.population = 50  # Reduced initial grasshopper population

    def eat_grass(self, grass_energy):
        # Grasshopper gains energy from eating grass
        energy_consumed = grass_energy * 0.15  # Efficiency rate of 15% for herbivore
        self.energy += energy_consumed
        # Decrease grass energy
        return energy_consumed

    def increase_population(self):
        growth = min(self.energy / 50, 15)  # Increased growth rate and cap for grasshoppers
        self.population += int(growth)


class Snake:
    def __init__(self):
        self.energy = 0
        self.population = 10  # Reduced initial snake population

    def eat_grasshopper(self, grasshopper_energy):
        # Snake gains energy from eating a grasshopper
        energy_consumed = grasshopper_energy * 0.25  # Efficiency rate of 25% for carnivore
        self.energy += energy_consumed
        # Decrease grasshopper energy
        return energy_consumed

    def increase_population(self):
        growth = min(self.energy / 200, 2)  # Even slower growth for carnivores, capped at 2 population increase
        self.population += int(growth)


class Eagle:
    def __init__(self):
        self.energy = 0
        self.population = 2  # Maintained initial eagle population

    def eat_snake(self, snake_energy):
        # Eagle gains energy from eating a snake
        energy_consumed = snake_energy * 0.6  # Efficiency rate of 60%
        self.energy += energy_consumed
        # Decrease snake energy
        return energy_consumed

    def increase_population(self):
        # Increase population based on available energy (arbitrary factor)
        self.population += int(self.energy / 100)


def simulate_food_chain():
    # Create instances of each class
    sun = Sun()
    grass = Grass()
    grasshopper = Grasshopper()
    snake = Snake()
    eagle = Eagle()

    # Simulation loop
    for i in range(1000):  # Simulate for 10 time units
        print(f"Time unit {i + 1}:")
        print("------------------")

        # Energy flow
        sun_energy = sun.provide_energy()  # Sun provides energy to grass
        grass_energy = grass.photosynthesize(sun_energy)  # Grass photosynthesizes

        # Grasshopper eats grass
        grasshopper_energy_consumed = grasshopper.eat_grass(grass_energy)
        grass.energy -= grasshopper_energy_consumed
        grasshopper.increase_population()

        # Snake eats grasshopper
        snake_energy_consumed = snake.eat_grasshopper(grasshopper_energy_consumed)
        grasshopper.energy -= snake_energy_consumed
        snake.increase_population()

        # Eagle eats snake
        eagle_energy_consumed = eagle.eat_snake(snake_energy_consumed)
        snake.energy -= eagle_energy_consumed
        eagle.increase_population()

        # Print the energy and population levels for each entity
        print(f"Sun's remaining energy: infinite")
       
        print(f"Grass's energy: {grass.energy:.2f}, population: {grass.population}")
        
        print(f"Grasshopper's energy: {grasshopper.energy:.2f}, population: {grasshopper.population}")
        
        print(f"Snake's energy: {snake.energy:.2f}, population: {snake.population}")
       
        print(f"Eagle's energy: {eagle.energy:.2f}, population: {eagle.population}")
        
        # Wait for 2 seconds between time units
        
        print("\n")

simulate_food_chain()

