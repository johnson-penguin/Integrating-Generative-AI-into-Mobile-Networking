import re
import json

def extract_conf_key_value_pairs(conf_path, output_json_path):
    with open(conf_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    segments = []
    current_block = []
    inside_block = False
    current_label = None

    for line in lines:
        stripped = line.strip()

        # 開始區塊，如 security = {
        if re.match(r'^\w+\s*=\s*\{', stripped):
            inside_block = True
            current_label = re.match(r'^(\w+)\s*=', stripped).group(1)
            current_block = [stripped]
            continue

        # 處於區塊內部
        if inside_block:
            current_block.append(line.rstrip('\n'))
            if stripped.endswith('};'):
                # 區塊結束，提取內部單行 key=value
                block_body = "\n".join(current_block)
                for match in re.finditer(r'^\s*(\w+)\s*=\s*(.*?);', block_body, flags=re.MULTILINE):
                    key = match.group(1)
                    value = match.group(0).strip()
                    segments.append({
                        "label": key,
                        "content": value
                    })
                inside_block = False
                current_block = []
            continue

        # 單行格式
        match = re.match(r'^(\w+)\s*=\s*.*?;', stripped)
        if match:
            label = match.group(1)
            segments.append({
                "label": label,
                "content": stripped
            })

    # 儲存為 JSON
    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump(segments, f, indent=2, ensure_ascii=False)

    return output_json_path

# 執行轉換
converted_path = extract_conf_key_value_pairs(
    conf_path="/home/aiml/johnson/thesis_rag/test_conf_for_building/cu.conf",
    output_json_path="/home/aiml/johnson/thesis_rag/test_conf_for_building/cu_conf.json"
)
converted_path
