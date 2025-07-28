import matplotlib.pyplot as plt
import numpy as np

def fifo_page_replacement():
    # Get user input with validation
    try:
        print("\n=== FIFO Page Replacement Algorithm ===\n")
        frame_count = int(input("Enter number of frames: "))
        
        if frame_count <= 0:
            print("Error: Number of frames must be positive")
            return
            
        # Get reference string as space-separated numbers
        ref_input = input("Enter reference string (space-separated page numbers): ")
        reference_string = [int(x) for x in ref_input.strip().split()]
        
        if not reference_string:
            print("Error: Reference string cannot be empty")
            return
    except ValueError:
        print("Error: Please enter valid integer values")
        return
    
    # Process FIFO algorithm
    frames = []
    page_faults = 0
    page_hits = 0
    states = []  # To store states for visualization
    fault_hit = []  # To track faults and hits
    
    print("\nPage Replacement Process:")
    print("-" * 40)
    print(f"{'Reference':<10}{'Frames':<20}{'Status':<10}")
    print("-" * 40)
    
    for i, page in enumerate(reference_string):
        # Save current state of frames for visualization
        states.append(frames.copy())
        
        if page not in frames:  # Page fault
            page_faults += 1
            fault_hit.append('Fault')
            
            if len(frames) == frame_count:  # If frames are full, remove oldest page
                frames.pop(0)
            frames.append(page)
            status = "Fault"
        else:  # Page hit
            page_hits += 1
            fault_hit.append('Hit')
            status = "Hit"
        
        # Display current state
        frame_str = ', '.join(map(str, frames))
        print(f"{page:<10}{frame_str:<20}{status:<10}")
    
    # Add the final state
    states.append(frames.copy())
    
    # Calculate and display statistics
    total_references = len(reference_string)
    fault_rate = (page_faults / total_references) * 100
    hit_rate = (page_hits / total_references) * 100
    
    print("\n=== Results ===")
    print(f"Total page references: {total_references}")
    print(f"Page faults: {page_faults} ({fault_rate:.2f}%)")
    print(f"Page hits: {page_hits} ({hit_rate:.2f}%)")
    
    # Create visualization
    create_visualization(reference_string, states, fault_hit, frame_count)
  def create_visualization(reference_string, states, fault_hit, frame_count):
    # Prepare figure
    plt.figure(figsize=(12, 6))
    
    # Create a grid for visualization
    references = len(reference_string)
    
    # Plot reference string
    plt.subplot(2, 1, 1)
    for i, page in enumerate(reference_string):
        color = 'red' if fault_hit[i] == 'Fault' else 'green'
        plt.text(i, 0, str(page), ha='center', va='center', 
                 bbox=dict(facecolor=color, alpha=0.3))
    
    plt.xlim(-0.5, references-0.5)
    plt.ylim(-0.5, 0.5)
    plt.title('Reference String with Faults (red) and Hits (green)')
    plt.axis('off')
    
    # Plot frame states
    plt.subplot(2, 1, 2)
    
    # Create a matrix to represent frame states
    matrix = np.full((frame_count, references+1), np.nan)  # Using NaN for empty slots
    
    for i, state in enumerate(states):
        for j, page in enumerate(state):
            if j < frame_count:  # Ensure we don't exceed frame count
                matrix[j, i] = page
    
    # Plot the matrix as a heatmap with custom colors
    cmap = plt.cm.viridis
    plt.imshow(matrix, aspect='auto', cmap=cmap)
    
    # Add text labels to the cells
    for i in range(frame_count):
        for j in range(references+1):
            if not np.isnan(matrix[i, j]):
                plt.text(j, i, f"{int(matrix[i, j])}", ha='center', va='center', color='white')
    
    # Add labels and title
    plt.xlabel('Reference Sequence')
    plt.ylabel('Frames')
    plt.title('FIFO Page Replacement Visualization')
    
    # Set x-ticks to match reference string
    plt.xticks(range(references+1), ['Initial'] + [str(p) for p in reference_string])
    plt.yticks(range(frame_count), [f'Frame {i+1}' for i in range(frame_count)])
    
    # Add statistics as text
    fault_count = fault_hit.count('Fault')
    hit_count = fault_hit.count('Hit')
    fault_rate = (fault_count / references) * 100
    hit_rate = (hit_count / references) * 100
    
    stats = f"Page Faults: {fault_count} ({fault_rate:.2f}%)\n" \
           f"Page Hits: {hit_count} ({hit_rate:.2f}%)"
    
    plt.figtext(0.02, 0.02, stats, fontsize=10, 
               bbox=dict(facecolor='#e8f4f8', alpha=0.5))
    
    # Show plot with tight layout
    plt.tight_layout()
    plt.show()

if name == "main":
    try:
        fifo_page_replacement()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
