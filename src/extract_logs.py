import mmap
import os
import sys

def extract_logs(input_date):
    input_filename = "logs_2024.log"  # Updated log file name
    output_filename = f"output/output_{input_date}.txt"
    os.makedirs("output", exist_ok=True)  # Ensure output directory exists
    
    try:
        with open(input_filename, "r", encoding="utf-8") as file:
            with mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as mapped_file:
                with open(output_filename, "w", encoding="utf-8") as outfile:
                    for line in iter(mapped_file.readline, b""):
                        line = line.decode("utf-8").rstrip("\r\n")
                        if line.startswith(input_date):
                            outfile.write(line + "\n")
        print(f"Logs for {input_date} extracted successfully to {output_filename}")
    except FileNotFoundError:
        print(f"Error: Could not open file '{input_filename}'.")
    except MemoryError:
        print("Error: Memory limit exceeded. Try processing the file in chunks.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py <YYYY-MM-DD>")
        sys.exit(1)
    
    extract_logs(sys.argv[1])
