import random
import math

"""The Job Shop Scheduling Problem using the Particle Swarm Optimization"""

duration_of_job = []
deadline_of_job = []


def initial_input():
    global population_size
    global number_of_jobs
    global working_matrix
    global velocity_matrix
    global personal_best_matrix
    global global_best_matrix
    """number_of_jobs = int(input("Enter the number of jobs:"))
    for x in range(0, number_of_jobs):
        print("For job", x + 1)
        duration_of_job.append(int(input("Enter the duration of job:")))
        deadline_of_job.append(int(input("Enter the deadline of job:")))"""
    print("Now we begin with Particle Swarm Optimization")
    population_size = int(input("Enter the population size:"))
    working_matrix = [0 for x in range(population_size)]
    velocity_matrix = [[] for x in range(population_size)]
    personal_best_matrix = [0 for x in range(population_size)]
    global_best_matrix = [0 for x in range(population_size)]
    print("And now we have everything we need from you. ThankYou Very Much")


def read_file():
    global duration_of_job
    global deadline_of_job
    global number_of_jobs
    even_count = 0
    with open("saving_integers.txt") as file:
        for line in file:
            working_list = (list(map(int, line.split())))
    for x in working_list:
        if (even_count % 2 == 0):
            duration_of_job.append(working_list[even_count])
            even_count += 1
        else:
            deadline_of_job.append(working_list[even_count])
            even_count += 1
    number_of_jobs = len(duration_of_job)


def initialization():
    """Random initialization of positions, personal best matrix, global best solution and velocity matrix"""
    global working_matrix
    global personal_best_matrix
    global global_best_matrix
    global_best_matrix = random.sample(range(1, number_of_jobs + 1), number_of_jobs)
    for i in range(population_size):
        working_matrix[i] = random.sample(range(1, number_of_jobs + 1), number_of_jobs)
        personal_best_matrix[i] = random.sample(range(1, number_of_jobs + 1), number_of_jobs)
        if fitness_value(personal_best_matrix[i]) > fitness_value(global_best_matrix):
            global_best_matrix = personal_best_matrix[i]
    print("Initialization Complete")


def fitness_value(given=[]):
    delay = []
    total_time_taken = 0
    delay_made = 0
    for x in range(number_of_jobs):
        total_time_taken += duration_of_job[given[x] - 1]
        delay_made = total_time_taken - deadline_of_job[given[x] - 1]
        if (delay_made < 0):
            delay_made = 0
        delay.append(delay_made)
    return 1 + (1 / sum(delay))


def fitness_value_normal(given=[]):
    delay = []
    total_time_taken = 0
    delay_made = 0
    for x in range(number_of_jobs):
        total_time_taken += duration_of_job[given[x] - 1]
        delay_made = total_time_taken - deadline_of_job[given[x] - 1]
        if (delay_made < 0):
            delay_made = 0
        delay.append(delay_made)
    return sum(delay)


def create_a_swap_sequence(a=[], b=[]):
    global number_of_jobs
    return_matrix = []
    for x in range(number_of_jobs):
        for y in range(number_of_jobs):
            if a[x] == b[y] and x != y:
                return_matrix = return_matrix + [x, y]
    return return_matrix


def create_new_velocity_matrix():
    global population_size
    global personal_best_matrix
    global global_best_matrix
    global working_matrix
    global velocity_matrix
    global number_of_jobs
    for x in range(population_size):
        velocity_matrix[x] = velocity_matrix[x] + create_a_swap_sequence(personal_best_matrix[x], working_matrix[x])
        velocity_matrix[x] = velocity_matrix[x] + create_a_swap_sequence(global_best_matrix, working_matrix[x])


def swap(a=[], b=[]):
    x = 0
    while x < len(b):
        temp = a[b[x]]
        a[b[x]] = a[b[x + 1]]
        a[b[x + 1]] = temp
        x += 2
    return a


def create_new_working_matrix():
    global velocity_matrix
    global working_matrix
    global personal_best_matrix
    global global_best_matrix
    for x in range(population_size):
        working_matrix[x] = swap(working_matrix[x], velocity_matrix[x])
        if fitness_value(working_matrix[x]) > fitness_value(personal_best_matrix[x]):
            personal_best_matrix[x] = working_matrix[x]
        if fitness_value(working_matrix[x]) > fitness_value(global_best_matrix):
            global_best_matrix = working_matrix[x]


def print_solution():
    global global_best_matrix
    print("\n\nThe best solution is: " + str(global_best_matrix) + " with a fitness value of: " + str(fitness_value(
        global_best_matrix)) + " and the normal fitness value of: " + str(fitness_value_normal(global_best_matrix)))


def debug_print():
    global population_size
    global number_of_jobs
    global working_matrix
    global velocity_matrix
    global personal_best_matrix
    global global_best_matrix
    print(
        "\n Population Size: " + str(population_size) + "\n Number of Jobs: " + str(
            number_of_jobs) + "\n Working Matrix: " + str(working_matrix) + "\n Velocity Matrix: " + str(
            velocity_matrix) + "\n Personal Best Matrix: " + str(
            personal_best_matrix) + "\n Global Best Matrix: " + str(global_best_matrix))
    print(
        "\n Length of Velocity Matrix: " + str(len(velocity_matrix)) + "\n and the length of the first part is: " + str(
            len(velocity_matrix[0])))


def working():
    iterations = 10
    read_file()
    initial_input()
    initialization()
    for x in range(iterations):
        create_new_velocity_matrix()
        create_new_working_matrix()
    """debug_print()"""
    print_solution()


working()
