#!/bin/bash
# Combined full script: start local tcpdump, start gNB, telnet into RU to run dpdk_cap, and clean up

REMOTE_IP="192.168.8.67"
CAP_SIZE="50"
TCPDUMP_FILE="/home/oai72/Johnson/pcap/test.pcap"
GNB_CONF="/home/oai72/FH_7.2_dev/openairinterface5g/cmake_targets/ran_build/build"
LOG_FILE="/home/oai72/Johnson/log/test.log"

# Step 1: Start local tcpdump
echo "🔵 Starting local tcpdump..."
sudo tcpdump -i eno8303 -w $TCPDUMP_FILE &
TCPDUMP_PID=$!

# Step 2: Start gNB
echo "🔵 Starting gNB..."
cd $GNB_CONF
sudo ./nr-softmodem \
  -O ../../../targets/PROJECTS/GENERIC-NR-5GC/CONF/gnb.sa.band78.273prb.fhi72.2x2-TM500_johnson.conf \
  --sa --reorder-thread-disable 1 --thread-pool 1,3,5,7,9,11,13,15 > $LOG_FILE &
GNB_PID=$!

# Step 3: Wait for gNB to stabilize
echo "⏳ Waiting 5 seconds for gNB initialization..."
sleep 5

# Step 4: Telnet to RU and run dpdk_cap(0,50)
echo "🔵 Telnet into $REMOTE_IP and sending dpdk_cap(0,$CAP_SIZE)..."

expect << EOF
set timeout 30

spawn telnet $REMOTE_IP
sleep 2
send "\r"
expect {
    "Debug>" {
        send "dpdk_cap(0,$CAP_SIZE)\r"
    }
}
sleep 5
send "\035"
expect "telnet>"
send "quit\r"
expect eof
EOF

echo "✅ dpdk_cap command sent and Telnet session closed."

# Step 5: Wait more to capture traffic
echo "⏳ Capturing traffic for 10 seconds..."
sleep 10

# Step 6: Stop gNB and tcpdump
echo "🛑 Stopping gNB and tcpdump..."
sudo kill -2 $GNB_PID
sudo kill -2 $TCPDUMP_PID

# Step 7: Return to home directory
cd
echo "✅ All processes terminated successfully."
