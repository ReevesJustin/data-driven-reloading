#!/bin/bash
mkdir -p notebooks/executed
for nb in notebooks/*.ipynb; do
    echo "Running $nb"
    jupyter nbconvert --execute --to notebook "$nb" --output-dir=notebooks/executed --ExecutePreprocessor.timeout=600 2>&1 | tee -a run_log.txt
    echo "Finished $nb"
done