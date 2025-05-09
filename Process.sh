#!/bin/bash

LOG_FILE="/var/log/auth.log"
CLEANED_LOG="cleaned_auth.log"
REDUCED_LOG="reduced_auth.log"
TOP_IPS="top_brute_force_ips.txt"

echo "[1] Cleaning log file..."
# Remove empty lines and duplicates
grep -v '^$' "$LOG_FILE" | sort | uniq > "$CLEANED_LOG"

echo "[2] Reducing log file (last 1000 lines)..."
# Reduce to last 1000 lines
tail -n 1000 "$CLEANED_LOG" > "$REDUCED_LOG"

echo "[3] Extracting top IPs from brute-force attempts..."
# Extract brute-force attempts and count offending IPs
grep "Failed password" "$REDUCED_LOG" | awk '{print $(NF-3)}' | \
  sort | uniq -c | sort -nr | head -n 10 > "$TOP_IPS"

echo "Top brute-force source IPs:"
cat "$TOP_IPS"

echo "Done. Output files:"
echo " - Cleaned log: $CLEANED_LOG"
echo " - Reduced log: $REDUCED_LOG"
echo " - Top IPs: $TOP_IPS"
