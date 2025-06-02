import os
import re

# === Automatically locate input/output based on script's location ===
base_dir = os.path.dirname(os.path.abspath(__file__))
print(f"🔍 Base directory: {base_dir}")
log_path = os.path.join(base_dir, "sample_input", "cu_gnb_with_ansi.log")
output_dir = os.path.join(base_dir, "sample_output")
print(log_path)
print(output_dir)
# === Define ANSI color patterns for status classification ===
status_patterns = {
    'ERROR': re.compile(r'\x1b\[(1;)?31m'),             # Red / bright red
    'WARNING': re.compile(r'\x1b\[(1;)?33m|\x1b\[93m'),  # Yellow / bright yellow
    'INFO': re.compile(r'\x1b\[(1;)?34m'),              # Blue
    'SUCCESS': re.compile(r'\x1b\[(1;)?32m'),           # Green
}

# === Prepare container for logs by status ===
status_logs = {status: [] for status in status_patterns}

# === Try reading the log file ===
if not os.path.exists(log_path):
    print(f"❌ Log file not found at: {log_path}")
    exit(1)

with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        for status, pattern in status_patterns.items():
            if pattern.search(line):
                status_logs[status].append(line)
                break  # Only assign one status per line

# === Ensure output directory exists ===
os.makedirs(output_dir, exist_ok=True)

# === Write logs to output files by status ===
for status, lines in status_logs.items():
    output_file = os.path.join(output_dir, f"log_{status}.txt")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(lines)

print("✅ Logs classified successfully into:", output_dir)
