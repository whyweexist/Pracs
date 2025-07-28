import threading
import time
import random

NUM_PHILOSOPHERS = 5
forks = [threading.Lock() for _ in range(NUM_PHILOSOPHERS)]
running = True  # Shared flag to stop the simulation

def philosopher(i):
    left = forks[i]
    right = forks[(i + 1) % NUM_PHILOSOPHERS]

    while running:
        print(f"Philosopher {i} is thinking.")
        time.sleep(random.uniform(1, 2))

        # Deadlock prevention: odd philosophers pick up right fork first
        first, second = (left, right) if i % 2 == 0 else (right, left)

        with first:
            print(f"Philosopher {i} picked up fork {i if i % 2 == 0 else (i + 1) % NUM_PHILOSOPHERS}")
            with second:
                print(f"Philosopher {i} picked up fork {(i + 1) % NUM_PHILOSOPHERS if i % 2 == 0 else i}")
                print(f"Philosopher {i} is eating.")
                time.sleep(random.uniform(1, 2))
                print(f"Philosopher {i} has finished eating.")

    print(f"Philosopher {i} is exiting.")

# Start threads
threads = []
for i in range(NUM_PHILOSOPHERS):
    t = threading.Thread(target=philosopher, args=(i,))
    threads.append(t)
    t.start()

# Run the simulation for 20 seconds
time.sleep(20)
running = False  # Signal all threads to stop

# Wait for all threads to exit
for t in threads:
    t.join()

print("\nSimulation stopped gracefully.")
