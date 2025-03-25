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
       * [Ouput](#output): content and format of output files to `FALAFL`
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

`FALAFL` has one optional and three required parameters. They are:
$\delta$, $p$, $k$, and $q$.

  **Parameter** | **Description**
 ---------------|----------------
      $\delta$  |  TBA
      $p$        | TBA
      $k$        | TBA
      $q$        | TBA



<a name="files"></a>

## Files

Here we will describe the content and format for input and output for `FALAFL`.

<a name="input"></a>
### Input

TBA


<a name="output"></a>
### Output
TBA
<a name="example"></a>
## Example
TBA


<a name="contact"></a>
# Contact

We are glad you are using `FALAFL` and look forward to hearing your own creative way of applying `FALAFL` on your data! If you have encountered any issues with `FALAFL`, please report on the [issue forum](https://github.com/Storyboardslee/FALAFL/issues) or contact Xuan Cindy Li [[email]](xli1994@umd.edu). 

<!-- References -->

[^1]: Bian, S., Hou, Y., Zhou, X., Li, X., Yong, J., Wang, Y., Wang, W., Yan, J., Hu, B., Guo, H., Wang, J.,
Gao, S., Mao, Y., Dong, J., Zhu, P., Xiu, D., Yan, L., Wen, L., Qiao, J., Tang, F., Fu, W.: Single-cell multiomics sequencing and analyses of human colorectal cancer. Science **362**(6418), 1060-1063 (Nov 2018). [https://doi.org/10.1126/science.aao3791](https://doi.org/10.1126/science.aao3791) (This URL will be updated soon.)

[^2]: Li, X. C., Liu, Y., Sch\"affer, A. A., Mount, S. M., Sahinalp, S. C.: Fair molecular feature selection unveils universally tumor lineage-informative methylation sites in colorectal cancer. [bioRxiv 2024.02.22.580595. [https://doi.org/10.1101/2024.02.22.580595](https://doi.org/10.1101/2024.02.22.580595)


