"""Command line tool to compare two words phonetically"""
import argparse
from .__init__ import phonetic_distance, __version__

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="Calculate phonetic distance between two words.")
    parser.add_argument("word1", help="First word")
    parser.add_argument("word2", help="Second word")
    parser.add_argument("-l", "--language", default="en",
                        help="Language for phonetic comparison (default returns lowest score for "+
                        "all supported languages)")
    parser.add_argument("-v", "--version", action="version", version=f'%(prog)s {__version__}',
                        help="Print the version")
    args = parser.parse_args()

    if hasattr(args, 'version') and args.version:
        print(f"%(prog)s {__version__}")
    elif args.word1 and args.word2:
        distance = phonetic_distance(args.word1, args.word2, args.language)
        print(distance)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
