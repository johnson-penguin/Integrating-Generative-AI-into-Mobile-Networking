import os
import subprocess
import time
import re
import sys
from datetime import datetime

class Tee:
    def __init__(self, log_path):
        self.terminal = sys.stdout
        self.log = open(log_path, "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        self.terminal.flush()
        self.log.flush()

# 🔁 自動儲存 console 輸出
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
console_log_path = f"/home/oai72/Johnson/tool/scenario_gen/cu/cu_test_log/console_log.txt"
sys.stdout = sys.stderr = Tee(console_log_path)
print(f"📥 Logging this run to: {console_log_path}\n")



# === Tool: Clear ANSI control codes (colors) ===
def remove_ansi(text):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

config_dir = "/home/oai72/Johnson/tool/scenario_gen/cu/cu_test_conf"
log_output_dir = "/home/oai72/Johnson/tool/scenario_gen/cu/cu_test_log"
build_dir = "/home/oai72/oai_split/openairinterface5g/cmake_targets/ran_build/build"
cu_binary = "./nr-softmodem"
cu_cmd_template = f"sudo RFSIMULATOR=server {cu_binary} --rfsim --sa -O {{}}"

# Make sure the log output folder exists
os.makedirs(log_output_dir, exist_ok=True)

# === Execute each config file ===
conf_files = sorted(f for f in os.listdir(config_dir) if f.endswith(".conf"))

# === Execute each config file ===
os.chdir(build_dir)
summary = []

for idx, conf_file in enumerate(conf_files):
    config_path = os.path.join(config_dir, conf_file)
    log_filename = os.path.splitext(conf_file)[0] + "_log.txt"
    log_path = os.path.join(log_output_dir, log_filename)

    print(f"\n🔧 [{idx}] Running config: {conf_file}")

    subprocess.run("sudo pkill -9 -f nr-softmo", shell=True)
    time.sleep(1)

    cmd = cu_cmd_template.format(config_path)
    print(f"🛠️ Running: {cmd} for 20 seconds")

    try:
        proc = subprocess.run(
            cmd.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=20,
            text=True
        )
        output = proc.stdout
        status = f"exit={proc.returncode}"
    except subprocess.TimeoutExpired as e:
        partial_output = e.stdout
        if isinstance(partial_output, bytes):
            try:
                partial_output = partial_output.decode("utf-8", errors="ignore")
            except Exception:
                partial_output = "[Unable to decode partial output]"

        output = f"⏰ Timeout after 20s\nPartial output:\n{partial_output}"   
        status = "timeout"

    output = remove_ansi(output)

    with open(log_path, 'w') as f:
        f.write(output)

    print(f"📄 Saved log to {log_path}")
    summary.append({
        "index": idx,
        "config_file": conf_file,
        "log_file": log_path,
        "status": status
    })

    time.sleep(1)  

print("\n📊 Summary:")
for s in summary:
    print(f"- [{s['index']}] {s['config_file']} => {s['status']}")

print("\n✅ All configs executed.")
