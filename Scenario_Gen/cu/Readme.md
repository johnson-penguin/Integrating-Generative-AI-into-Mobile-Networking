# CU Config Generator
This tool generates multiple mutated versions of a CU .conf file for testing purposes. It randomly modifies 1 to 5 configuration parameters per file, and saves both the .conf and its corresponding metadata .json for debugging.

# Why This Generator?
Manually creating configuration files with different parameter combinations is time-consuming and error-prone.
This generator automates the process by producing a large number of .conf files with randomly mutated parameters based on a predefined rule set.

It is designed to:
- Accelerate testing by generating diverse test cases.
- Simulate real-world misconfigurations and edge cases.
- Help identify which parameters may cause the CU to crash.


# Features
- Generates multiple randomized `.conf` files from a baseline config.
- Randomly mutates a number of parameters per file, controlled by the `num_params_range` setting in the script.
- Records mutation details in separate `.json` files.
- Creates a `summary.json` to track all generated configs and their mutated fields.

# Directory Structure
After running the script, the following structure will be created:

```bash= 
scenario_gen/cu/
├── cu_test_conf/      # Contains generated .conf files
│   ├── 0_cu_gnb_original.conf
│   ├── 1_cu_gnb_random.conf
│   └── ...
├── cu_test_json/      # Contains .json metadata for each config
│   ├── 1_cu_gnb_random.json
│   ├── 2_cu_gnb_random.json
│   └── summary.json   # Lists all generated configs and mutated fields
```

# How to Run
You can also modify the parameter mutation range directly in the script:
```bash=
num_configs = 3  # Number of config files to generate
num_params_range = (1, 5)  # Number of parameters to mutate per config
```

# Example 

## Entry in conf
```bash=

# Active_gNBs = ( "gNB-Eurecom-CU");

Active_gNBs = ( "gNB-Eurecom-CU");

# Asn1_verbosity, choice in: none, info, annoying
Asn1_verbosity = "none";
Num_Threads_PUSCH = 8;

gNBs =
(
 {
    ////////// Identification parameters:
    gNB_ID = 0xZZZZ;                 # <--------------------- For example, this parameter was modified in this random case.

#     cell_type =  "CELL_MACRO_GNB";

    gNB_name  =  "gNB-Eurecom-CU";

    // Tracking area code, 0x0000 and 0xfffe are reserved values
    tracking_area_code  =  1;
    plmn_list = ({ mcc = 001; mnc = 01; mnc_length = 2; snssaiList = ( { sst = 1;}); });

    nr_cellid = 1;
.
.
.
.
```
## Entry in n_cu_gnb_random.json
```bash=
{
  "gNB_ID": {
    "original": "gNB_ID = 0xe00;",
    "variant": "gNB_ID = 0xZZZZ;"
  }
}
```

## Entry in summary.json
```bash=
{
  "1_cu_gnb_random.conf": {
    "json": "1_cu_gnb_random.json",
    "mutated_params": [
      "gNB_ID"
    ]
  },
  "2_cu_gnb_random.conf": {
    "json": "2_cu_gnb_random.json",
    "mutated_params": [
      "plmn_list",
      "local_s_if_name"
    ]
.
.
.
.
.
```
