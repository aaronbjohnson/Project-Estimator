# Project Estimator

![Caption for the picture.](/plots/plot.png)

This repository is an attempt to consolidate a project I’ve been  playing around with for a while. The idea is to use data that I collect from my freelance business in order to make giving estimations to my clients both more efficient and more accurate. For more info on my business and why I’m modeling this data, check out my initial post on my blog [here](https://aaronbjohnson.github.io/first-post.html).

## Contents

**feature_engineering.py** is the script used to create the **hour_page** and original **difficulty** variable. For more information on this, please visit the blog post linked above.

**modeling-notebook.ipynb** is the python notebook used to create the actual model. It uses the insights gained from the Exploratory Data Analysis. Again, check out the blog post for those insights.

**predictor_linear_<date>.py** uses the model created by the python notebook to make new predictions based on user inputs. As I'm always gathering new data, this file name will always change based on how recently I've appended new data. Keeping a record of when I created a particular model helps me to compare one model to another and to trace back problems.

**R-project-estimator.Rmd** contains the Exploratory Data Analysis and visualizations. A web-friendly version of this can be found in the **reports** folder, or in [this blog post](https://aaronbjohnson.github.io/project-estimator-continued-using-r.html).

**utilities.py** contains a few functions to make things easier. For example, there is a function that will encode a binary categorical variable given a dataframe and column name.

**data folder** contains both the original raw data `processed_<date>_projects.csv`, and the engineered data `engineered_data.csv` that was produced from the `feature_engineering.py` file described above.

**models folder** stores the model create from the python notebook.

**reports folder** contains the **html** version of the EDA notebook, completed in **RStudio**. The contents of this can also be viewed on the blog post [here](https://aaronbjohnson.github.io/project-estimator-continued-using-r.html).

**plots** folder contains an saved plots from the EDA.




## Running the program

From the project’s root folder, run the `predictor_linear_<date>.py` file:

```console
python predictor_linear_<date>.py
```

You will be prompted to enter information about the project’s total **number of pages**, whether or not a **3D model** will be required, and a **difficulty rating** (a guide for which is printed out prior to the imput prompts).

The model will then run and will output its estimation of the project length in **total hours**.

## Bug reports

If you discover any bugs, feel free to create an issue on GitHub. I also
encourage you to help even more by forking and sending me a pull request.

https://github.com/aaronbjohnson/Project-Estimator

## Maintainers

* Aaron Johnson (https://github.com/aaronbjohnson)

## License

MIT License

