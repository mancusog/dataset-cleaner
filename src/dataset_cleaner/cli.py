import typer
from pathlib import Path
from dataset_cleaner.config import load_config
from dataset_cleaner.reporting import print_info
from dataset_cleaner.cleaning import rename_images, crop_images
from dataset_cleaner.caption import caption_images

app = typer.Typer()
YAML = "config.yaml"

@app.command()
def info(config: Path = Path(YAML)):
    """Show dataset folder metadata."""
    cfg = load_config(config)
    print_info(cfg.dataset_folder)

@app.command()
def rename(config: Path = Path(YAML)):
    """Show if rename is enabled"""
    cfg = load_config(config)
    if cfg.rename.enabled:
        rename_images(cfg.dataset_folder, cfg.rename)
    else:
        typer.echo("Rename is disabled. Set rename.enabled: true in config.yaml")

@app.command()
def crop (config: Path = Path(YAML)):
    """Crop images if crop is enabled"""
    cfg = load_config(config)
    if cfg.crop.enabled:
        crop_images(cfg.dataset_folder, cfg.crop)
    else:
        typer.echo("Crop is disabled. Set crop.enabled: true in config.yaml")

@app.command()
def caption (config: Path = Path(YAML)):
    """Caption images with Ollama"""
    cfg = load_config(config)
    if cfg.caption.enabled:
        caption_images(cfg.dataset_folder, cfg.caption)
    else:
        typer.echo("Caption is disabled, Set caption.enabled: true in config.yaml")

if __name__ == "__main__":
    app()