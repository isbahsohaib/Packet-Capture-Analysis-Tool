# Packet-Capture-Analysis-Tool
The Network Packet Analyzer is a Python tool that captures and analyzes network traffic, leveraging ICMP packets to compute key metrics and providing insights into network performance, with a structured and well-documented codebase.
## Overview

The Network Packet Analyzer is a Python-based tool designed to analyze network traffic by capturing, filtering, and computing various metrics based on ICMP packets. This tool provides insights into network performance, including key metrics such as echo requests, data exchange, ping round trip time, throughput, and hop count.

## Features

- **Packet Filtering:** The tool allows users to filter packets based on specific criteria, enhancing the ability to focus on relevant network data.

- **Metrics Computation:** Leveraging ICMP packets, the analyzer computes essential metrics, including:
  - Number of echo requests sent/received
  - Total data bytes exchanged
  - Average ping round trip time
  - Throughput
  - Hop count

## Codebase Organization

The codebase is structured for clarity and maintainability, with modular files serving distinct purposes:

1. **filter_packets.py:** Contains functionality for packet filtering, allowing users to customize their analysis based on specific parameters.

2. **packet_parser.py:** Implements packet parsing to extract relevant information from network packets, facilitating subsequent metric computation.

3. **compute_metrics.py:** Houses the computation logic for various network performance metrics using the parsed packet data.

## Usage

To use the Network Packet Analyzer, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the analyzer by executing the main script: `python main.py`.

## Example Usage

```python
from filter_packets import filter_packets
from packet_parser import parse_packets
from compute_metrics import compute_network_metrics

# Example: Filtering packets based on source IP address
filtered_packets = filter_packets(source_ip="192.168.1.1")

# Example: Parsing filtered packets
parsed_data = parse_packets(filtered_packets)

# Example: Computing network metrics
metrics = compute_network_metrics(parsed_data)

print(metrics)
