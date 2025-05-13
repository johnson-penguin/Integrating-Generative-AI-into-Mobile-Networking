import re
import os
import shutil
import random
import json
import argparse
from du_test_params import test_params

# === Meta-parameters controlling test generation ===
num_configs = 3  # Number of config files to generate
num_params_range = (2, 5) # Randomly mutate this many parameters per config

# === Path settings ===
original_config = "/home/oai72/oai_split/openairinterface5g/targets/PROJECTS/GENERIC-NR-5GC/CONF/johnson/du_gnb.conf"
conf_output_dir = "/home/oai72/Johnson/tool/scenario_gen/du/du_multi_param_test_conf/conf"
json_output_dir = "/home/oai72/Johnson/tool/scenario_gen/du/du_multi_param_test_conf/json"

os.makedirs(conf_output_dir, exist_ok=True)
os.makedirs(json_output_dir, exist_ok=True)

# === Save baseline config ===
baseline_config_path = os.path.join(conf_output_dir, "0_du_gnb_original.conf")
shutil.copyfile(original_config, baseline_config_path)
print(f"✅ Baseline config saved to {baseline_config_path}")

# === Load original config content ===
with open(original_config, 'r') as f:
    base_content = f.read()

param_keys = list(test_params.keys())
summary_log = {}

# === Generate config files ===
for i in range(1, num_configs + 1):
    num_params = random.randint(*num_params_range)
    selected_keys = random.sample(param_keys, num_params)
    modified_content = base_content
    mutation_log = {}

    for key in selected_keys:
        entry = test_params[key]
        orig = entry["original"]
        variant = random.choice(entry["variants"])

        pattern = re.escape(orig.strip())
        if re.search(pattern, modified_content):
            modified_content = re.sub(pattern, variant, modified_content)
            mutation_log[key] = {
                "original": orig,
                "variant": variant
            }
        else:
            print(f"⚠️ Not found in config: {key} | {orig}")

    # Save mutated config
    conf_name = f"{i}_du_gnb_random.conf"
    conf_path = os.path.join(conf_output_dir, conf_name)
    with open(conf_path, "w") as f:
        f.write(modified_content)

    # Save corresponding metadata
    json_name = f"{i}_du_gnb_random.json"
    json_path = os.path.join(json_output_dir, json_name)
    with open(json_path, "w") as f:
        json.dump(mutation_log, f, indent=2)

    # Add to summary log
    summary_log[conf_name] = {
        "json": json_name,
        "mutated_params": list(mutation_log.keys())
    }

    print(f"✅ Generated: {conf_name} with {len(mutation_log)} mutated parameters")

# Save summary.json
summary_path = os.path.join(json_output_dir, "summary.json")
with open(summary_path, "w") as f:
    json.dump(summary_log, f, indent=2)
print(f"\n📄 Summary saved to {summary_path}")

print("\nDone ")
