# Step 1: Read input file
with open('input.txt', 'r') as f:
    lines = f.readlines()

# Step 2: Split each line into separate texts
split_lines = [line.strip().split(':') for line in lines]

# Step 3: Determine the number of texts in each line
num_texts = max(len(split_line) for split_line in split_lines)

# Step 4: Ask the user which part to export
print(f"Which part would you like to export? (1-{num_texts})")
export_index = int(input()) - 1  # Convert user input to 0-indexed

# Step 5: Extract the specified text from each line
output_lines = [split_line[export_index] if export_index < len(split_line) else split_line[-1] for split_line in split_lines]

# Step 6: Write output file
with open('output.txt', 'w') as f:
    f.write('\n'.join(output_lines))

print("Successfully exported")

# Created by Twissen using ChatGPT
# https://twissen.sellix.io/ & https://twissenservices.sellix.io/