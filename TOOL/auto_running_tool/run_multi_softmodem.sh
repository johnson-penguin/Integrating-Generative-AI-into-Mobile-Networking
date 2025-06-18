#!/bin/bash
set -euo pipefail

# ===== 參數設定 | Parameter Settings =====
BUILD_DIR="/home/oai72/FH_7.2_dev/openairinterface5g/cmake_targets/ran_build/build"
CU_CONF_DIR="../../../targets/PROJECTS/GENERIC-NR-5GC/CONF/johnson/conf/cu_confs"
DU_CONF_DIR="../../../targets/PROJECTS/GENERIC-NR-5GC/CONF/johnson/conf/du_confs"
CAP_IFACE="eno8303"
LOG_DIR="/home/oai72/Johnson/auto_tool/log"
mkdir -p "$LOG_DIR"
cd "$BUILD_DIR" || { echo "❌ 無法進入目錄: $BUILD_DIR | Cannot enter directory: $BUILD_DIR"; exit 1; }

# ===== 掃描資料夾 | Scan Configuration Folders =====
mapfile -t CU_CONFS < <(find "$CU_CONF_DIR" -type f -name "*.conf" | sort)
mapfile -t DU_CONFS < <(find "$DU_CONF_DIR" -type f -name "*.conf" | sort)

# ===== 檢查配對數量一致 | Check if CU/DU Config Counts Match =====
if [ ${#CU_CONFS[@]} -ne ${#DU_CONFS[@]} ]; then
  echo "❌ CU / DU conf 數量不一致，請確認一一對應 | CU / DU config count mismatch, please ensure one-to-one mapping"
  echo "CU_CONFS: ${#CU_CONFS[@]} 個, DU_CONFS: ${#DU_CONFS[@]} 個"
  echo "CU_CONFS: ${#CU_CONFS[@]}, DU_CONFS: ${#DU_CONFS[@]}"
  exit 1
fi

# ===== 開始逐組測試 | Start Testing Each CU/DU Pair =====
for i in "${!CU_CONFS[@]}"; do
  CU_CONF="${CU_CONFS[$i]}"
  DU_CONF="${DU_CONFS[$i]}"
  SESSION_NAME_CU="oai_cu_$i"
  SESSION_NAME_DU="oai_du_$i"
  TIMESTAMP=$(date +%F_%H%M%S)

  echo -e "\n=========================="
  echo "🚀 開始第 $((i + 1)) 組測試"
  echo "Starting Test Set $((i + 1))"
  echo "CU_CONF: $CU_CONF"
  echo "DU_CONF: $DU_CONF"
  echo "=========================="

  # Step 1: 開始封包擷取 | Start Packet Capture
  NGAP_PCAP="$LOG_DIR/${i}_ngap.pcap"
  sudo tcpdump -i "$CAP_IFACE" port 38412 -w "$NGAP_PCAP" &
  TCPDUMP_PID=$!
  echo "$TCPDUMP_PID" > /tmp/tcpdump_pid

  # Step 2: 啟動 CU | Launch CU
  CU_LOG="$LOG_DIR/${i}_cu.log"
  tmux new-session -d -s "$SESSION_NAME_CU" \
    "cd $BUILD_DIR && sudo ./nr-softmodem -O \"$CU_CONF\" --thread-pool 1,3,5,7 2>&1 | tee \"$CU_LOG\""
  echo "🧠 CU 啟動中，log: $CU_LOG"
  echo "🧠 CU is launching, log: $CU_LOG"

  # Step 3: 等待後啟動 DU | Wait and Then Launch DU
  for x in {1..2}; do
    sleep 5
    echo "⏳ 等待中 (Waiting)... [$x/2]"
  done
  DU_LOG="$LOG_DIR/${i}_du.log"
  tmux new-session -d -s "$SESSION_NAME_DU" \
    "cd $BUILD_DIR && timeout 20s sudo ./nr-softmodem -O \"$DU_CONF\" --thread-pool 9,11,13,15 2>&1 | tee \"$DU_LOG\""
  echo "📶 DU 啟動中，log: $DU_LOG"
  echo "📶 DU is launching, log: $DU_LOG"

  # Step 4: 等待接收並停止封包擷取 | Wait and Stop Packet Capture
  for x in {1..5}; do
    sleep 5
    echo "⏳ 等待中 (Waiting)... [$x/5]"
  done
  echo "🛑 停止封包擷取... | Stopping Packet Capture..."
  if [ -f /tmp/tcpdump_pid ]; then
    TCPDUMP_PID=$(cat /tmp/tcpdump_pid)
    sudo kill "$TCPDUMP_PID" 2>/dev/null
    sleep 2
    sudo pkill -f "tcpdump -i $CAP_IFACE"
    rm -f /tmp/tcpdump_pid
  fi

  # Step 5: 結束 nr-softmodem | Terminate nr-softmodem Processes
  echo "🧨 終止所有 nr-softmodem... "
  echo "🧨 Terminating all nr-softmodem processes..."
  sudo pkill -f nr-softmodem || true
  sleep 2
  sudo pkill -9 -f nr-softmodem || true

  tmux has-session -t "$SESSION_NAME_CU" 2>/dev/null && tmux kill-session -t "$SESSION_NAME_CU"
  tmux has-session -t "$SESSION_NAME_DU" 2>/dev/null && tmux kill-session -t "$SESSION_NAME_DU"

  echo "✅ 組 $((i + 1)) 測試完成！"
  echo "Test Set $((i + 1)) Completed!"
  echo "CU log: $CU_LOG"
  echo "DU log: $DU_LOG"
  echo "PCAP:   $NGAP_PCAP"

  # Step 6: 檢查是否有錯誤字元標記（紅字） | Check for red text escape code in CU/DU logs
  RED_ANSI_MARKER=$'\033[0m\033[1;31m'

  if grep -a -q "$RED_ANSI_MARKER" "$CU_LOG" || grep -a -q "$RED_ANSI_MARKER" "$DU_LOG"; then
    echo "⚠️ 偵測到紅色 ANSI 錯誤碼，標記此組為異常 | ANSI red marker detected, marking as failed"
    echo "FAILED_SET_$i: CU=$CU_CONF, DU=$DU_CONF" >> "$LOG_DIR/error_cases.txt"

    # （可選）備份 log 到 error_logs
    mkdir -p "$LOG_DIR/error_logs"
    cp "$CU_LOG" "$LOG_DIR/error_logs/${i}_cu_error.log"
    cp "$DU_LOG" "$LOG_DIR/error_logs/${i}_du_error.log"
  fi


  echo "⏳ 緩衝等待 5 秒..."
  echo "Cooldown for 5 seconds..."
  for x in {1..5}; do
    sleep 1
    echo "⏳ 緩衝等待中 (Buffering)... [$x/5]"
  done
done

echo -e "\n🎉 所有測試完成！"
echo -e "\n🎉 All Tests Completed!"


if [ -f "$LOG_DIR/error_cases.txt" ]; then
  echo -e "\n🚨 以下組別包含紅字錯誤，請檢查 error_cases.txt"
  cat "$LOG_DIR/error_cases.txt"
else
  echo -e "\n✅ 所有組別未偵測到紅字錯誤"
fi