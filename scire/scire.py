# Scire - Information Gathering, Recon, Scanning, and Enumeration

import sys
import time
import argparse

help_menu = """
Usage:
  scire (-t TARGET | -f FILE) [-o FILENAME] [-w SCAN]
  scire -h

Options:
  -h --help                       show this help message
  -t --target                     set target (comma separated, no spaces, if multiple)
  -f --file                       set target (reads from file, one domain per line)
  -n --with-nmap                  perform an nmap service/script scan
  -o --output                     save to filename
  -p --ip                         outputs the resolved IPs for each subdomain, and a full list of unique ips
  -r --recursive                  recursively search over all subdomains
  -w --overwrite-nmap-scan SCAN  overwrite default nmap scan (default -nPn -sV -sC)
  -v --verbose                    print debug info and full request output
"""

def seconds_to_str(time):
    hours, rem = divmod(int(time), 3600)
    minutes, seconds = divmod(rem, 60)
    return f"{hours}h {minutes}m {seconds}s" if hours else f"{minutes}m {seconds}s"

banner = """\033[91m
 _______ _______ _____  ______ _______
 |______ |         |   |_____/ |______
 ______| |_____  __|__ |    \\_ |______

\033[0m"""

def parse_args():
    parser = argparse.ArgumentParser(
        description="Scire - Information Gathering, Recon, Scanning, and Enumeration",
        epilog="Happy hunting!",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-t', '--target', help='Set target (comma separated, no spaces, if multiple)')
    group.add_argument('-f', '--file', help='Read targets from file (one domain per line)')

    parser.add_argument('-n', '--with-nmap', action='store_true', help='Perform nmap service/script scan')
    parser.add_argument('-o', '--output', help='Save to filename')
    parser.add_argument('-p', '--ip', action='store_true', help='Output resolved IPs and list of unique IPs')
    parser.add_argument('-r', '--recursive', action='store_true', help='Recursively search over all subdomains')
    parser.add_argument('-w', '--overwrite-nmap-scan', help='Overwrite default nmap scan (default: -nPn -sV -sC)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Print debug info and full request output')

    return parser.parse_args()

def main():
    try:
        launch_time = time.time()
        print(banner)

        args = parse_args()
        
        if args.verbose:
            print("[DEBUG] Arguments parsed:")
            print(args)

    except KeyboardInterrupt:
        print(f"\nScire ran for {seconds_to_str(time.time() - launch_time)}")
        print("Closing Scire...")
        sys.exit(0)

if __name__ == "__main__":
    main()
