## Solutions Considered  

When designing this log extraction script, several approaches were considered to efficiently filter logs for a specific date:  

### 1. Line-by-Line Reading (Standard Approach)  
- This method involves reading the file line by line using a simple loop and checking if the line starts with the given date.  
- **Pros**: Low memory usage, easy to implement.  
- **Cons**: Can be slow for very large log files since each line is processed sequentially.  

### 2. Loading the Entire File into Memory  
- One option was to read the entire log file into memory as a string and then use string operations to extract relevant lines.  
- **Pros**: Potentially faster for smaller files due to efficient string operations.  
- **Cons**: Not feasible for large files due to high memory consumption, risking performance issues or crashes.  

### 3. Using Memory-Mapped Files (`mmap`)  
- Instead of reading the entire file at once, `mmap` allows treating the file as if it were a list in memory, enabling efficient searching.  
- **Pros**: Faster access, efficient memory usage since only required parts of the file are loaded on demand.  
- **Cons**: Slightly more complex to implement and may require handling encoding and memory constraints.  

## Final Solution Summary  

The final implementation uses **memory-mapped files (`mmap`)** because it balances performance and memory efficiency. This approach allows quick searching through the log file without loading it entirely into RAM. The script iterates over the log lines, checks for the specified date at the beginning of each line, and writes matching entries to an output file. Additionally, it includes error handling for file access issues, memory limitations, and unexpected errors.  

This solution was chosen as it performs well even for large log files while avoiding excessive memory usage.  

## Steps to Run  

Follow these steps to run the script successfully:  

### 1. Ensure Python is Installed  
- The script requires Python 3.x. You can check your installed version by running:  
  ```sh
  python --version
  ```  

### 2. Prepare the Log File  
- Ensure that the log file (`logs_2024.log`) is in the same directory as the script.  

### 3. Run the Script with a Date Argument  
- Open a terminal or command prompt.  
- Navigate to the directory containing `extract_logs.py`.  
- Run the script using:  
  ```sh
  python extract_logs.py YYYY-MM-DD
  ```  
  Replace `YYYY-MM-DD` with the desired date. Example:  
  ```sh
  python extract_logs.py 2024-01-15
  ```  

### 4. Check the Output  
- The extracted logs will be saved in the `output` directory with the filename `output_YYYY-MM-DD.txt`.  
- Example output file: `output/output_2024-01-15.txt`.  

### 5. Handle Errors if Needed  
- If the log file is missing, ensure that `logs_2024.log` is in the correct location.  
- If you encounter a memory error, try breaking the file into smaller chunks.