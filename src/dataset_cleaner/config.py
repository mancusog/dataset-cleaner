from pathlib import Path
import yaml
from pydantic import BaseModel

class CropConfig(BaseModel):
    enabled: bool = False
    aspect_ratio: str = "16:9"
    method: str = "center"

class RenameConfig(BaseModel):
    enabled: bool = False
    criteria: str = "progressive"
    prefix: str = ""

class CaptionConfig(BaseModel):
    enabled: bool = False
    model: str = "gemma4:e4b"
    system_prompt: str = "Describe this image in precise detail for use as a training caption in an image generation model"

class Config(BaseModel):
    dataset_folder: Path
    crop: CropConfig = CropConfig()
    rename: RenameConfig = RenameConfig()
    caption: CaptionConfig = CaptionConfig()

def load_config(path: Path = Path("config.yaml")) -> Config:
    with open(path) as f:
        data = yaml.safe_load(f)
        return Config(**data)