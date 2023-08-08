# Genic Region Interactive Plotting

This repository provides a Python script for generating interactive genomic data plots using the "numpy" and "matplotlib" libraries. The script enables you to visualize various data configurations through an interactive plotting interface. Follow the steps below to set up and execute the script.

## Prerequisites

1. Ensure you have Python installed on your system. You can check the installed version by running this command in your command line:

    ```
    python --version
    ```

2. Install the required libraries, "numpy" and "matplotlib," using the following commands in the command line:

    ```
    pip install numpy
    pip install matplotlib
    ```

## Installation

1. Download the provided files and unzip the `avg_dics.zip` file.
2. Place all the extracted files into a single folder. Confirm that all files are located within the same folder.

## Configuration

1. Open the `genic_region_interactive_plotting.py` file in a text editor. It's recommended to use a Python-specific editor like PyCharm.
2. Navigate to lines 15 to 54 in the script. This section contains various plot configurations.
3. Note that it's not feasible to include all configurations within a single plot. You'll need to choose a subset of configurations to display.
4. Replace lines 57 to 61 with your preferred subset of configurations. Ensure that each line ends with a comma.
5. Each line signifies a configuration and includes the following details:
    - Accession name
    - Real SNPs or predicted SNPs
    - Conversion specificity or combined conversions

## Running the Script

1. After making the necessary edits to the `genic_region_interactive_plotting.py` file, execute the script using this command:

    ```
    python genic_region_interactive_plotting.py
    ```

2. An interactive plot window will appear, resembling the attached image.
3. By clicking on the names displayed on the left side of the plot, you can toggle the corresponding plots on or off within the plotting area.

Feel free to experiment with different configurations to effectively visualize your data.
