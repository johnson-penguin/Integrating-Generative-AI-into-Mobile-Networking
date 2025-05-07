# 1. cu_test_params.py / du_test_params.py
Define multiple sets of test parameters with corresponding alternative values. Each parameter contains both original and variant values, which can be used to simulate errors or different scenarios of the setup behavior.
- [OAI_CU : 22 case](https://github.com/johnson-penguin/Integrating-Generative-AI-into-Mobile-Networking/blob/main/Scenario_Gen/cu/cu_test_params.py)
- [OAI_DU : 84 case](https://github.com/johnson-penguin/Integrating-Generative-AI-into-Mobile-Networking/blob/main/Scenario_Gen/du/du_test_params.py)

```bash=
test_params = {
    "Num_Threads_PUSCH": (
        'Num_Threads_PUSCH = 8;',
        'Num_Threads_PUSCH = asdasfsad;'
    ),
    "amf_ip_address": (
        'amf_ip_address = ({ ipv4 = "192.168.8.00" });',
        'amf_ip_address = ({ ipv4 = "1.2.3.4" });'
    ),
.
.
.
    "plmn_list": (
        'plmn_list = ({ mcc = 001; mnc = 01; mnc_length = 2; snssaiList = ( { sst = 1;}); });',
        'plmn_list = ({ mcc = 208; mnc = 93; mnc_length = 2; snssaiList = ( { sst = 1; }); });'
    )    
}
```
✅ Example: amf_ip_address was 192.168.8.00, changed to 1.2.3.4

📄 This file is data structure only, no execution logic.

---

# 2. gen_test_cu_config.py / gen_test_du_config.py
Automatically generates a series of profiles based on the variables defined in [cu_test_params.py](https://github.com/johnson-penguin/Integrating-Generative-AI-into-Mobile-Networking/blob/main/Scenario_Gen/cu/gen_test_cu_config.py) / du_test_params.py:
- 0_cu_gnb_original.conf: Backup of the original configuration file.
- 1_cu_gnb_paramX.conf ~ N_cu_gnb_paramY.conf: Mutated versions of each parameter.

✅ This program will apply each set of original/variant parameters to the original configuration file and save it as a new .conf file.

![image](https://github.com/user-attachments/assets/341e68cb-9749-4982-9572-769f3fd10be1)

---

# 3. test_cu_config_params.py
Run all the above .conf configuration files in order and save the execution log to the specified directory:

- Start the CU with nr-softmodem and terminate after 30 seconds of simulation.
- Each configuration file will produce a corresponding execution log.
- A summary of the execution status (success, timeout, exit code, etc.) is listed at the end.

It is normal for this session to time out because the CU will wait indefinitely for the DU to start.

![image](https://github.com/user-attachments/assets/577f34cd-b134-4a46-bda6-14a50e8f700e)

Based on the status, you can determine which parameters will cause the CU or DU to crash directly during operation.
![image](https://github.com/user-attachments/assets/e4124b12-d6ad-4aed-8896-a0c37a530126)

- [Normal case (timeout)](https://github.com/johnson-penguin/Integrating-Generative-AI-into-Mobile-Networking/blob/main/Scenario_Gen/cu/cu_test_log/0_cu_gnb_original_log.txt)

```bash=
[GTPU]   SA mode 
[GTPU]   Configuring GTPu address : 192.168.8.43, port : 2152
[GTPU]   Initializing UDP for local address 192.168.8.43 with port 2152
[GTPU]   Created gtpu instance id: 94
[F1AP]   Starting F1AP at CU
[NR_RRC]   Entering main loop of NR_RRC message task
[NR_RRC]   Accepting new CU-UP ID 3584 name gNB-Eurecom-CU (assoc_id -1)
[UTIL]   threadCreate() for TASK_GTPV1_U: creating thread with affinity ffffffff, priority 50
[F1AP]   F1AP_CU_SCTP_REQ(create socket) for 127.0.0.5 len 10
[GTPU]   Initializing UDP for local address 127.0.0.5 with port 2152
[GTPU]   Created gtpu instance id: 95
[NGAP]   Received NGSetupResponse from AMF
[GNB_APP]   [gNB 0] Received NGAP_REGISTER_GNB_CNF: associated AMF 1
```

- [Exit case (255)](https://github.com/johnson-penguin/Integrating-Generative-AI-into-Mobile-Networking/blob/main/Scenario_Gen/cu/cu_test_log/3_cu_gnb_ciphering_algorithms_log.txt)

```bash=
[UTIL]   running in SA mode (no --phy-test, --do-ra, --nsa option present)
[OPT]   OPT disabled
[HW]   Version: Branch: develop Abrev. Hash: 054506f5ae Date: Tue Dec 10 13:33:23 2024 +0000
[GNB_APP]   Initialized RAN Context: RC.nb_nr_inst = 1, RC.nb_nr_macrlc_inst = 0, RC.nb_nr_L1_inst = 0, RC.nb_RU = 0, RC.nb_nr_CC[0] = 0
[GNB_APP]   F1AP: gNB_CU_id[0] 3584
[GNB_APP]   F1AP: gNB_CU_name[0] gNB-Eurecom-CU
[GNB_APP]   SDAP layer is disabled
[GNB_APP]   Data Radio Bearer count 1
[NR_RRC]   do_SIB23_NR, size 9
[RRC]   unknown ciphering algorithm "nea4" in section "security" of the configuration file
CMDLINE: "./nr-softmodem" "--rfsim" "--sa" "-O" "/home/oai72/Johnson/tool/scenario_gen/cu/cu_test_conf/4_cu_gnb_ciphering_algorithms.conf" 
[CONFIG] function config_libconfig_init returned 0
```
