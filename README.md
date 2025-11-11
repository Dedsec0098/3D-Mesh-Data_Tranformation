# Mesh Data Transformation - Assignment Submission

**Author:** Shrish Mishra  
**Date:** November 10, 2025  
**Assignment:** Mesh Data Transformation and Error Analysis

---

## Project Overview

This project implements mesh data transformation techniques including normalization, quantization, and reconstruction with comprehensive error analysis. The assignment covers three main tasks:

1. **Data Loading & Exploration** - Loading and analyzing 3D mesh files
2. **Normalization & Quantization** - Applying two normalization methods with quantization
3. **Reconstruction & Error Analysis** - Dequantizing, denormalizing, and measuring reconstruction errors

---

## Project Structure

```=

---

## 🛠️ Requirements

### Python Version
- Python 3.8 or higher

### Required Libraries
Install the following libraries before running the notebook:

```bash
pip install trimesh
pip install open3d
pip install numpy
pip install matplotlib
pip install pandas
pip install scipy
```

Or install all at once:
```bash
pip install trimesh open3d numpy matplotlib pandas scipy
```

---

## How to Run this project :

### Step 1: Setup Environment
1. Ensure Python 3.8+ is installed
2. Install all required libraries (see Requirements section)
3. Place all mesh files in the `8samples/` folder

### Step 2: Run the Notebook
1. Open Jupyter Notebook or JupyterLab:
   ```bash
   jupyter notebook
   ```
   or
   ```bash
   jupyter lab
   ```

2. Navigate to and open `Mesh_Data_Transformation.ipynb`

3. Run all cells sequentially:
   - Click "Cell" → "Run All" in the menu, OR
   - Press `Shift + Enter` to run each cell individually

---

## Tasks Breakdown

### **Task 1: Data Loading and Exploration** (20 Marks)
**What it does:**
- Loads 8 mesh files from the `8samples/` folder using Trimesh
- Extracts vertex coordinates (x, y, z) as NumPy arrays
- Computes statistics (min, max, mean, std, range) for each axis
- Creates 2D projections (XY, XZ, YZ planes) for visualization

**Key Outputs:**
- Printed statistics for all meshes
- 2D projection plots showing vertex distribution
- Verification of mesh properties (watertight, bounds, face count)

---

### **Task 2: Normalization and Quantization** (40 Marks)
**What it does:**
- Implements **two normalization methods**:
  1. **Min-Max Normalization**: Scales coordinates to [0, 1] range
  2. **Unit Sphere Normalization**: Centers mesh at origin, scales to unit sphere
- Applies **quantization** with 1024 bins to discretize coordinates
- Processes all 8 meshes with both methods
- Saves processed meshes as .obj files in `processed_meshes/` folder

**Key Outputs:**
- 32 processed mesh files (8 meshes × 4 processing types)
- 3D visualizations comparing original, normalized, and quantized versions
- Comparative analysis of both normalization methods

**Key Functions:**
- `normalize_min_max()` - Min-Max normalization
- `normalize_unit_sphere()` - Unit Sphere normalization
- `quantize_vertices()` - Quantization with configurable bin size

---

### **Task 3: Dequantization, Denormalization & Error Analysis** (40 Marks)
**What it does:**
- Reverses the transformation pipeline:
  - **Dequantize**: Recover normalized coordinates from quantized data
  - **Denormalize**: Recover original scale from normalized coordinates
- Computes error metrics:
  - **MSE (Mean Squared Error)**: Measures squared differences
  - **MAE (Mean Absolute Error)**: Measures absolute differences
- Analyzes errors per axis (X, Y, Z) for each method
- Creates comprehensive visualizations and statistical analysis

**Key Outputs:**
- 3D comparison plots (Original vs Reconstructed)
- Per-axis error bar charts (MSE and MAE)
- Overall error comparison across all meshes
- Error distribution heatmaps
- Summary statistics table
- Detailed written conclusion

**Key Functions:**
- `dequantize_vertices()` - Reverse quantization
- `denormalize_min_max()` - Reverse Min-Max normalization
- `denormalize_unit_sphere()` - Reverse Unit Sphere normalization
- `compute_mse()` - Calculate Mean Squared Error
- `compute_mae()` - Calculate Mean Absolute Error
- `compute_per_axis_error()` - Per-axis error analysis

---

## Key Findings & Observations

### Normalization Method Comparison

#### **Min-Max Normalization**
- **Pros:**
  - Lowest reconstruction error (both MSE and MAE)
  - Preserves exact proportions of original mesh
  - Balanced errors across all three axes
  - Predictable range [0, 1] for all coordinates
  
- **Cons:**
  - Not centered at origin
  - Sensitive to outliers
  - Scales each axis independently (may distort aspect ratio)

- **Best for:** Accurate mesh reconstruction, visualization, storage

#### **Unit Sphere Normalization**
- **Pros:**
  - Centered at origin (0, 0, 0)
  - Rotation and translation invariant
  - Preserves shape without deformation
  - Ideal for machine learning applications
  
- **Cons:**
  - Slightly higher reconstruction error
  - Variable range (typically [-1, 1])
  - May waste resolution on thin/elongated shapes

- **Best for:** Machine learning, neural networks, geometric processing

### Quantization Impact (1024 bins)
- Introduces minimal distortion (errors in range 10^-6 to 10^-3)
- Both methods maintain high fidelity after reconstruction
- Sufficient resolution for most practical applications
- Trade-off between storage efficiency and accuracy

### Error Patterns Observed
1. **Per-Axis Variation**: Errors are NOT uniform across X, Y, Z axes
2. **Geometry Dependency**: Different mesh shapes show different error patterns
3. **Consistent Rankings**: Min-Max consistently outperforms Unit Sphere in reconstruction accuracy
4. **Acceptable Error Levels**: All errors are within acceptable ranges for practical use

### Final Recommendation
- **For Reconstruction Tasks**: Use **Min-Max Normalization** (lowest error)
- **For Machine Learning**: Use **Unit Sphere Normalization** (better geometric properties)
- **Quantization**: 1024 bins provide excellent accuracy-efficiency balance

---

## Visualizations Generated

The notebook generates the following visualizations:

1. **2D Projections** (Task 1)
   - Top view (XY plane)
   - Front view (XZ plane)
   - Side view (YZ plane)

2. **Normalization Comparison** (Task 2)
   - Original vs Normalized vs Quantized (both methods)
   - 3D scatter plots with color-coded vertices

3. **Reconstruction Analysis** (Task 3)
   - Original vs Reconstructed (side-by-side comparison)
   - Per-axis MSE bar charts
   - Per-axis MAE bar charts
   - Overall error comparison (all meshes)
   - Error distribution heatmaps

---

## Output Files

### Processed Meshes (32 files total)
All processed meshes are saved in `.obj` format:

- `processed_meshes/normalized_minmax/` - 8 files
- `processed_meshes/normalized_sphere/` - 8 files
- `processed_meshes/quantized_minmax/` - 8 files
- `processed_meshes/quantized_sphere/` - 8 files

### Visualizations
All plots are generated inline in the Jupyter notebook:
- 2D projections for all meshes
- 3D comparison visualizations
- Error metric plots (bar charts, heatmaps)
- Summary statistics tables

##  Learning Outcomes

After completing this assignment, you will understand:
- 3D mesh data structures and manipulation
- Normalization techniques and their trade-offs
- Quantization and its effects on data fidelity
- Error metrics for evaluating reconstruction quality
- Practical applications in computer graphics and machine learning
- Data visualization techniques for 3D geometries


**End of README**
