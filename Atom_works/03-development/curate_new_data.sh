#!/bin/bash
# This script curates new data from the NAS sources.

# Example usage:
# ./curate_new_data.sh /mnt/nas2024 /home/caiser77/dgx_workspace/curated_data

curated_dir=$2
source_dir=$1

if [ ! -d "$curated_dir" ]; then
  mkdir -p "$curated_dir"
fi

# Copy new files from source to curated directory
rsync -av --ignore-existing $source_dir/ $curated_dir/

# Log the operation
echo "Data curated from $source_dir to $curated_dir at $(date)" >> /home/caiser77/dgx_workspace/curate_log.txt