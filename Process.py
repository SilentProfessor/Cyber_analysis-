import re
from collections import Counter
from datetime import datetime

LOG_FILE = "/var/log/auth.log"
CLEANED_LOG = "cleaned_auth.log"
REDUCED_LOG = "reduced_auth.log"
TOP_IPS_FILE = "top_brute_force_ips.txt"
MAX_LINES = 1000

def clean_log(input_file, output_file):
    seen = set()
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.strip() and line not in seen:
                seen.add(line)
                outfile.write(line)

def reduce_log(input_file, output_file, max_lines=MAX_LINES):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()[-max_lines:]
    with open(output_file, 'w') as outfile:
        outfile.writelines(lines)

def extract_failed_ips(input_file):
    ip_pattern = re.compile(r'Failed password.*from (\d+\.\d+\.\d+\.\d+)')
    with open(input_file, 'r') as file:
        ips = [match.group(1) for line in file for match in [ip_pattern.search(line)] if match]
    return Counter(ips)

def main():
    print("[1] Cleaning log...")
    clean_log(LOG_FILE, CLEANED_LOG)

    print("[2] Reducing log...")
    reduce_log(CLEANED_LOG, REDUCED_LOG)

    print("[3] Analyzing brute-force IPs...")
    ip_counts = extract_failed_ips(REDUCED_LOG)
    top_ips = ip_counts.most_common(10)

    with open(TOP_IPS_FILE, 'w') as outfile:
        for ip, count in top_ips:
            outfile.write(f"{ip}: {count} attempts\n")

    print("\nTop brute-force source IPs:")
    for ip, count in top_ips:
        print(f"{ip}: {count} attempts")

    print("\nOutput files created:")
    print(f" - {CLEANED_LOG}")
    print(f" - {REDUCED_LOG}")
    print(f" - {TOP_IPS_FILE}")

if __name__ == "__main__":
    main()
