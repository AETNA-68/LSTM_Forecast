"""
Script that use the config.yaml to download and extract the information from  online zip-file
"""

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    """
    Dataclass that receives variables with paths
    """
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path