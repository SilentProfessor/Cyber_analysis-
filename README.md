# Cybersecurity Log Preprocessing & Brute-Force Detection

This project automates the preprocessing of Linux system logs and identifies brute-force SSH login attempts based on IP analysis.

## Features

- Cleans and deduplicates `/var/log/auth.log`
- Reduces log to recent entries for quick analysis
- Extracts and counts brute-force login attempts
- Outputs top offending IP addresses

## Files

- `process.py` — Python script for cleaning, reducing, and analyzing logs
- `process.sh` — Bash script alternative
- `cleaned_auth.log` — Cleaned and deduplicated log
- `reduced_auth.log` — Reduced log (last 1000 lines)
- `top_brute_force_ips.txt` — Top 10 IPs with most brute-force attempts

## Requirements

- Python 3.x
- Linux system with `/var/log/auth.log` (Debian/Ubuntu-based)
- Root access (for reading system logs)

## Usage

### Python Script

```bash
sudo python3 process.py

Bash Script
chmod +x process.sh
sudo ./process.sh

Output Example
192.168.1.100: 12 attempts
203.0.113.50: 9 attempts
...

License
MIT License

Author
Your Name – GitHub Profile


---

### **Steps to Upload to GitHub:**

1. **Create GitHub Repository**

   - Go to [GitHub](https://github.com) > New Repository
   - Name it e.g., `cybersec-log-analyzer`

2. **Push Code from Local Terminal**

   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/log-analyzer.git
   git push -u origin main

