## Description

A command-line tool to prepare image datasets for generative AI model training. Supports batch renaming, aspect ratio cropping, and automatic captioning via Ollama. Configured via YAML.

## Installation

```bash
pip install dataset-cleaner
```

## Usage

```bash
# Show dataset info
dataset-cleaner info

# Rename images progressively
dataset-cleaner rename

# Crop images to target aspect ratio
dataset-cleaner crop

# Caption images with Ollama
dataset-cleaner caption
```

## Features

- Dataset inspection (resolution, file size, caption status)
- Progressive batch renaming
- Aspect ratio cropping (center crop)
- Automatic captioning via Ollama (local LLM)
- Reusable YAML config
