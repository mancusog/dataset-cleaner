import typer
from pathlib import Path
from dataset_cleaner.config import load_config
from dataset_cleaner.reporting import print_info

app = typer.Typer()

@app.command()
def info(config: Path = Path("config.yaml")):
    """Show dataset folder metadata."""
    cfg = load_config(config)
    print_info(cfg.dataset_folder)

if __name__ == "__main__":
    app()