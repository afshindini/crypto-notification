"""Main loop for running the service"""
import click
from pathlib import Path
from yaml import load, Loader

from service import run_service

@click.command()
@click.option('-c', '--config', default='./config.yml', type=str)
@click.option("--show_conf", is_flag=True, default=False, help="Show the config file.")
def service_cli(config, show_conf) -> None:
    """Read default config from a file"""
    if Path(config).exists():
        with open(config, 'r') as conf:
            cfg = load(conf.read(), Loader=Loader)
            if show_conf:
                click.echo(cfg)
    else:
        raise Exception("There is no config file.") 
    run_service(cfg)


if __name__=="__main__":
    service_cli()

        