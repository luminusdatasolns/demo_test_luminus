import os

def create_project_structure():
    # Define the directory structure
    directories = [
        'data/raw',
        'data/processed',
        'notebooks',
        'src/data',
        'src/features',
        'src/models',
        'src/utils',
        'tests'
    ]

    # Create directories
    for dir_path in directories:
        os.makedirs(dir_path, exist_ok=True)
        # Create __init__.py in Python package directories
        if dir_path.startswith('src'):
            with open(os.path.join(dir_path, '__init__.py'), 'w') as f:
                pass

    # Create README.md with template content
    readme_content = """# ML Project Template

## Project Structure    
- `data/`: Raw and processed data
  - `raw/`: Original data
  - `processed/`: Cleaned/transformed data
- `notebooks/`: Jupyter notebooks for EDA
- `src/`: Source code
  - `data/`: Data processing scripts
  - `features/`: Feature engineering code
  - `models/`: Model training code
  - `utils/`: Helper functions
- `tests/`: Unit tests

## Setup
1. Clone this repository
2. Create a conda environment: `conda create --name project_name python=3.11`
3. Activate environment: `conda activate project_name`
4. Install requirements: `pip install -r requirements.txt`

## Usage
[Add usage instructions here]
"""
    with open('README.md', 'w') as f:
        f.write(readme_content)

    # Create .gitignore
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Jupyter Notebook
.ipynb_checkpoints

# VS Code
.vscode/

# Data
data/raw/*
data/processed/*
!data/raw/.gitkeep
!data/processed/.gitkeep

# Environment
.env
.venv
env/
venv/
ENV/

# Mac OS
.DS_Store

# Model files
*.pkl
*.h5
*.joblib
"""
    with open('.gitignore', 'w') as f:
        f.write(gitignore_content)

    # Create placeholder files to keep empty directories
    for dir_path in ['data/raw', 'data/processed']:
        with open(os.path.join(dir_path, '.gitkeep'), 'w') as f:
            pass

    # Create requirements.txt
    requirements_content = """numpy
pandas
scikit-learn
matplotlib
seaborn
jupyter
black
pylint
pytest"""
    with open('requirements.txt', 'w') as f:
        f.write(requirements_content)

if __name__ == "__main__":
    create_project_structure()
    print("ML project template structure created successfully!")