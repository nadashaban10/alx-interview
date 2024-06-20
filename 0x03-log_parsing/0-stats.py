#!/usr/bin/python3
"""
Log parsing
"""

import sys

# Main execution starts here
if __name__ == '__main__':

    # Initialize filesize and count variables
    filesize, count = 0, 0
    # Define a list of HTTP status codes to track
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    # Initialize a dictionary to count occurrences of each status code
    stats = {k: 0 for k in codes}

    # Function to print the current statistics
    def print_stats(stats: dict, file_size: int) -> None:
        # Print the total filesize
        print("File size: {:d}".format(filesize))
        # Print the count of each status code, sorted by code
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

    # Main loop to process lines from stdin
    try:
        for line in sys.stdin:
            # Increment the line count
            count += 1
            # Split the line into components
            data = line.split()
            try:
                # Extract the status code from the line
                status_code = data[-2]
                # If the status code is one we're tracking, increment its count
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                # Ignore any errors in processing the status code
                pass
            try:
                # Add the size of the current request to the total filesize
                filesize += int(data[-1])
            except BaseException:
                # Ignore any errors in processing the filesize
                pass
            # Every 10 lines, print the current statistics
            if count % 10 == 0:
                print_stats(stats, filesize)
        # After processing all lines, print the final statistics
        print_stats(stats, filesize)
    except KeyboardInterrupt:
        print_stats(stats, filesize)
        raise
