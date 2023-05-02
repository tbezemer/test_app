import click
import logging

logger = logging.getLogger(__name__)


@click.group()
@click.option("-v", "--verbose", is_flag=True)
def main(verbose):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level)


@main.command()
@click.option("-d", "--data_source", type=str)
def run(data_source):
    logger.info(f"Processing '{data_source}'")
