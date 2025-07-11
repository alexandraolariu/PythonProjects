LOG_FILE_PATH = 'sample.log'

TARGET_KEYWORD = 'error'

# --- Core Analyzer Function ---
#  Reads a log file and counts occurrences of a specific keyword. Returns:
#         int: The number of times the keyword was found.
#         Returns -1 if the file is not found or an error occurs.

def count_keyword_in_log(log_file_path, keyword):
    count = 0
    keyword_lower = keyword.lower()

    try:
        with open(log_file_path, 'r') as f:
            for line in f:
                if keyword_lower in line.lower():
                    count += 1
    except FileNotFoundError:
        print(f"Error: Log file not found at '{log_file_path}'.")
        return -1
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return -1
    return count


if __name__ == "__main__":
    print(f"Analyzing '{LOG_FILE_PATH}' for occurrences of '{TARGET_KEYWORD}'...")


    found_count = count_keyword_in_log(LOG_FILE_PATH, TARGET_KEYWORD)

    if found_count != -1:
        print(f"\nReport:")
        print(f"'{TARGET_KEYWORD}' found {found_count} times.")
    else:
        print("\nAnalysis failed.")

    print("\nDone.")
