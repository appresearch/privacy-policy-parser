"""CLI for privacy policy parser."""
import argparse
import json
import sys
from .parser import Parser


def main():
    parser = argparse.ArgumentParser(description="Parse privacy policies")
    parser.add_argument("source", help="URL or file path")
    parser.add_argument("--output", "-o", help="Output JSON file")
    
    args = parser.parse_args()
    parser = Parser()
    
    try:
        result = parser.parse(args.source)
        if args.output:
            with open(args.output, "w") as f:
                json.dump(result, f, indent=2)
        else:
            print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)



