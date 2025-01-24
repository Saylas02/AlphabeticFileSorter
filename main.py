def read_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    return [line.strip() for line in lines if line.strip()]

def sort_tcodes(lines):
    tcodes = []
    for line in lines:
        parts = line.split("\t\t")
        if len(parts) == 2:
            tcodes.append((parts[0], parts[1]))
    return sorted(tcodes, key=lambda x: x[0])

def write_file(sorted_tcodes, output_path):
    with open(output_path, "w") as file:
        for tcode, description in sorted_tcodes:
            file.write(f"{tcode}\t\t{description}\n")

if __name__ == "__main__":
    input_file = "example.txt"
    output_file = "sorted_example.txt"

    lines = read_file(input_file)
    sorted_tcodes = sort_tcodes(lines)
    write_file(sorted_tcodes, output_file)
    print(f"Die sortierten Transaktionen wurden in '{output_file}' gespeichert.")
