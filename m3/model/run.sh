#!/bin/bash -l
#SBATCH --chdir /scratch/izar/chansel/project-m3-2024-morenectarlesspoison/model
#SBATCH --ntasks 1
#SBATCH --cpus-per-task 1
#SBATCH --mem 70G
#SBATCH --time 6:00:00
#SBATCH --gres gpu:1
#SBATCH --account cs-552
#SBATCH --qos cs-552
#SBATCH --reservation cs-552
python evaluator.py
date