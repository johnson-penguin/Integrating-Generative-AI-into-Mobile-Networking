# Scenario_Latest Workspace

This workspace contains all components for automated debugging, configuration correction, and LLM-based reasoning for 5G O-RAN integration scenarios.

## 📁 Directory Structure

This workspace contains:
- 🔧 `tools/`:
  - Scripts and notebooks for testing and integration
- 📂
  - `Reason/`: RAG model reason and no-RAG model reason
  - `input_data/`: Raw logs and configs
  - `output_data/`: LLM-generated configs or results
  - `debug_cases/`: YAML-formatted debug database
  - `sft_data/`: Datasets for supervised fine-tuning


## 🔧 Main Use Cases

- **Log Analysis**: Extract key error patterns from CU/DU/RU logs.
- **Config Correction**: Detect invalid `.conf` values and auto-fix using debug rules.
- **RAG Integration**: Retrieve relevant knowledge from debug YAML to improve LLM accuracy.
- **Reason Evaluation**: Compare LLM-generated `reason` vs. RAG-LLM-generated `reason`.
- **SFT Benchmarking**: Train and evaluate LLMs using domain-specific config/debug datasets.

## 🧠 Folder Conventions

- All generated or predicted results go into `output/` or `reason_gen/`.
- Human-authored content (labels, configs) should be stored in `reference/` or `reason_gold/`.
- Never edit `debug_cases/debug.yaml` directly without reviewing version control.

## 🚀 Getting Started

1. Place your CU/DU logs into `data/input/`
2. Run the notebook or tools in `tools/` to parse and match errors


---

For detailed documentation, please refer to individual notebooks or modules in `tools/`.
