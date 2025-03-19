#!/bin/bash -l
#SBATCH --chdir /scratch/izar/chansel/SFT
#SBATCH --ntasks 1
#SBATCH --cpus-per-task 1
#SBATCH --mem 64G
#SBATCH --time 12:00:00
#SBATCH --gres gpu:1
#SBATCH --account cs-552
#SBATCH --qos cs-552
source /scratch/izar/chansel/venvs/morenectarlesspoison/bin/activate
python ./SFT.py