# FALAFL
FALAFL: FAir muLti-sAmple Feature sELection. Applicable to comparative analysis of multi-patient data.



Welcome to the repository for `FALAFL`, an algorithmic approach based on combinatorial optimization and designed to perform feature selection in sequencing data which ensures a balanced selection of features from all patient samples in a cohort.

![Schema Figure for Sgootr](/assets/falafl_sysarch.pdf)


# Table of Contents

  1. [Getting Started](#start) 
     * [Setting Up](#setup): how to download the required tools and programs

  2. [Using `FALAFL`](#manual)
     * [Files](#files) 
       * [Input](#input): content and format of input files to `FALAFL`
       * [Ouput](#output): content and format of output files to `Sgootr`
     * [Example](#example): a guide to perform feature selection on the colorectal cancer patient cohort [^1]
  3. [Contact](#contact)

# Getting Started

## Setting up


<a name="start"></a>
# Getting Started

To help you get started with using `Sgootr`, we will first describe how to set up the required tools and programs, then lead you through an example that reproduces our main result on metastatic colorectal cancer patient CRC01 [^1].

<a name="setup"></a>
## Setting Up

Follow instructions to [install `conda`](https://conda.io/projects/conda/en/latest/user-guide/install/).

Follow instructions to [install `Gurobi`](https://support.gurobi.com/hc/en-us/articles/360044290292-How-do-I-install-Gurobi-for-Python-), retrieve a `Gurobi` license (which is [free for academics](https://www.gurobi.com/academia/academic-program-and-licenses/)), and [set up the license](https://www.gurobi.com/documentation/9.5/quickstart_mac/retrieving_and_setting_up_.html) on your computing environment.

Then:

```console
 $ git clone https://github.com/Storyboardslee/FALAFL.git
 $ cd FALAFL
```


<a name="manual"></a>
# Using `FALAFL`

We will describe the configurations and input files used by `FALAFL`, followed by an example to perform feature selection on the colorectal cancer patient cohort [^1].

<a name="config"></a>
## Configurations

<a name="files"></a>

## Files

Here we will describe the content and format for input and output for `FALAFL`.

<a name="input"></a>
### Input


<a name="output"></a>
### Output

<a name="example"></a>
## Example

<a name="contact"></a>
# Contact

We are glad you are using `FALAFL` and look forward to hearing your own creative way of applying `FALAFL` on your data! If you have encountered any issues with `FALAFL`, please report on the [issue forum](https://github.com/Storyboardslee/FALAFL/issues) or contact Xuan Cindy Li [[email]](xli1994@umd.edu). 

<!-- References -->

[^1]: Bian, S., Hou, Y., Zhou, X., Li, X., Yong, J., Wang, Y., Wang, W., Yan, J., Hu, B., Guo, H., Wang, J.,
Gao, S., Mao, Y., Dong, J., Zhu, P., Xiu, D., Yan, L., Wen, L., Qiao, J., Tang, F., Fu, W.: Single-cell multiomics sequencing and analyses of human colorectal cancer. Science **362**(6418), 1060-1063 (Nov 2018). [https://doi.org/10.1126/science.aao3791](https://doi.org/10.1126/science.aao3791)


