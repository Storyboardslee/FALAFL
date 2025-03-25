# FALAFL
FALAFL: FAir muLti-sAmple Feature sELection. Applicable to comparative analysis of multi-patient data.



Welcome to the repository for `FALAFL`[^2], an algorithmic approach based on combinatorial optimization and designed to perform feature selection in sequencing data which ensures a balanced selection of features from all patient samples in a cohort.

![Schema Figure for FALAFL](/assets/falafl_sysarch.png)


# Table of Contents

  1. [Setting up](#start) 
 
  2. [Using `FALAFL`](#manual)
     * [Parameters](#param)
     * [Files](#files) 
       * [Input](#input): content and format of input files to `FALAFL`
       * [Intermediate output](#inter_output): content and format of intermediate output of `FALAFL`
       * [Final output](#final_output): content and format of final output files to `FALAFL`
     * [Example](#example): a guide to perform feature selection on the colorectal cancer patient cohort [^1]
  4. [Contact](#contact)



<a name="start"></a>
# Setting up

Follow instructions to [install `conda`](https://conda.io/projects/conda/en/latest/user-guide/install/).

Follow instructions to [install `Gurobi`](https://support.gurobi.com/hc/en-us/articles/360044290292-How-do-I-install-Gurobi-for-Python-), retrieve a `Gurobi` license (which is [free for academics](https://www.gurobi.com/academia/academic-program-and-licenses/)), and [set up the license](https://www.gurobi.com/documentation/9.5/quickstart_mac/retrieving_and_setting_up_.html) on your computing environment.

Then:

```console
 $ git clone https://github.com/Storyboardslee/FALAFL.git
 $ cd FALAFL
```


<a name="manual"></a>
# Using `FALAFL`

We will describe the parameters, input files, and output files used by `FALAFL`, followed by an example to perform feature selection on the colorectal cancer patient cohort [^1].

<a name="param"></a>
## Parameters

`FALAFL` has one optional and three required parameters. Given a methylation read coverage data represented as a patient-by-site matrix $S_{n\times m}$, where $n$ is the number of patients, $m$ the number of CpG sites, and $s_{i,j}$ the fraction of cells in patient, the parameters $\delta$, $p$, $k$, and $q$ are the following:

 | **Parameter** | **Description** |
 |---------------|----------------|
 |     $\delta$  |  Optional, the minimum coverage threshold for a feature to be included in the analysis. For each patient $i$, we have $s_{i,j} > \delta$ for each site $j$; if not, site $j$ is not considered any further for that patient.|
 |     $p$        | The threshold for binarization of $S$ to obtain $\overline{S}$, where $\overline{s}_{i,j}$ indicates whether site $j$ has sufficient read depth in at least a fraction of $p$ cells in patient $i$. |
 |     $k$        |  The threshold for keeping sites in $\overline{S}$. We eliminate all sites $j$ where the total number of patients $i$ with $s_{i,j} =1$ is $\leq k$. |
  |    $q$        |  The proportion of sites chosen in each patient. `FALAFL` chooses the largest subset of sites $s_j$, so that for each patient $i$, the proportion of $\overline{s}_{i,j}=1$ among the chosen sites is at least $q$.          |



<a name="files"></a>

## Files

Here we will describe the content and format for input and output for `FALAFL`.

<a name="input"></a>
### Input

The input to `FALAFL` is a patient-by-site matrix $S_{n\times m}$, where $n$ is the number of patients, $m$ the number of CpG sites (or any other molecular features the user wish to study), and $s_{i,j}$ the fraction of cells in patient (i.e., tumor sample) $i$ in which CpG site $j$ has "sufficient" read depth (e.g.,two reads or more) as defined by the user. We choose to implement in a way such that the program takes [`.npz` file](https://numpy.org/doc/2.2/reference/generated/numpy.savez.html#numpy.savez) as input, in which the input matrix $S_{n\times m}$ is stored in the field `m` in the file.

<a name="inter_output"></a>
### Intermediate output
The preprocessing step (as excuted in `src/preprocess.py`) of `FALAFL` takes care of filtering for sites satisfying $s_{i,j} > \delta $, binarizing $S$ to obtain $\overline{S}$, where $\overline{s}_{i,j}$ indicates whether site $j$ has sufficient read depth in at least a fraction of $p$ cells in patient $i$, and filtering for sites with good coverage in at least $k$ patients. This intermediate state outputs $\overline{S}_{n,m'}$ (where $m'$ denotes the number of sites not eliminated in the preprocessing steps) as an `.npz` file, in which $\overline{S}_{n,m'}$ is stored in the field `m` in the file.


<a name="final_output"></a>
### Final Output
The final output of `FALAFL` is the indices of the sites selected by ILP (as excuted in `src/falafl.py`). The output is an `.npz` file, in which the indices of the selected sites are stored in the field `cols` in the file.


<a name="example"></a>
## Example

We include an example of running the entire `FALAFL` pipeline (preprocessing and ILP-based feature selection) in `demo.ipynb` using the colorectal cancer data in `demo_data`.



<a name="contact"></a>
# Contact

We are glad you are using `FALAFL` and look forward to hearing your own creative way of applying `FALAFL` on your data! If you have encountered any issues with `FALAFL`, please report on the [issue forum](https://github.com/Storyboardslee/FALAFL/issues) or contact Xuan Cindy Li [[email]](xli1994@umd.edu). 

<!-- References -->

[^1]: Bian, S., Hou, Y., Zhou, X., Li, X., Yong, J., Wang, Y., Wang, W., Yan, J., Hu, B., Guo, H., Wang, J.,
Gao, S., Mao, Y., Dong, J., Zhu, P., Xiu, D., Yan, L., Wen, L., Qiao, J., Tang, F., Fu, W.: Single-cell multiomics sequencing and analyses of human colorectal cancer. Science **362**(6418), 1060-1063 (Nov 2018). [https://doi.org/10.1126/science.aao3791](https://doi.org/10.1126/science.aao3791) 

[^2]: Li, X. C., Liu, Y., Sch\"affer, A. A., Mount, S. M., Sahinalp, S. C.: Fair molecular feature selection unveils universally tumor lineage-informative methylation sites in colorectal cancer. bioRxiv 2024.02.22.580595. [https://doi.org/10.1101/2024.02.22.580595](https://doi.org/10.1101/2024.02.22.580595) (This URL will be updated soon.)


