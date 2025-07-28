def calculate_need(max_need, allocation):
    n = len(max_need)
    m = len(max_need[0])
    need = [[max_need[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]
    return need

def is_safe(n, m, available, max_need, allocation):
    need = calculate_need(max_need, allocation)
    finish = [False] * n
    safe_seq = []
    work = available[:]

    while len(safe_seq) < n:
        found = False
        for i in range(n):
            if not finish[i]:
                if all(need[i][j] <= work[j] for j in range(m)):
                    for j in range(m):
                        work[j] += allocation[i][j]
                    safe_seq.append(i)
                    finish[i] = True
                    found = True
                    break
        if not found:
            return False, [], need
    return True, safe_seq, need

def suggest_remedy(need, available):
    # Suggests a simple fix: increase the available resource type with the most shortfall
    n = len(need)
    m = len(available)
    max_shortfall = [0] * m

    for i in range(n):
        for j in range(m):
            if need[i][j] > available[j]:
                max_shortfall[j] = max(max_shortfall[j], need[i][j] - available[j])

    print("\nSuggested Remedy:")
    for j in range(m):
        if max_shortfall[j] > 0:
            print(f"- Increase Resource {chr(65 + j)} by at least {max_shortfall[j]} units.")

# ------------------------- MAIN PROGRAM -------------------------

# Input
n = int(input("Enter number of processes: "))
m = int(input("Enter number of resource types: "))

print("\nEnter Allocation Matrix (process-wise):")
allocation = []
for i in range(n):
    row = list(map(int, input(f"Allocation for P{i}: ").split()))
    allocation.append(row)

print("\nEnter Maximum Need Matrix (process-wise):")
max_need = []
for i in range(n):
    row = list(map(int, input(f"Max need for P{i}: ").split()))
    max_need.append(row)

available = list(map(int, input("\nEnter Available Resources: ").split()))

# Safety Check
safe, sequence, need = is_safe(n, m, available, max_need, allocation)

# Output
print("\n----------------------------------")
if safe:
    print("System is in a SAFE state.")
    print("Safe Sequence:", ' -> '.join(f'P{p}' for p in sequence))
else:
    print("System is in an UNSAFE state. No safe sequence exists.")
    suggest_remedy(need, available)
