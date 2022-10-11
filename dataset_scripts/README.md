# Merge_COCO_FILES

Simple yet fully working tool

## Requirments
`python==3.x`

## Installation
```
Simply:
1- git clone https://github.com/mohamadmansourX/Merge_COCO_FILES.git
2- cd Merge_COCO_FILES
```

## COCO Files Merge Usage
```
python merge.py Json1.json Json2.json OUTPU_JSON.json
```

Json1 and Json2 are the two COCO files to be merged.

OUTPU_JSON is the output file for the combined results

<br>

**Note:**

The script will do the following checks as well:
1. Duplicate filenames checks (to count if the same image has two annotations)
2. Categories checks (Both files should have same categegories (name, id))

The reason I didn't mix categories, incase they are different, is to help annotators identifying any change in there categories. 
I believe this will be helpful incase of annotating a dataset as batches or splitting the annotation on members. Any change in ids caused by software being used or human mistake will be directly identified.
  

Example of Dog category existing in file 2 but not file 1
  
<code>AssertionError: Category name: Dog in file 2 does not exist in file 1</code>


Example of Cat category existing in both files but with different ids:

<code>AssertionError: Category name: Cat, id: 1 in file 1 and 2 in file 2</code>
<br>

## COCO File Class Edit Usage

```
python INPUT_JSON.json OUTPU_JSON.json Label1 Label2...
```

*Note: the script will do the necessary checks as well (duplicate filenames, ....)*


## Installation

``cocosplit`` requires python 3 and basic set of dependencies:

specifically, in addition to the requirements of the original repo, (``scikit-multilearn``) is required, it is included the requirements.txt file

```
pip install -r requirements
```


## Usage

The same as the original repo, with adding an argument (``--multi-class``) to preserve class distributions
The argument is optional to ensure backward compatibility

```
$ python cocosplit.py -h
usage: cocosplit.py [-h] -s SPLIT [--having-annotations]
                    coco_annotations train test

Splits COCO annotations file into training and test sets.

positional arguments:
  coco_annotations      Path to COCO annotations file.
  train                 Where to store COCO training annotations
  test                  Where to store COCO test annotations

optional arguments:
  -h, --help            show this help message and exit
  -s SPLIT              A percentage of a split; a number in (0, 1)
  --having-annotations  Ignore all images without annotations. Keep only these
                        with at least one annotation
  --multi-class         Split a multi-class dataset while preserving class
                        distributions in train and test sets
```

# Running

```
$ python cocosplit.py --having-annotations --multi-class -s 0.8 /path/to/your/coco_annotations.json train.json test.json
```

will split ``coco_annotation.json`` into ``train.json`` and ``test.json`` with ratio 80%/20% respectively. It will skip all
images (``--having-annotations``) without annotations.