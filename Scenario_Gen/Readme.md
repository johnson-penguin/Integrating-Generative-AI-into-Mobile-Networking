# 1. cu_test_params.py / du_test_params.py
Define multiple sets of test parameters with corresponding alternative values. Each parameter contains both original and variant values, which can be used to simulate errors or different scenarios of the setup behavior.
- [OAI_CU config file: Total 22 params](https://github.com/johnson-penguin/Integrating-Generative-AI-into-Mobile-Networking/blob/main/Scenario_Gen/cu/cu_test_conf/0_cu_gnb_original.conf)
    - [single param testcase generator](https://github.com/johnson-penguin/Integrating-Generative-AI-into-Mobile-Networking/blob/main/Scenario_Gen/cu/cu_test_params.py)
- [OAI_DU config file: Total 84 params](https://github.com/johnson-penguin/Integrating-Generative-AI-into-Mobile-Networking/blob/main/Scenario_Gen/du/du_test_conf/0_du_gnb_original.conf)
    -  [single param testcase generator](https://github.com/johnson-penguin/Integrating-Generative-AI-into-Mobile-Networking/blob/main/Scenario_Gen/du/du_test_params.py)


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
Automatically Generate Multiple Configuration Profiles Based on cu_test_params.py / du_test_params.py:

- `0_cu_gnb_original.conf`: A direct backup of the original configuration file. (Corresponds to the blue block in Figure 1)
- `1_cu_gnb_paramX.conf ~ N_cu_gnb_paramY.conf`: Mutated configuration files, each containing a modified version of a specific parameter. (Corresponds to the red blocks in Figure 1)

The program systematically applies each set of original and variant parameters to the baseline configuration file, generating a new .conf file for each case. These outputs align with the structure illustrated in Figure 1 below.

- Figure 1
    - ![image](https://github.com/user-attachments/assets/e05c304f-84b7-4f4a-a774-7edce0399846)



---

# 3. test_cu_config_params.py
Run all the above .conf configuration files in order and save the execution log to the specified directory:

- Start the CU with nr-softmodem and terminate after **30 seconds** of simulation.
- Each configuration file will produce a corresponding execution log.

![image](https://github.com/user-attachments/assets/e8d38640-8db1-40d1-b00a-31070ec5269b)

**Based on the execution results, you can identify which parameter modifications cause the CU or DU to crash during runtime.**

A summary of the execution status — including **success**, **timeout**, and **exit codes** — is provided at the end of the test session.

Note: It is expected for some sessions to time out, as the CU may wait indefinitely if the DU fails to start.

![image](https://github.com/user-attachments/assets/ce4345d3-4520-46ea-a2d4-cdb882f647c7)

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
