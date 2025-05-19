import re
import json

def extract_config_blocks(config_text):
    block_patterns = [
        r"(?P<key>\w+)\s*=\s*\(\s*\{.*?\}\s*\);",     # key = ( { ... } );
        r"(?P<key>\w+)\s*=\s*\{.*?\};",                   # key = { ... };
        r"(?P<key>\w+)\s*:\s*\{.*?\};",                   # key : { ... };
        r"(?P<key>\w+)\s*=\s*\(.*?\);",                   # key = ( ... );
        r"(?P<key>\w+)\s*=\s*\".*?\";",                 # key = "value";
        r"(?P<key>\w+)\s*=\s*\d+;"                         # key = 123;
    ]

    segments = []
    for pattern in block_patterns:
        for match in re.finditer(pattern, config_text, re.DOTALL):
            key = match.group("key")
            content = match.group().strip()
            segments.append({ "label": key, "content": content })

    return [dict(t) for t in {tuple(d.items()) for d in segments}]

# 載入設定檔
config_path = "/home/aiml/johnson/Scenario/Scenario_5/DU/conf/Scenario_5.conf"
with open(config_path, "r", encoding="utf-8") as f:
    config_text = f.read()

segments = extract_config_blocks(config_text)

# 儲存成 JSON
with open(config_path + ".segments.json", "w", encoding="utf-8") as f:
    json.dump(segments, f, indent=2, ensure_ascii=False)

print(f"✅ 已儲存分段結果：{config_path}.segments.json，共 {len(segments)} 段")
