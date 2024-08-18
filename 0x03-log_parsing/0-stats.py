#!/usr/bin/python3
"""Log parsing"""

# Importing Libraries
import sys
import re
from typing import Dict


if __name__ == "__main__":
    """ Main Function """
    
    # Pattern to match the log line
    pattern: str = (
        r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'    # IP Address
        r' - \[.*?\] '                            # Datetime
        r'"GET /projects/260 HTTP/1.1" '          # Request method and resource
        r'(\d{3}) '                               # Status code
        r'(\d+)$'                                 # File size
    )

    # Initialize variables
    line_count: int = 0
    size: int = 0
    status: Dict[str, int] = {}

    try: # Handle keyboard interrupt
        while True: # Infinite loop
            # Read stdin line by line
            line: str = sys.stdin.readline().strip()
            if not line:
                break

            # Match the pattern
            match = re.match(pattern, line)
            if not match:
                continue

            # Extract status code and file size from the matched groups
            status_code = match.group(1)
            file_size = int(match.group(2))

            # Update metrics
            size += file_size
            status[status_code] = status.get(status_code, 0) + 1

            # Print metrics every 10 lines
            line_count += 1
            if line_count == 10:
                print(f"File size: {size}")
                for key in sorted(status.keys()): # Sort the status codes
                    print(f'{key}: {status[key]}')
                line_count = 0  # Reset counter after printing

    # Handle keyboard interrupt
    except KeyboardInterrupt:
        print(f"File size: {size}")
        for key in sorted(status.keys()):
            print(f'{key}: {status[key]}')
