def process_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            lines = infile.readlines()

        # Process each line
        processed_lines = []
        for line in lines:
            # Split the line by the pipe symbol
            parts = line.split('|')
            
            parts[3] = parts[3] + '|'
            
            newline = parts[0] + '|' + parts[1] + '|' + parts[2] + '|' + parts[3] + '|' + parts[4] + '|' + parts[5]
            
            processed_lines.append(newline)

        # Write the modified lines to the output file
        with open(output_file, 'w') as outfile:
            outfile.writelines(processed_lines)

        print(f"Processed {len(lines)} lines. Output saved to {output_file}")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")

# Example usage
input_filename = 'data_cache.txt'  # Replace with your input file name
output_filename = 'output.txt'  # Replace with your desired output file name
process_file(input_filename, output_filename)
