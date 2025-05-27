import re
import json

def extract_conf_segments_flat(conf_path, output_json_path):
    with open(conf_path, 'r', encoding='utf-8') as f:
        conf_text = f.read()

    # 清除註解（避免干擾 parser）
    conf_text = re.sub(r'//.*?$|#.*?$', '', conf_text, flags=re.MULTILINE)

    # 簡單展平括號中的內容（gNBs = (...) / {...}）
    def extract_inner_params(block):
        param_pattern = re.compile(r'(?P<label>\w+)\s*=\s*(?P<value>.+?;)', re.DOTALL)
        return param_pattern.finditer(block)

    # 提取所有區塊
    block_pattern = re.compile(r'(?P<outer_label>\w+)\s*=\s*[\({](?P<block>.*?)[\)}]\s*;', re.DOTALL)
    segments = []

    for match in block_pattern.finditer(conf_text):
        block = match.group('block')
        for sub in extract_inner_params(block):
            label = sub.group('label').strip()
            content = sub.group(0).strip()
            segments.append({
                "label": label,
                "content": content
            })

    # 補上非區塊的獨立設定
    simple_pattern = re.compile(r'(?P<label>\w+)\s*=\s*(?P<value>[^;{}()\n]+);')
    for match in simple_pattern.finditer(conf_text):
        if not any(seg["label"] == match.group("label").strip() for seg in segments):
            segments.append({
                "label": match.group("label").strip(),
                "content": match.group(0).strip()
            })

    # 輸出
    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump(segments, f, indent=2, ensure_ascii=False)

    print(f"✅ 完成展平並輸出至 {output_json_path}")

# 測試用
if __name__ == "__main__":
    extract_conf_segments_flat(
        conf_path="/home/aiml/johnson/Scenario/Scenario_6/fata_cu.conf",
        output_json_path="/home/aiml/johnson/Scenario/Scenario_6/fata_cu_segments.json"
    )
