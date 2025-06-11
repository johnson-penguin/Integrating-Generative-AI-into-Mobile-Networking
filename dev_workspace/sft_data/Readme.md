## Summary: What is this used for?
This JSON object serves as a training or evaluation sample for fine-tuning or benchmarking a language model to correct telecom configuration files. It includes:

# SFT Training Data Field Explanation

| **Field**          | **Purpose**                                                                 |
|--------------------|------------------------------------------------------------------------------|
| `label`            | Target parameter being fixed                                                 |
| `before` / `after` | The configuration value before and after correction                         |
| `model_reason`     | Why the LLM thinks the change is necessary                                   |
| `reference_reason` | Why this value is valid based on known reference_reason                      |
| `config_type`      | Specifies whether the parameter is CU / DU / RU                              |
| `source_file`      | Tracks where the sample came from                                            |







## `label`
```bash= 
"label": "Active_gNBs"
```
- The **name of the configuration parameter** being corrected.
- In this case, it's the `Active_gNBs` field in a CU configuration file.


## `before`
```bash=
"before": "Active_gNBs = ( \"\" );"
```
- The **original (incorrect or suboptimal)** value from the configuration file.
- An empty list means no gNB is activated, which would cause RAN initialization to fail.

## `after`
```bash=
"after": "Active_gNBs = ( \"gNB-Eurecom-CU\" );"
```

- The **corrected value** proposed by the model.
- This activates the gNB named `"gNB-Eurecom-CU"` and enables proper initialization.

## `model_reason`
```bash=
"model_reason": "Ensures a match between Active_gNBs and gNB_name to prevent invalid RAN context and PLMN mismatch, resolving the 'did not match with PLMNs in RRC' issue."
```
- The reasoning provided by the model for making the change.
- Explains the fix addresses a mismatch between the activated gNBs and the defined `gNB_name`, which otherwise causes RAN context or PLMN validation issues.

## `reference_reason`
```bash=
"reference_reason": "Matches the gNB_name defined in the gNBs section"
```
- The `justification based on reference_config.txt` (e.g., another section in the config file or external MAC/IP mapping).
- Confirms that the proposed value is consistent with what’s defined elsewhere in the configuration.

## `config_type`
```bash
"config_type": "CU"
```
- Indicates the **type of configuration** the change applies to:
  - "CU" for Central Unit
  - "DU" for Distributed Unit
  - "RU" for Radio Unit


## `source_file`
```bash=
"source_file": "13_cu_gnb_Active_gNBs.conf"
```
- The **name of the configuration file** where this parameter was located.
- Useful for traceability and auditing which test case produced the sample.
