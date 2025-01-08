# DATAR: A Dataset for Tracking App Releases  

**Submission by Group 7**  
**Course**: 2IMP40 - Empirical Methods in Software Engineering  

This project is centered around the paper [DATAR: A Dataset for Tracking App Releases](https://github.com/ISE-Research/DATAR) [[1]](#1). It aims to preprocess, clean, and analyze the dataset provided by the authors to create visualizations and tables that are integral to the report.  

---

## Project Structure  

### 1. **Code Files**  
- **`utils.py`**: Contains utility functions to read the dataset, which is specified as JSON lists.  
- **`preprocessing.ipynb`**: Processes the raw dataset into a convenient pickle file for further analysis.  
- **`data_cleaning.ipynb`**: Ensures data integrity by aligning app review versions with release metadata, eliminating missing attributes.  
- **`results.ipynb`**: Contains the main analysis code that uses the cleaned data to generate visualizations, tables, and other outputs used in the report.  

---

### 2. **Data**  
The **data** folder is meant to store cleaned and preprocessed data. However, this folder is not published to GitHub due to size and privacy considerations.  

To generate the data locally:  
1. Download the dataset from [Zenodo](https://doi.org/10.5281/zenodo.10320168).  
2. Run the notebooks in the following sequence:
   - `preprocessing.ipynb`
   - `data_cleaning.ipynb`  

---

### 3. **Figures**  
The **Figures** folder contains all the visualizations created in `results.ipynb`.

---

## References
<a id="1">[1]</a> 
Y. Abedini, M. H. Hajihosseini, and A. Heydarnoori. "DATAR: A Dataset for Tracking App Releases", In Proceedings of the 21st IEEE/ACM International Conference on Mining Software Repositories (MSR), Lisbon, Portugal, Apr. 2024.