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
✅ 範例：amf_ip_address 原始為 192.168.8.00，變異為 1.2.3.4

📄 此檔案僅為資料結構，無執行邏輯。

2. gen_test_cu_config.py
根據 cu_test_params.py 中定義的變異項目，自動產生一系列設定檔：

0_cu_gnb_original.conf: 原始設定檔的備份

1_cu_gnb_paramX.conf ~ N_cu_gnb_paramY.conf: 每個參數對應的變異版本

✅ 此程式會將每一組原始/變異參數套入原始設定檔中，儲存為新的 .conf 檔

3. test_cu_config_params.py
依序執行上述所有 .conf 設定檔，並將執行 log 儲存至指定目錄：

使用 nr-softmodem 啟動 CU，模擬 30 秒後終止

每個設定檔會產出一份對應的執行 log

於結尾列出執行狀態摘要（成功、timeout、exit code 等）
