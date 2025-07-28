import matplotlib.pyplot as plt

def fcfs_disk_scheduling():
    # Get user input with simple validation
    try:
        print("\n=== FCFS Disk Scheduling Algorithm ===\n")
        disk_size = int(input("Enter disk size (e.g., 200): "))
        initial_head = int(input("Enter initial head position: "))
        
        if not 0 <= initial_head < disk_size:
            print(f"Error: Initial head position must be between 0 and {disk_size-1}")
            return
        
        # Get request queue as space-separated numbers
        request_input = input("Enter disk request queue (space-separated numbers): ")
        request_queue = [int(x) for x in request_input.strip().split()]
        
        if not request_queue or any(not 0 <= req < disk_size for req in request_queue):
            print(f"Error: All requests must be between 0 and {disk_size-1} and queue cannot be empty")
            return
    except ValueError:
        print("Error: Please enter valid integer values")
        return
    
    # Process FCFS algorithm
    head_positions = [initial_head] + request_queue
    movements = [abs(head_positions[i] - head_positions[i-1]) for i in range(1, len(head_positions))]
    total_head_movement = sum(movements)
    avg_seek_time = total_head_movement / len(request_queue)
    
    # Display step-by-step movement and results
    print("\nStep-by-step head movement:")
    for i in range(1, len(head_positions)):
        print(f"Move from {head_positions[i-1]} to {head_positions[i]} = {movements[i-1]} cylinders")
    
    print(f"\nTotal head movement: {total_head_movement} cylinders")
    print(f"Average seek time: {avg_seek_time:.2f} cylinders")
    
    # Create visualization
    create_visualization(initial_head, request_queue, disk_size, total_head_movement, avg_seek_time)

def create_visualization(initial_head, request_queue, disk_size, total_movement, avg_movement):
    # Prepare data for visualization
    positions = [initial_head] + request_queue
    x_values = list(range(len(positions)))
    labels = ['Initial'] + [f'Req {i+1}' for i in range(len(request_queue))]
    
    # Create plot with improved styling
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, positions, 'bo-', linewidth=2, markersize=8)
    
    # Add movement labels
    for i in range(1, len(positions)):
        plt.annotate(
            f"{abs(positions[i] - positions[i-1])}",
            xy=((x_values[i] + x_values[i-1])/2, (positions[i] + positions[i-1])/2),
            xytext=(0, 10), textcoords='offset points', ha='center',
            bbox=dict(boxstyle='round,pad=0.3', fc='#f0f0f0', alpha=0.7)
        )
    
    # Enhance plot appearance
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.title('FCFS Disk Scheduling - Head Movement', fontsize=14)
    plt.xlabel('Request Sequence')
    plt.ylabel('Disk Position (Cylinder)')
    plt.xticks(x_values, labels)
    plt.ylim(-5, disk_size + 5)
    
    # Add reference line and statistics
    plt.axhline(y=initial_head, color='r', linestyle='--', alpha=0.5)
    plt.figtext(0.02, 0.02, 
               f"Total Head Movement: {total_movement} cylinders\n"
               f"Average Seek Time: {avg_movement:.2f} cylinders", 
               fontsize=10, bbox=dict(facecolor='#e8f4f8', alpha=0.5))
    
    plt.tight_layout()
    plt.show()

if name == "main":
    try:
        fcfs_disk_scheduling()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
