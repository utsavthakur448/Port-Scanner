# Port Scanner in Python 🔎

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

The scanner uses TCP `connect_ex()` to determine whether a connection can be established to a specific port.

---

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/NEXUSSCAN.git
```

Move into the project directory:

```bash
cd NEXUSSCAN
```

Check that Python 3 is installed:

```bash
python3 --version
```

---

## ▶️ Usage

### Scan a port range

```bash
python3 scan.py -t 127.0.0.1 -sp 1 -ep 100
```

### Scan a domain

```bash
python3 scan.py -t example.com -sp 1 -ep 1000
```

### Command format

```bash
python3 scan.py -t TARGET -sp START_PORT -ep END_PORT
```

| Argument               | Description                   |
| ---------------------- | ----------------------------- |
| `-t` / `--target`      | Target IP address or hostname |
| `-sp` / `--start-port` | Starting TCP port             |
| `-ep` / `--end-port`   | Ending TCP port               |

---

## 📌 Example Output

```text
Starting scan on host: 192.168.56.101

PORT    STATE        SERVICE
-----------------------------------------------------
22      open         SSH
80      open         HTTP
443     open         HTTPS

Time taken: 1.42 seconds
```

When no open ports are found:

```text
Starting scan on host: 192.168.56.101

PORT    STATE        SERVICE
-----------------------------------------------------

No open ports found.

Time taken: 5.39 seconds
```

---

## 🔍 Service Detection

When an open port is discovered, NEXUSSCAN attempts to identify the standard service associated with that TCP port.

For example:

```text
22    → SSH
80    → HTTP
443   → HTTPS
3306  → MYSQL
3389  → RDP
```

For ports without a known standard service mapping, the scanner reports:

```text
UNKNOWN
```

This feature identifies the service associated with the **standard port number**; it does not perform deep software or version fingerprinting.

---

## ⚡ Multithreading

NEXUSSCAN uses Python's `threading` module to scan multiple ports concurrently rather than scanning every port sequentially.

This makes the scanner significantly more practical when scanning a larger port range.

The scanner also waits for all scanning threads to complete before displaying the final scan time.

---

## 🎨 Terminal Output

The terminal output uses ANSI color codes to make important information easier to identify:

* 🟢 **Green** — Open ports
* 🔵 **Cyan** — Scanner information and headings

Example:

```text
[OPEN] 22    SSH
[OPEN] 80    HTTP
[OPEN] 443   HTTPS
```

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
python3 scan.py -t 192.168.56.101 -sp 1 -ep 1000
```

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

---

## ⚠️ Legal & Ethical Notice

NEXUSSCAN should only be used against systems that you own or have explicit authorization to test.

Unauthorized port scanning can violate organizational policies, terms of service, or applicable laws. The author is not responsible for misuse of this tool.

---

## ⭐ Support

If you find this project useful for learning about network security and Python socket programming, consider giving the repository a ⭐ on GitHub.
