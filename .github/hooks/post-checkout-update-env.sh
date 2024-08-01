#!/bin/bash
# .github/hooks/update_conda_env.sh

# Update Conda environment if environment.yml exists
if [ -f environment.yml ]; then
    conda env update --file environment.yml --prefix ./.conda --prune
fi