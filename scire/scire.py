# Scire - Information Gathering, Recon, Scanning, and Enumeration

import sys
import time
import argparse

def seconds_to_str(time):
    hours, rem = divmod(int(time), 3600)
    minutes, seconds = divmod(rem, 60)
    return f"{hours}h {minutes}m {seconds}s" if hours else f"{minutes}m {seconds}s"

banner = """\033[91m
 _______ _______ _____  ______ _______
 |______ |         |   |_____/ |______
 ______| |_____  __|__ |    \\_ |______

\033[0m"""

def main():
    try:
        launch_time = time.time()
        print(banner)

        # First pass: minimal parser just to check for --help
        pre_parser = argparse.ArgumentParser(add_help=False)
        pre_parser.add_argument('-h', '--help', action='store_true')
        known_args, _ = pre_parser.parse_known_args()

        # Now define the full parser
        parser = argparse.ArgumentParser(
            description="Scire - Information Gathering, Recon, Scanning, and Enumeration",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            add_help=False
        )

        group = parser.add_mutually_exclusive_group(required=not known_args.help)
        group.add_argument('-t', '--target', help='Set target (comma separated, no spaces, if multiple)')
        group.add_argument('-f', '--file', help='Read targets from file (one domain per line)')

        parser.add_argument('-n', '--with-nmap', action='store_true', help='Perform nmap service/script scan')
        parser.add_argument('-o', '--output', help='Save to filename')
        parser.add_argument('-p', '--ip', action='store_true', help='Output resolved IPs and list of unique IPs')
        parser.add_argument('-r', '--recursive', action='store_true', help='Recursively search over all subdomains')
        parser.add_argument('-v', '--verbose', action='store_true', help='Print debug info and full request output')
        parser.add_argument('-w', '--overwrite-nmap-scan', help='Overwrite default nmap scan (default: -nPn -sV -sC)')
        parser.add_argument('-h', '--help', action='store_true', help='Show this help message and exit')

        args = parser.parse_args()

        if args.help:
            runtime = seconds_to_str(time.time() - launch_time)
            parser.epilog = f"Scire ran for {runtime}. For Knowledge!"
            parser.print_help()
            sys.exit(0)

        if args.verbose:
            print("[DEBUG] Arguments parsed:")
            print(args)

    except KeyboardInterrupt:
        print(f"\nScire ran for {seconds_to_str(time.time() - launch_time)}")
        print("Closing Scire...")
        sys.exit(0)

if __name__ == "__main__":
    main()
