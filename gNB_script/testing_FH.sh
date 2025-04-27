#!/bin/bash
# Official bash script structure, embedding expect commands for further bash integrations

REMOTE_IP="192.168.8.67"
CAP_SIZE="50"

echo "🔵 Starting telnet to $REMOTE_IP and sending dpdk_cap(0,$CAP_SIZE)..."

expect << EOF
set timeout 30

# 1. Start Telnet connection
spawn telnet $REMOTE_IP

# 2. Wait for the connection to stabilize
sleep 2

# 3. Send Ctrl+Enter to enter Debug mode
send "\r"

# 4. Wait for the Debug prompt
expect {
    "Debug>" {
        # 5. Send dpdk_cap(0,50) command
        send "dpdk_cap(0,$CAP_SIZE)\r"
    }
}

# 6. Wait 5 seconds after sending the command
sleep 5

# 7. Send Ctrl+] to access the Telnet command line
send "\035"

# 8. Wait for the telnet> prompt
expect "telnet>"

# 9. Send quit to close the Telnet session
send "quit\r"

expect eof
EOF

echo "✅ dpdk_cap command sent and Telnet session closed successfully."
