#!/bin/bash

# Define the environment prefix
ENV_PREFIX=".conda"

# Create the Conda environment from environment.yml with the specified prefix
echo "Creating Conda environment from environment.yml..."
conda env create --file environment.yml --prefix $ENV_PREFIX

# Activate the newly created environment
echo "Activating the Conda environment..."
source $(conda info --base)/etc/profile.d/conda.sh
conda activate $ENV_PREFIX

# Copy the pre-commit hook to the .git/hooks directory
echo "Setting up Git hooks..."
cp .github/hooks/pre-commit .git/hooks/pre-commit

# Make sure the pre-commit hook is executable
chmod +x .git/hooks/pre-commit

echo "Setup completed successfully."