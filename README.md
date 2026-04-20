## Description

A command-line tool that reads a messy CSV file, validates and cleans it, and produces a detailed report.
It validates column schemas with Pydantic, handles missing values, detects and optionally removes duplicates and outliers, and generates a textual report.
Supports YAML config files to reuse the same pipeline across different datasets.

## Installation

```bash
pip install dataset-cleaner
```

## Usage

```bash
# Basic cleaning
dataset-cleaner clean dataset.csv --output dataset_clean.csv

# With YAML config
dataset-cleaner clean dataset.csv --config config.yaml --output dataset_clean.csv

# Report only, without modifying the file
dataset-cleaner report dataset.csv
```

## Features

- Column schema validation with Pydantic
- Missing values handling (drop, mean/median, mode)
- Duplicate row detection and removal
- Outlier detection (IQR or z-score)
- Textual report + before/after PNG histogram
- Reusable YAML config