import os
import subprocess
import time
from datetime import datetime

# === 設定 ===
build_dir = "/home/oai72/oai_split/openairinterface5g/cmake_targets/ran_build/build"
cu_config = "../../../targets/PROJECTS/GENERIC-NR-5GC/CONF/johnson/cu_gnb.conf"
du_config_dir = "/home/oai72/Johnson/tool/scenario_gen/du/du_test_conf"
log_output_dir = "/home/oai72/Johnson/tool/scenario_gen/du/du_test_log"


import sys

# 將所有輸出導向 log 檔 + terminal
class Tee:
    def __init__(self, logfile_path):
        self.terminal = sys.stdout
        self.log = open(logfile_path, "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        self.terminal.flush()
        self.log.flush()

# 最上方加這段
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
console_log_path = f"/home/oai72/Johnson/tool/scenario_gen/du/du_test_log/console_log.txt"
sys.stdout = sys.stderr = Tee(console_log_path)










# 建立 log 資料夾
os.makedirs(log_output_dir, exist_ok=True)
print("📁 Log folder created.")

# 取得所有 DU config
du_confs = sorted(f for f in os.listdir(du_config_dir) if f.endswith(".conf"))
print("📄 Found DU config files:", du_confs)

# 進入執行目錄
os.chdir(build_dir)

summary = []

# === 測試每個 DU 設定檔 ===
for idx, du_conf in enumerate(du_confs, 1):
    du_conf_path = os.path.join(du_config_dir, du_conf)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    cu_log = os.path.join(log_output_dir, f"cu_log_{du_conf}_{timestamp}.txt")
    du_log = os.path.join(log_output_dir, f"du_log_{du_conf}_{timestamp}.txt")

    print(f"\n🚀 [{idx}] Testing DU config: {du_conf}")

    # 啟動 CU
    with open(cu_log, "w") as cu_log_f:
        cu_proc = subprocess.Popen(
            ["sudo", "./nr-softmodem", "--rfsim", "--sa", "-O", cu_config],
            stdout=cu_log_f,
            stderr=subprocess.STDOUT,
            env=dict(os.environ, RFSIMULATOR="server")
        )
        print("🔧 CU started.")
        time.sleep(10)

    # 啟動 DU
    with open(du_log, "w") as du_log_f:
        du_proc = subprocess.Popen(
            ["sudo", "./nr-softmodem", "--rfsim", "--sa", "-O", du_conf_path],
            stdout=du_log_f,
            stderr=subprocess.STDOUT,
            env=dict(os.environ, RFSIMULATOR="server")
        )
        print("📡 DU started.")
        time.sleep(30)

    # 關閉 CU / DU
    cu_proc.kill()
    du_proc.kill()
    cu_proc.wait(timeout=5)
    du_proc.wait(timeout=5)

    # 預設狀態
    status = "✅ Success"

    # 檢查 log
    if os.path.getsize(du_log) == 0:
        status = "❌ DU log empty"
    else:
        with open(du_log, 'r', encoding='utf-8', errors='ignore') as logf:
            log_content = logf.read()
            if "Assertion" in log_content or "couldn't be loaded" in log_content:
                status = "❌ Error in DU startup"
            elif "got sync" not in log_content and "RF started" not in log_content:
                status = "⚠️ No sync or RF start"

    # 加入 summary
    summary.append({
        "index": idx,
        "config_file": du_conf,
        "log_file": du_log,
        "status": status
    })

    # 保險性殺掉殘留
    subprocess.run(["sudo", "pkill", "-f", "nr-softmodem"])
    print(f"{status} | Logs saved.")
    time.sleep(1)

# === 輸出測試總結 ===
print("\n📊 Summary:")
for s in summary:
    print(f"- [{s['index']}] {s['config_file']} => {s['status']}")
