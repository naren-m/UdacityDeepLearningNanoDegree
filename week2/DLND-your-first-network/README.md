Creating the work environment


cd into the dlnd-your-first-network folder that you just unzipped.

Create a new conda environment:
```bash
conda create --name dlnd python=3
```

Enter your new environment:
```bash
Mac/Linux: >> source activate dlnd
Windows: >> activate dlnd
```

Ensure you have numpy, matplotlib, pandas, and jupyter notebook installed by doing the following:
```bash
conda install numpy matplotlib pandas jupyter notebook
```

Run the following to open up the notebook:
```bash
jupyter notebook dlnd-your-first-neural-network.ipynb
```

Convert ipython notebook to python script 
```bash
jupyter nbconvert --to python dlnd-your-first-neural-network.ipynb
```