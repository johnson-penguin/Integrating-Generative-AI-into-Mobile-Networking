import os
import subprocess
import time
import re

# === 工具：清除 ANSI 控制碼（顏色） ===
def remove_ansi(text):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

# === 路徑設定 ===
config_dir = "/home/oai72/Johnson/tool/test_code/cu/cu_test_conf"
log_output_dir = "/home/oai72/Johnson/tool/test_code/cu/cu_test_log"
build_dir = "/home/oai72/oai_split/openairinterface5g/cmake_targets/ran_build/build"
cu_binary = "./nr-softmodem"
cu_cmd_template = f"sudo RFSIMULATOR=server {cu_binary} --rfsim --sa -O {{}}"

# 確保 log 輸出資料夾存在
os.makedirs(log_output_dir, exist_ok=True)

# === 搜尋所有 .conf 設定檔 ===
conf_files = sorted(f for f in os.listdir(config_dir) if f.endswith(".conf"))

# === 執行每個 config 檔案 ===
os.chdir(build_dir)
summary = []

for idx, conf_file in enumerate(conf_files):
    config_path = os.path.join(config_dir, conf_file)
    log_filename = os.path.splitext(conf_file)[0] + "_log.txt"
    log_path = os.path.join(log_output_dir, log_filename)

    print(f"\n🔧 [{idx}] Running config: {conf_file}")

    # 清除殘留程序
    subprocess.run("sudo pkill -9 -f nr-softmo", shell=True)
    time.sleep(1)

    cmd = cu_cmd_template.format(config_path)
    print(f"🛠️ Running: {cmd} for 30 seconds")

    try:
        proc = subprocess.run(
            cmd.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=30,
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

        output = f"⏰ Timeout after 30s\nPartial output:\n{partial_output}"   
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

    time.sleep(1)  # 稍作冷卻避免系統未釋放資源

# === 顯示摘要 ===
print("\n📊 Summary:")
for s in summary:
    print(f"- [{s['index']}] {s['config_file']} => {s['status']}")

print("\n✅ All configs executed.")
