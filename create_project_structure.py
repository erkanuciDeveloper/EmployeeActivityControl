import os

# Define the directory structure
directories = [
    "src/presentation/app",
    "src/presentation/notebooks",
    "src/domain/model",
    "src/domain/utils",
    "src/infrastructure/data/raw",
    "src/infrastructure/data/processed",
    "src/infrastructure/data/features",
    "src/infrastructure/scripts/data_collection",
    "src/infrastructure/scripts/models",
    "src/infrastructure/models/saved_models",
    "src/infrastructure/logs",
    "src/infrastructure/exceptions",
    "tests/unit",
    "tests/integration",
    "tests/e2e",
    "docs",
    ".vscode",
]

# Create the directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)

# Define the files to create
files = [
    "src/infrastructure/scripts/data_collection/mouse_activity.py",
    "src/infrastructure/scripts/data_collection/keyboard_activity.py",
    "src/infrastructure/scripts/data_collection/screen_activity.py",
    "src/infrastructure/scripts/data_preprocessing.py",
    "src/infrastructure/scripts/feature_engineering.py",
    "src/infrastructure/scripts/model_training.py",
    "src/infrastructure/scripts/model_evaluation.py",
    "src/presentation/notebooks/exploratory_data_analysis.ipynb",
    "src/domain/utils/data_utils.py",
    "src/domain/utils/model_utils.py",
    "src/presentation/app/app.py",
    "src/presentation/app/requirements.txt",
    "src/infrastructure/exceptions/custom_exceptions.py",
    "docs/requirements.md",
    "docs/design.md",
    "docs/api.md",    
    "setup.py",
    ".vscode/settings.json",  # Include settings.json in .vscode directory
    "README.md",
]

# Create the files
for file in files:
    open(file, 'a').close()

print("Project structure and files created successfully.")
