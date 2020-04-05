# early_identification
This is a simple library to make analyzing gradescope data easier. Built-in functions will clean and sanitize the data. The package will also generate a couple of standard graphs and return the cleaned data to the user so they can create their own graphs.

## Example Usage
First install the package (in the root of this git directory) with
```
python setup.py develop
```
This package simplifies may lines of data cleaning into a few short lines
```
from earlyidentify import StudentData
data = StudentData(["data/HW1_scores.csv", "data/HW2_scores.csv", "data/HW3_scores.csv"], "SID")
```
The first argument to `StudentData` should be a list of the file paths (order these from first to last pset). The second argument should be the identifier to join these data sets on (preferable use the anonymous key that Gradescope generates). If you want to do additionally filtration, you can specify students to drop by any property. For example, if I wanted to drop students with certain first names, I would do
```
left = ["Anis", "Ashkhen", "Cara", "Desiree", "James", "Lingdi", "Reza", "Suzana", "Xiaoxuan"]
data = StudentData(["data/HW1_scores.csv", "data/HW2_scores.csv", "data/HW3_scores.csv"], "SID", "First Name", left)
```
Once you've imported your data, there are three key functions. The first function automatically graphs pset averages. It can be called out of the box as `test.graph_average()`. You can also call it with a threshold value to only look at students who have a lower than 80% average, for example as `data.graph_average(0.8)`. Finally, you can set `auto_ignore=True` to ignore students that had zeros on either of the first two psets to filter out students who may have dropped the class (the package automatically drops people with all zeros for this reason).

If you want to just use the cleaned data on your own, you can call `get_psets()` (or `get_data()`) to get the pset averages (or the raw question scores). This will be returned as a Pandas DataFrame. The problem set scores are normalized on a 0-1 scale since psets are usually weighted the same, but the questions data is left unnormalized since some questions are worth more than others.
