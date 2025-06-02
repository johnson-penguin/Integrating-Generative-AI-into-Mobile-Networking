# Project Description
This script extracts and classifies ANSI-colored log lines from OAI gNB logs into separate files based on their status levels (ERROR, WARNING, INFO, SUCCESS).

# Directory Structure
```bash=
project/
├── extract_log_by_status.py
├── sample_input/
│   └── cu_gnb_with_ansi.log
└── sample_output/
    ├── log_ERROR.txt
    ├── log_WARNING.txt
    ├── log_INFO.txt
    └── log_SUCCESS.txt
```

# How it work?

| Color  | ANSI Code                  | Status  |
| ------ | -------------------------- | ------- |
| Red    | `\x1b\[31m`, `\x1b\[1;31m` | ERROR   |
| Yellow | `\x1b\[33m`, `\x1b\[93m`   | WARNING |
| Blue   | `\x1b\[34m`                | INFO    |
| Green  | `\x1b\[32m`                | SUCCESS |

# Input / Output Mapping

| Type   | Path / Filename                                              | Description                                 |
| ------ | ------------------------------------------------------------ | ------------------------------------------- |
| Input  | `/home/oai72/Johnson/tool/sample_input/cu_gnb_with_ansi.log` | Raw gNB log with ANSI color codes           |
| Script | `/home/oai72/Johnson/tool/extract_log_by_status.py`          | Python script for classifying logs by color |
| Output | `/home/oai72/Johnson/tool/sample_output/log_ERROR.txt`       | Contains all lines classified as `ERROR`    |
| Output | `/home/oai72/Johnson/tool/sample_output/log_WARNING.txt`     | Contains all lines classified as `WARNING`  |
| Output | `/home/oai72/Johnson/tool/sample_output/log_INFO.txt`        | Contains all lines classified as `INFO`     |
| Output | `/home/oai72/Johnson/tool/sample_output/log_SUCCESS.txt`     | Contains all lines classified as `SUCCESS`  |

# How to Capture ANSI-colored Logs ?

To ensure that the log file contains ANSI color codes (used for classification),
**please use the `script` command** when launching the gNB:

```bash=
sudo script -c "./nr-softmodem -O ../../../targets/PROJECTS/GENERIC-NR-5GC/CONF/cu_gnb.conf --thread-pool 1,3,5,7" /home/oai72/Johnson/log/cu_gnb_with_ansi.log
```

# Flow chart
![論文-gNB_LOG_check drawio](https://github.com/user-attachments/assets/f648bc20-3a83-463b-9766-5e792dffc4c7)
