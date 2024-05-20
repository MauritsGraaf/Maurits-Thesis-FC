
# Beyond Reviews: Validating Online Consumer Reviews Using Unsupervised Machine Learning Methods

This thesis addresses the challenge of identifying fake online reviews in the rapidly growing e-commerce sector. By leveraging unsupervised machine learning models, it aims to enhance the reliability of consumer feedback systems. The study evaluates various models to understand their effectiveness in detecting fraudulent reviews. The ultimate goal is to promote a more transparent and trustworthy e-commerce marketplace. This research was conducted for the Rotterdam School of Management and Feedback Company, a prominent experience management agency in the Netherlands.

![logo](https://github.com/MauritsGraaf/Maurits-Thesis-FC/assets/147798957/8c25c273-3497-4ea9-bf96-a15300ca3842)
![logo](https://github.com/MauritsGraaf/Maurits-Thesis-FC/assets/147798957/1291a0e3-6576-444c-8f6c-24344a330e6a)

## Table of contents

1. [Title and Description](#title)
2. [Acknowledgements](#acknowledgements)
3. [Installation](#installation)
6. [Usage/Examples](#usage/examples)
7. [Support](#support)

## Acknowledgements

The dataset used in this thesis is based on the research presented in the following paper:

- Hou, Y., Li, J., He, Z., Yan, A., Chen, X., & McAuley, J. (2024). Bridging language and items for retrieval and recommendation. arXiv Preprint arXiv:2403.03952. https://arxiv.org/abs/2403.03952


The FraudEagle model and its implementation were informed by the following work:

- Akoglu, L., Chandy, R., & Faloutsos, C. (2013). Opinion Fraud detection in online reviews by network effects. Proceedings of the International AAAI Conference on Web and Social Media, 7, 2–11. https://doi.org/10.1609/icwsm.v7i1.14380

The SpEagle model and its implementation were informed by the following work:

- Rayana, S., & Akoglu, L. (2015). Collective Opinion Spam Detection. Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 21, 985–994. https://doi.org/10.1145/2783258.2783370

The ASM model and its implementation were informed by the following work:

- Mukherjee, A., Kumar, A., Liu, B., Wang, J., Hsu, M., Castellanos, M., & Ghosh, R. (2013). Spotting opinion spammers using behavioral footprints. Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 19, 632–640. https://doi.org/10.1145/2487575.2487580


## Installation

### Prerequisites

1. **Python**: Ensure that Python 3.6 or later is installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).
2. **Git**: Ensure that Git is installed on your system. You can download Git from [git-scm.com](https://git-scm.com/).

### Cloning the Repository

1. Clone the repository to your local machine using the following command:
```bash
git clone https://github.com/MauritsGraaf/Maurits-Thesis-FC
```

2. Navigate to the project directory:
```bash
cd Maurits-Thesis-FC
```

### Creating a virtual environment
1. Create a virtual environment to manage dependencies:
```bash
python -m venv venv
```

2. Activate the virtual environment
On windows:
```bash
venv\Scripts\activate
```
On MacOS and Linux:
```bash
source venv/bin/activate
```

### Installing dependencies
1. Install the required dependencies using `pip`:
```bash
pip install -r requirements.txt
```

### Setting Up the Environment Variables
1. Create a `.env` file in the root directory of the project and add the necessary environment variables. For example:
```bash
DATASET_PATH=/path/to/your/dataset
OUTPUT_PATH=/path/to/save/output
```

### Running the notebooks
1. The repository contains four Jupyter Notebook files for different stages of the analysis:

- `Fake Reviews Notebook ~ Data preparation.ipynb`
- `Fake Reviews Notebook ~ FraudEagle.ipynb`
- `Fake Reviews Notebook ~ SpEagle.ipynb`
- `Fake Reviews Notebook ~ ASM.ipynb`
- `comparing_outputs.ipynb`

2. To run these notebooks, start Jupyter Notebook in the project directory:
```bash
jupyter notebook
```

3. Open and run each notebook in the same order as descriped in step 1 of this section.

## Usage/Examples

### Running the Notebooks
The repository contains five Jupyter Notebook files, each focusing on different stages of the analysis:

1. Data preparation
- `Fake Reviews Notebook ~ Data preparation.ipynb`
- Prepares the dataset for analysis by cleaning and preprocessing the data.
- To run this notebook: 

```bash
jupyter notebook "Fake Reviews Notebook ~ Data preparation.ipynb"
```

2. FraudEagle
- `Fake Reviews Notebook ~ FraudEagle.ipynb`
- Implements and runs the FraudEagle model to detect fake reviews.
- To run this notebook: 
```bash
jupyter notebook "Fake Reviews Notebook ~ FraudEagle.ipynb"
```

3. SpEagle model
- `Fake Reviews Notebook ~ SpEagle.ipynb`
- Implements and runs the SpEagle model to detect fake reviews.
- To run this notebook: 
```bash
jupyter notebook "Fake Reviews Notebook ~ SpEagle.ipynb"
```

4. ASM model
- `Fake Reviews Notebook ~ ASM.ipynb`
- Implements and runs the ASM model to detect fake reviews.
- To run this notebook: 
```bash
jupyter notebook "Fake Reviews Notebook ~ ASM.ipynb"
```

5. Comparing Outputs
- `comparing_outputs.ipynb`
- Compares the outputs of the different models to evaluate their performance.
- To run this notebook: 
```bash
jupyter notebook "comparing_outputs.ipynb"
```

### Example workflow
1. **Data preparation:**
- Start by running the data preparation notebook to clean and preprocess your dataset or use the HuggingFace Download. This step ensures that the data is in the correct format for the subsequent models.

2. **Running models:**
- After preparing the data, sequentially run the FraudEagle, SpEagle, and ASM notebooks. Each notebook contains specific instructions and code cells that need to be executed to apply the respective model to the data.

3. **Comparing Results:**
- Finally, run the comparing outputs notebook to evaluate and compare the performance of the FraudEagle, SpEagle, and ASM models. This notebook will generate visualizations and metrics to help you understand the strengths and weaknesses of each model.

### Command Line Interface
If you prefer to run the notebooks programmatically, you can use the following commands in your terminal:

```bash
# Data Preparation
jupyter nbconvert --to notebook --execute "Fake Reviews Notebook ~ Data preparation.ipynb"

# FraudEagle Model
jupyter nbconvert --to notebook --execute "Fake Reviews Notebook ~ FraudEagle.ipynb"

# SpEagle Model
jupyter nbconvert --to notebook --execute "Fake Reviews Notebook ~ SpEagle.ipynb"

# ASM Model
jupyter nbconvert --to notebook --execute "Fake Reviews Notebook ~ ASM.ipynb"

# Comparing Outputs
jupyter nbconvert --to notebook --execute "comparing_outputs.ipynb"
```



## Support

If you have any questions, suggestions, or need further assistance with the repository, please feel free to contact me:

**Maurits Graaf**
- **Email:** maurits.graaf@hotmail.com
- **GitHub:** github.com/MauritsGraaf
- **LinkedIn:** https://nl.linkedin.com/in/maurits-graaf-a740341b6


## Gif
![review_gif](https://github.com/MauritsGraaf/Maurits-Thesis-FC/assets/147798957/5659563c-dbdf-4e3e-9938-7139b035b52f)



