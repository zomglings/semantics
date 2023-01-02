import argparse

from .oai import generate_cli as generate_openai_cli


def main() -> None:
    parser = argparse.ArgumentParser(description="Tools to extract semantics from data")
    parser.set_defaults(func=lambda _: parser.print_help())

    subparsers = parser.add_subparsers()

    openai_parser = generate_openai_cli()
    subparsers.add_parser("openai", parents=[openai_parser], add_help=False)

    args = parser.parse_args()
    args.func(args)
