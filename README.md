# 🔎 Port Scanner

A lightweight and multithreaded TCP port scanner built with Python for network reconnaissance and security testing in authorized environments.

NEXUSSCAN resolves hostnames to IP addresses, scans a user-defined range of TCP ports, identifies commonly associated services, and presents open-port results in a clean, color-coded terminal interface.


## 🚀 Features

* 🔍 TCP Connect port scanning
* 🌐 Domain/hostname to IP resolution
* ⚡ Multithreaded scanning for faster execution
* 🛠️ Service identification using standard TCP service mappings
* 🎨 Color-coded terminal output
* 📊 Clean tabular scan results
* ⏱️ Scan execution time
* ✅ Displays a clear message when no open ports are found
* 💻 Simple command-line interface

---

## 🧰 Technology Used

* **Python 3**
* `socket` — TCP connections, hostname resolution, and service identification
* `threading` — concurrent port scanning
* `argparse` — command-line argument handling
* ANSI escape sequences — terminal colors
* `time` — scan timing

---

## ⚙️ How It Works

NEXUSSCAN follows a simple scanning workflow:

```text
User provides target
        ↓
Resolve hostname to IP
        ↓
Create TCP socket
        ↓
Attempt connection to each port
        ↓
If connection succeeds
        ↓
Identify standard service
        ↓
Display open port + service
        ↓
Show total scan time
```
---

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/utsavthakur448/Port-Scanner.git
```

Move into the project directory:

```bash
cd Port-Scanner
```

---

## ▶️ Usage

```bash
python3 port_scanner.py -h
```

### Scan a domain

```bash
python3 port_scanner.py -t <ip> -sp 1 -ep 1000
```

### Command format

```bash
python3 port_scanner.py -t TARGET -sp START_PORT -ep END_PORT
```

| Argument               | Description                   |
| ---------------------- | ----------------------------- |
| `-t` / `--target`      | Target IP address or hostname |
| `-sp` / `--start-port` | Starting TCP port             |
| `-ep` / `--end-port`   | Ending TCP port               |

---

## 🧪 Testing Environment

The project can be tested safely against:

* `localhost`
* Your own machine
* A local virtual machine
* Metasploitable
* Other intentionally vulnerable lab environments

For example, when using a private lab network:

```bash
python3 port_scanner.py -t 192.168.56.101 -sp 1 -ep 1000
```
---

## 📌 Output ScreenShot

<img width="1485" height="736" alt="Screenshot_2026-08-16_01_46_55" src="https://github.com/user-attachments/assets/4afdf3f9-6c5a-4790-966a-75ee8e43f4e8" />

<img width="1445" height="662" alt="Screenshot_2026-08-16_01_45_35" src="https://github.com/user-attachments/assets/c635c687-d01b-45dd-b6be-73c6085bb14d" />

---

## 📚 What I Learned

Building NEXUSSCAN helped me strengthen my understanding of:

* TCP/IP networking
* TCP ports and services
* Socket programming in Python
* Hostname and IP resolution
* Multithreading
* Command-line argument parsing
* Network reconnaissance concepts
* Basic service identification
* Error handling
* Performance measurement

---

## 🔮 Future Improvements

Possible future versions may include:

* Service/banner grabbing
* Better port-state classification
* Configurable timeout
* Controlled thread pool
* Common-port scanning profiles
* JSON/CSV reporting
* Web dashboard
* More advanced service fingerprinting

---

## 👨‍💻 Author

**Utsav Thakur**

Cybersecurity Enthusiast | Ethical Hacking | VAPT | Penetration Testing
