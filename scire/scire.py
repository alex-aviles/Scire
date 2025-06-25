# Scire - Information Gathering, Recon, Scanning, and Enumeration

import sys
import time
import argparse
import chardet



def parse_file(filename):
    targets = []
    try:
        with open(filename, 'rb') as f:
            raw = f.read()
            result = chardet.detect(raw)
            encoding = result['encoding']
            print(f"Detected encoding: {encoding} for file: {filename}")
            lines = raw.decode(encoding).splitlines()
            targets = [line.strip() for line in lines if line.strip()]
    except Exception as e:
        print(f"[!] Error: {e}")
    return targets

def seconds_to_str(time):
    hours, rem = divmod(int(time), 3600)
    minutes, seconds = divmod(rem, 60)
    return f"{hours}h {minutes}m {seconds}s" if hours else f"{minutes}m {seconds}s"

def runtime(launch_time):
    return seconds_to_str(time.time() - launch_time)

def print_epilog(launch_time):
    print(f"\nScire ran for {runtime(launch_time)}. For Knowledge!")

banner = """\033[91m
 _______ _______ _____  ______ _______
 |______ |         |   |_____/ |______
 ______| |_____  __|__ |    \\_ |______

\033[0m"""

def main():
    try:
        launch_time = time.time()
        print(banner)
        time.sleep(0.2)
        # Minimal parser just to check for -h or --help
        pre_parser = argparse.ArgumentParser(add_help=False)
        pre_parser.add_argument('-h', '--help', action='store_true')
        known_args, _ = pre_parser.parse_known_args()

        # Defining the full parser
        parser = argparse.ArgumentParser(
            description="Scire - Scanning, Information Gathering, Recon, and Enumeration",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            add_help=False,
            epilog=None
        )

        group = parser.add_mutually_exclusive_group(required=not known_args.help)
        group.add_argument('-t', '--target', help='Assign target(s) - (comma separated, no spaces, if multiple)')
        group.add_argument('-f', '--file', help='Read list of targets from file - (one target ip address per line)')

        parser.add_argument('-n', '--nmap_portscan', action='store_true', help='Run nmap service or script scan')
        parser.add_argument('-o', '--output', help='Save to provided filename')
        parser.add_argument('-r', '--recursive', action='store_true', help='Recursively search over all subdomains')
        parser.add_argument('-v', '--verbose', action='store_true', help='Print debug info and full request output')
        parser.add_argument('-w', '--overwrite-nmap-scan', help='Overwrite default nmap scan (default: nmap -nPn -sV -sC target(s))')
        parser.add_argument('-h', '--help', action='store_true', help='Show this help message and exit')

        args = parser.parse_args()

        if args.target:
            print(args.target)
            #print_epilog(launch_time)
            #sys.exit(0)

        if args.file:
            targets = parse_file(args.file)
            print(targets)
            print_epilog(launch_time)
            sys.exit(0)

        if args.nmap_portscan:
            time.sleep(10)
            print_epilog(launch_time)
            sys.exit(0)

        if args.help:
            parser.print_help()
            print_epilog(launch_time)
            sys.exit(0)

    except KeyboardInterrupt:
        print("Scire execution cancelled.")
        print_epilog(launch_time)
        print("Closing Scire...")
        sys.exit(0)

if __name__ == "__main__":
    main()
