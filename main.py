#!/usr/bin/env python3
# coding: utf-8
import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type=str)
    args = parser.parse_args()

    print(f'hello {args.name}!')


if __name__ == '__main__':
    main()
