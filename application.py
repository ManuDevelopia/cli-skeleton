#!/usr/bin/env python
"""Command Line Interpreter skeleton."""
import click


@click.command()
def main():
    click.echo('Hello World!')

if __name__ == '__main__':
    main()
