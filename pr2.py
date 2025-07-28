import matplotlib.pyplot as plt

def preemptive_sjf():
    n = int(input("Enter number of processes: "))
    processes = []
    
    for i in range(n):
        at = int(input(f"Enter arrival time for P{i+1}: "))
        bt = int(input(f"Enter burst time for P{i+1}: "))
        processes.append({'pid': f'P{i+1}', 'arrival_time': at, 'burst_time': bt, 'remaining_time': bt, 'completion_time': 0})

    time = 0
    completed = 0
    gantt_chart = []
    waiting_times = {}
    turnaround_times = {}
    prev_process = None

    while completed != n:
        available = [p for p in processes if p['arrival_time'] <= time and p['remaining_time'] > 0]
        if available:
            current = min(available, key=lambda x: x['remaining_time'])
            current['remaining_time'] -= 1

            if prev_process != current['pid']:
                gantt_chart.append((time, current['pid']))
                prev_process = current['pid']

            if current['remaining_time'] == 0:
                current['completion_time'] = time + 1
                tat = current['completion_time'] - current['arrival_time']
                wt = tat - current['burst_time']
                turnaround_times[current['pid']] = tat
                waiting_times[current['pid']] = wt
                completed += 1
        else:
            if prev_process != 'IDLE':
                gantt_chart.append((time, 'IDLE'))
                prev_process = 'IDLE'
        time += 1

    # Table Output
    print("\n📊 Scheduling Table:\n")
    header = f"{'Process':<10}{'Arrival Time':<15}{'Burst Time':<12}{'Waiting Time':<15}{'Turnaround Time':<17}"
    print(header)
    print("-" * len(header))

    total_wt = 0
    total_tat = 0
    for p in processes:
        pid = p['pid']
        at = p['arrival_time']
        bt = p['burst_time']
        wt = waiting_times[pid]
        tat = turnaround_times[pid]
        total_wt += wt
        total_tat += tat
        print(f"{pid:<10}{at:<15}{bt:<12}{wt:<15}{tat:<17}")

    print(f"\n🔹 Average Waiting Time    : {total_wt / n:.2f}")
    print(f"🔹 Average Turnaround Time : {total_tat / n:.2f}")

    # Gantt Chart - Text Version
    print("\n🕒 Gantt Chart:")
    for i in range(len(gantt_chart)):
        start_time = gantt_chart[i][0]
        process = gantt_chart[i][1]
        end_time = gantt_chart[i + 1][0] if i + 1 < len(gantt_chart) else time
        print(f"| {process} ({start_time}-{end_time}) ", end="")
    print("|")

    # Gantt Chart - Visual
    fig, ax = plt.subplots()
    fig, ax = plt.subplots(figsize=(12, 2))
    color_map = plt.cm.get_cmap("tab20")  # 20 unique colors
    colors = {}
    y_base = 10

    for i, (start_time, process) in enumerate(gantt_chart):
        end_time = gantt_chart[i + 1][0] if i + 1 < len(gantt_chart) else time

        if process not in colors:
            if process == "IDLE":
                colors[process] = "gray"
            else:
                colors[process] = color_map(len(colors) % 20)

        ax.broken_barh(
            [(start_time, end_time - start_time)],
            (y_base, 9),
            facecolors=colors[process]
        )
        ax.text(
            start_time + (end_time - start_time) / 2,
            y_base + 4.5,
            process,
            ha="center",
            va="center",
            fontsize=9,
            color="white" if process != "IDLE" else "black"
        )

    ax.set_ylim(5, 25)
    ax.set_xlim(0, time)
    ax.set_xlabel("Time")
    ax.set_yticks([])
    ax.set_title("🕒 Gantt Chart - Preemptive SJF ")
    ax.grid(True)
    plt.tight_layout()
    plt.show()

# Run the scheduler
preemptive_sjf()
