# Auto Debug YAML Generator for OAI/O-RAN

This tool leverages LLMs (via NVIDIA OpenAI-compatible API) to automatically generate structured debug entries (`debug.yaml`) based on gNB configuration differences and error logs from OAI or O-RAN systems.

## 📌 Features

- Automatically compare baseline (success) and fail configurations.
- Parse and extract error logs from failed gNB runs.
- Use NVIDIA API call LLM (**llama3-70b**) to analyze issues and propose a structured YAML solution.
- Save the result to timestamped YAML files for future debugging reference.

## 🛠️ Requirements

- Python 3.8+
- `openai`, `difflib`, `re`, `json`, `pathlib`
- NVIDIA API key with OpenAI-compatible interface

## 🚀 Usage

1. Place success and failed config/log pairs into:
```bash
/home/aiml/johnson/auto_gen_debug_yaml/success_data/
/home/aiml/johnson/auto_gen_debug_yaml/fail_data/
```

2. Update your NVIDIA API key in the environment or directly in code.
- [Apply a API key](https://build.nvidia.com/)
3. Run the notebook:
```bash
jupyter notebook auto_gen_debug_yaml.ipynb
```
4. Output will be saved as:
```bash
debug_yaml_dir/debug_YYYYMMDD_HHMMSS.yaml
```

## 📂 Output Format
Each YAML entry contains:
- `stage`:
  - `cu_init`, `du_init`
  - `f1`, `NGAP`
  - `cell search`
  - `random access`
  - `syntax error`
- type: `CU`, `DU`
- symptom: summary of issue
- log_snippet: extracted error messages
- related_config: parameters causing the issue
- notes: explanation and resolution guidance

## 🧠 LLM Prompt Design
The prompt integrates:
- Config diffs (with difflib)
- Error log context
- Template YAML format as reference

```bash
You are an intelligent debugging agent within the 5G OAI/O-RAN architecture. You have access to knowledge about 3GPP specs, O-RAN standards, and OAI gNB initialization logic.

Your task is to analyze failure cases in gNB (CU/DU) configuration. You will be given:
- Configuration file differences between a working and a failed setup
- Corresponding error log snippets from both CU and DU

Please perform the following:
1. Determine what caused the failure
2. Identify which config parameters are related
3. Extract representative log messages that indicate the failure
4. Generate a debug.yaml entry in the following format

Use 5G NR and O-RAN terminology in your explanation. Specify the affected protocol layer (e.g., PHY, MAC, RRC), and explain the root cause. If possible, refer to specific 3GPP specs (e.g., TS 38.331, 38.401) or OAI module behavior (e.g., RCconfig failure, DU startup path).

Use the following input:

[CONFIG DIFFERENCE]
CU:
{cu_conf_diff_text or "No difference detected."}

DU:
{du_conf_diff_text or "No difference detected."}

[ERROR LOG]
CU:
{cu_log_diff_text or "No error log from CU."}

DU:
{du_log_diff_text or "No error log from DU."}

Expected output format:

- stage: <cu_init / du_init / f1 / NGAP / cell search / random access / syntax error>
  type: <CU / DU>
  symptom: "<short explanation of failure>"
  log_snippet:
    - "... error message ..."
  related_config:
    - "<parameter_name>"
  notes: |
    <In-depth technical explanation>
```


| Prompt Component       | Corresponding Content in Debug Prompt                                                                                  |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Role**               | `You are a OAI 5G/O-RAN debugging assistant working on gNB configuration issues.`                                      |
| **Task Description**   | `Analyze what caused the failure... Generate a debug.yaml...`                                                          |
| **Background Context** | `using 5G NR / O-RAN terminology`, `Clarify... using OAI’s initialization logic`; 3GPP SPEC IDs implied but not listed |
| **Expected Behaviour** | `Please output in this format`, `stage/type/symptom...notes`; YAML output format required                              |
