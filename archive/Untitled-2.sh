#!/bin/bash

echo "Installing Advanced Cybersecurity Tools..."

# Defense Tools
DEFENSE_TOOLS=(
    ufw
    fail2ban
    iptables
    snort
    suricata
    clamav
    rkhunter
)

# Offensive Tools (Some may require manual install steps after this)
OFFENSE_TOOLS=(
    burpsuite
    zaproxy
    maltego
    beef-xss
    se-toolkit
    wifite
    recon-ng
)

# Install defense tools
echo "Installing Defense Tools..."
for tool in "${DEFENSE_TOOLS[@]}"; do
    sudo apt install -
