#!/bin/bash

# ===== Meta Parameters =====
BUILD_DIR="/home/oai72/FH_7.2_dev/openairinterface5g/cmake_targets/ran_build/build"
CU_CONF="../../../targets/PROJECTS/GENERIC-NR-5GC/CONF/johnson/cu_gnb_liteon.conf"
DU_CONF="../../../targets/PROJECTS/GENERIC-NR-5GC/CONF/johnson/du_gnb_liteon.conf"
CAP_IFACE="eno8303"
LOG_DIR="/home/oai72/Johnson/auto_tool/log"
SESSION_NAME_CU="oai_cu"
SESSION_NAME_DU="oai_du"


mkdir -p "$LOG_DIR"
cd "$BUILD_DIR" || { echo "❌ 無法進入目錄: $BUILD_DIR"; exit 1; }

# ===== Step 1: Start tcpdump =====
NGAP_PCAP="$LOG_DIR/ngap_$(date +%F_%H%M%S).pcap"
echo "📡 開始擷取 NGAP 封包 (Capturing NGAP packets)"
sudo tcpdump -i "$CAP_IFACE" port 38412 -w "$NGAP_PCAP" &
TCPDUMP_PID=$!
echo "$TCPDUMP_PID" > /tmp/tcpdump_pid

# ===== Step 2: 啟動 tmux session，CU 先跑（不 timeout）=====
CU_LOG="$LOG_DIR/cu_log_$(date +%F_%H%M%S).ansi"
tmux new-session -d -s "$SESSION_NAME_CU" \
  "cd $BUILD_DIR && sudo ./nr-softmodem -O \"$CU_CONF\" --thread-pool 1,3,5,7 2>&1 | tee \"$CU_LOG\""
echo "🧠 CU 已啟動 (CU started), log: $CU_LOG"

# ===== Step 3: 等 20 秒後 DU 才跑 =====
for i in {1..2}; do
  sleep 5
  echo "⏳ 等待中 (Waiting)... [$i/2]"
done

DU_LOG="$LOG_DIR/du_log_$(date +%F_%H%M%S).ansi"
tmux new-session -d -s "$SESSION_NAME_DU" \
  "cd $BUILD_DIR && timeout 20s sudo ./nr-softmodem -O \"$DU_CONF\" --thread-pool 9,11,13,15 2>&1 | tee \"$DU_LOG\""
echo "📶 DU 已啟動 (DU started), log: $DU_LOG"

# ===== Step 4: 等待 DU 執行結束 =====
echo "⏳ 等待 DU 結束..."
for i in {1..5}; do
  sleep 5
  echo "⏳ 等待中 (Waiting)... [$i/5]"
done
# ===== Step 5: 停止 tcpdump =====
echo "🛑 停止封包擷取 (Stopping tcpdump)"
if [ -f /tmp/tcpdump_pid ]; then
  TCPDUMP_PID=$(cat /tmp/tcpdump_pid)
  sudo kill "$TCPDUMP_PID" 2>/dev/null
  sleep 2  # 等待 tcpdump 關閉
  sudo pkill -f "tcpdump -i $CAP_IFACE"
  rm -f /tmp/tcpdump_pid
else
  echo "⚠️ 無法找到 tcpdump_pid 檔案"
fi

# ===== Step 6: 強制終止所有 nr-softmodem 程序（CU / DU） =====
echo "🧨 強制終止所有 nr-softmodem 程序（CU / DU）"
sudo pkill -f nr-softmodem
if pgrep -f nr-softmodem > /dev/null; then
  echo "🧨 偵測到 nr-softmodem 執行中，強制結束..."
  sudo pkill -9 -f nr-softmodem
else
  echo "✅ nr-softmodem 已完全結束，無需處理"
fi

# 關閉 tmux session（若存在）
tmux has-session -t $SESSION_NAME_CU 2>/dev/null && tmux kill-session -t $SESSION_NAME_CU
tmux has-session -t $SESSION_NAME_DU 2>/dev/null && tmux kill-session -t $SESSION_NAME_DU


# ===== Done =====
echo -e "\n✅ 任務完成 (Task completed):"
echo "  - CU 日誌: $CU_LOG"
echo "  - DU 日誌: $DU_LOG"
echo "  - 封包檔: $NGAP_PCAP"
