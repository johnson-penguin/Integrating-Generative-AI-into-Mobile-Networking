import os
import re
import random
import string

# === 路徑設定 ===
input_file = "C:/Users/wasd0/Desktop/sample_confile/Scenario_5.conf"
output_dir = "C:/Users/wasd0/Desktop/sample_confile/Scenario_5_sample"
os.makedirs(output_dir, exist_ok=True)

# === patterns ===
ciphering_pattern = r'ciphering_algorithms\s*=\s*\(.*?\);'
integrity_pattern = r'integrity_algorithms\s*=\s*\(.*?\);'

# === 工具：隨機字串生成器 ===
def random_word(length=4):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# === 生成 30 組隨機 integrity_algorithms 組合 ===
random.seed(42)
alg_list = []
while len(alg_list) < 30:
    size = random.randint(1, 4)
    algs = tuple(random_word() for _ in range(size))
    if algs not in alg_list:
        alg_list.append(algs)

# === 讀取原始檔案 ===
with open(input_file, "r", encoding="utf-8") as f:
    original_text = f.read()

# === 統一將 ciphering_algorithms 設為 nea0 ===
text_with_fixed_cipher = re.sub(ciphering_pattern, 'ciphering_algorithms = ( "nea0" );', original_text)

# === 替換 integrity_algorithms 並產生 30 份樣本 ===
for idx, algs in enumerate(alg_list, start=1):
    alg_str = ', '.join(f'"{a}"' for a in algs)
    integrity_line = f'integrity_algorithms = ( {alg_str} );'

    replaced = re.sub(integrity_pattern, integrity_line, text_with_fixed_cipher)

    output_path = os.path.join(output_dir, f"Scenario_5_sample_{idx}.conf")
    with open(output_path, "w", encoding="utf-8") as out_f:
        out_f.write(replaced)
    print(f"✅ Saved: {output_path}")

print("🎉 Done: Replaced ciphering_algorithms and generated 30 integrity_algorithms samples.")
