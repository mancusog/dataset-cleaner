import typer
from pathlib import Path
from dataset_cleaner.config import load_config

app = typer.Typer()

@app.command()
def info(config: Path = Path("config.yaml")):
    """Show dataset folder metadata."""
    cfg = load_config(config)
    typer.echo(f"Dataset folder: {cfg.dataset_folder}")

if __name__ == "__main__":
    app()