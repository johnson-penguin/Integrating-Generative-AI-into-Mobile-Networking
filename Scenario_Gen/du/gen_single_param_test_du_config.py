import os
import shutil
from du_test_params import test_params

original_config = "/home/oai72/oai_split/openairinterface5g/targets/PROJECTS/GENERIC-NR-5GC/CONF/johnson/du_gnb.conf"
config_output_dir = "/home/oai72/Johnson/tool/scenario_gen/du/du_test_conf"
os.makedirs(config_output_dir, exist_ok=True)

print("參數總數量:", len(test_params))

# === Generate baseline profile ===
baseline_config_path = os.path.join(config_output_dir, "0_du_gnb_original.conf")
shutil.copyfile(original_config, baseline_config_path)
print(f"✅ Baseline config saved to {baseline_config_path}")

# === Generate mutation profiles for each test parameter ===
for idx, (param, (original_line, new_line)) in enumerate(test_params.items(), start=1):
    config_filename = f"{idx}_du_gnb_{param}.conf"
    modified_config_path = os.path.join(config_output_dir, config_filename)

    with open(original_config, 'r') as f:
        content = f.read().replace(original_line, new_line)
    with open(modified_config_path, 'w') as f:
        f.write(content)

    print(f"✅ Generated: {config_filename}")

print("\n🎉 All modified config files generated.")
