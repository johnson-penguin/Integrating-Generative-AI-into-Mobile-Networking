import os
import shutil
import random
from cu_test_params import test_params

original_config = "/home/oai72/oai_split/openairinterface5g/targets/PROJECTS/GENERIC-NR-5GC/CONF/cu_gnb.conf"
config_output_dir = "/home/oai72/Johnson/tool/scenario_gen/cu/cu_test_conf"
os.makedirs(config_output_dir, exist_ok=True)

# ✅ 控制參數：可以指定，也可以留空讓它自動隨機選
# Active_gNBs, amf_ip_address, Num_Threads_PUSCH
# local_s_address, ciphering_algorithms, integrity_algorithms, local_s_if_name
selected_params = ["Active_gNBs", "amf_ip_address","Num_Threads_PUSCH","local_s_address"]  # e.g. ["Num_Threads_PUSCH", "amf_ip_address"]

# ✅ 如果沒指定，從所有可用參數中隨機選幾個
if not selected_params:
    max_random_params = 2  # 可自行調整隨機挑幾個參數
    all_params = list(test_params.keys())
    selected_params = random.sample(all_params, min(max_random_params, len(all_params)))
    print(f"🎲 Randomly selected parameters: {selected_params}")

# === Generate baseline profile ===
baseline_config_path = os.path.join(config_output_dir, "0_cu_gnb_original.conf")
shutil.copyfile(original_config, baseline_config_path)
print(f"✅ Baseline config saved to {baseline_config_path}")

# === 展平 selected 測試項目 ===
flat_params = []
for param in selected_params:
    if param not in test_params:
        print(f"⚠️ Skipped unknown param: {param}")
        continue
    original = test_params[param]["original"]
    for variant in test_params[param]["variants"]:
        flat_params.append({
            "param": param,
            "original": original,
            "new": variant
        })

# === 生成變異組合 ===
for idx, item in enumerate(flat_params, start=1):
    param = item["param"]
    original_line = item["original"]
    new_line = item["new"]

    config_filename = f"{idx}_cu_gnb_{param}.conf"
    modified_config_path = os.path.join(config_output_dir, config_filename)

    with open(original_config, 'r') as f:
        content = f.read().replace(original_line, new_line)
    with open(modified_config_path, 'w') as f:
        f.write(content)

    print(f"✅ Generated: {config_filename}")

print("\n🎉 Config files generated for selected parameters.")
