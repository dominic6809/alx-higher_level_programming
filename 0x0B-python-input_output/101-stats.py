#!/usr/bin/python3
"""
Reads from standard input and computes metrics.
"""


import sys


def compute_metrics():
    total_file_size = 0
    status_code_counts =
  {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            parts = line.split()
            if len(parts) >= 9:
                status_code = int(parts[-2])
                file_size = int(parts[-1])
                
                # Update metrics
                total_file_size += file_size
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1

            if i % 10 == 0:
                print_statistics(total_file_size, status_code_counts)

    except KeyboardInterrupt:
        print_statistics(total_file_size, status_code_counts)

def print_statistics(total_file_size, status_code_counts):
    print("Total file size:", total_file_size)

    for status_code in sorted(status_code_counts.keys()):
        count = status_code_counts[status_code]
        if count > 0:
            print(f"{status_code}: {count}")

compute_metrics()
