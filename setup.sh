#!/bin/bash

# Init submodules
git submodule init
git submodule update

# Create the Conda environment from environment.yml with the specified prefix
ENV_PREFIX="./.conda"
echo "Creating Conda environment from environment.yml..."
conda env create --file environment.yml --prefix $ENV_PREFIX

echo "Activating the Conda environment..."
source $(conda info --base)/etc/profile.d/conda.sh
conda activate $ENV_PREFIX

# Copy the pre-commit hook to the .git/hooks directory
echo "Setting up Git hooks..."
cp -f .github/hooks/pre-commit .git/hooks/pre-commit
cp -f .github/hooks/post-checkout .git/hooks/post-checkout

chmod +x .git/hooks/pre-commit
chmod +x .git/hooks/post-checkout
chmod +x .github/hooks/*

echo "Setup completed successfully."