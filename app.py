# Read the contents of the first file
with open('file1.txt', 'r') as file1:
    content1 = file1.readlines()

# Read the contents of the second file
with open('file2.txt', 'r') as file2:
    content2 = file2.readlines()

# Sort the contents of the files
sorted_content1 = sorted(content1)
sorted_content2 = sorted(content2)

# Find similarities
similarities = set(sorted_content1).intersection(set(sorted_content2))

# Find differences
differences = set(sorted_content1).symmetric_difference(set(sorted_content2))

# Sort similarities and differences
sorted_similarities = sorted(similarities)
sorted_differences = sorted(differences)

# Write sorted content of file1 to a new file
with open('sorted_file1.txt', 'w') as sorted_file1:
    for line in sorted_content1:
        sorted_file1.write(line)

# Write sorted content of file2 to a new file
with open('sorted_file2.txt', 'w') as sorted_file2:
    for line in sorted_content2:
        sorted_file2.write(line)

# Write similarities to a new file in alphabetical order
with open('similarities.txt', 'w') as sim_file:
    sim_file.write('Similarities:\n')
    for line in sorted_similarities:
        sim_file.write(line)

# Write differences to a new file in alphabetical order
with open('differences.txt', 'w') as diff_file:
    diff_file.write('Differences:\n')
    for line in sorted_differences:
        diff_file.write(line)

# Combine similarities and differences into one file in alphabetical order
with open('comparison.txt', 'w') as comp_file:
    comp_file.write('Similarities:\n')
    for line in sorted_similarities:
        comp_file.write(line)
    comp_file.write('\nDifferences:\n')
    for line in sorted_differences:
        comp_file.write(line)

# Print the count of different lines
print(f"Number of different lines: {len(sorted_differences)}")

print("Comparison complete. Check 'sorted_file1.txt', 'sorted_file2.txt', 'similarities.txt', 'differences.txt', and 'comparison.txt' for results.")
