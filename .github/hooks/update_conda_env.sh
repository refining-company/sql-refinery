#!/bin/bash
# .github/hooks/update_conda_env.sh

# Export the current conda environment, remove 'name:' and 'prefix:' lines, and save to environment.yml
conda env export --from-history --prefix ./.conda | awk '!/^name: / && !/^prefix: /' > environment.yml

# Add the updated environment.yml to the commit
git add environment.yml