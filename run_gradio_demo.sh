#!/bin/bash

# Create the conda environment
conda env create -f environment.yml

# Activate the environment
source activate gradio-demo

# Run the Gradio demo
python gradio_demo.py 