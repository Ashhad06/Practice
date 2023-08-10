def read_fasta_file(file_path):
    sequences = {}
    current_sequence = ""
    current_name = None

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if current_name is not None:
                    sequences[current_name] = current_sequence
                current_name = line[1:]
                current_sequence = ""
            else:
                current_sequence += line

        if current_name is not None:
            sequences[current_name] = current_sequence

    return sequences

# Test the function with a sample FASTA file
test_file_path = r'C:\Users\ashhad\Desktop\test.fasta'
fasta_sequences = read_fasta_file(test_file_path)

# Print the sequences and their names
for name, sequence in fasta_sequences.items():
    print("Name:", name)
    print("Sequence:", sequence)
    print("=" * 20)
