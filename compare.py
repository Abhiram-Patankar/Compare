from difflib import unified_diff

def compare_xml_files(file1, file2):
    # Read both files
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        file1_lines = f1.readlines()
        file2_lines = f2.readlines()

    # Find differences
    diff = unified_diff(
        file1_lines, file2_lines,
        fromfile=file1,
        tofile=file2,
        lineterm=''
    )

    # Print differences
    for line in diff:
        print(line)

# Example usage
compare_xml_files('output.xml', 'outputOTC.xml')
