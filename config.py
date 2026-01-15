"""
Configure your parameters
"""
import os
# Seeding
SEED = 123
DEVICE='cuda:1'

# Training Parameters
MAX_EPOCHS = 1000
VAL_INTERVAL = 1
BATCH_SIZE = 50
LEARNING_RATE = 1e-1
NUM_WORKERS = 8
MODEL_TYPE = 'sfcne'
MODEL_NAME = f'your_model_name'

# Loss Parameters
CONTRASTIVE_TEMPERATURE = 0.05

# Early Stopping
PATIENCE = 10
SCHEDULER_FACTOR = 0.5
SCHEDULER_PATIENCE = 5

# Data
COHORT_SSL = 'your-cohort'
COHORT_EXTRACT = 'your-cohort'
IMG_SIZE = 96

# ============================================
# DIMENSIONALITY REDUCTION SETTINGS
# ============================================

# Choose reduction method: 'umap', 'tsne', or 'pca'
REDUCTION_METHOD = 'umap'  # Options: 'umap', 'tsne', 'pca'
# UMAP-specific parameters
N_NEIGHBORS = 10        # Number of neighbors (UMAP only)
MIN_DIST = 1.0         # Minimum distance (UMAP only)
# t-SNE-specific parameters
PERPLEXITY = 30        # Perplexity (t-SNE only, typically 5-50)
# General parameters
RANDOM_STATE = 3       # Random seed for reproducibility

# ============================================
# CONFIGURE PATHS
# ============================================

# File Paths (CHANGE THESE TO YOUR PATHS)
JSON_PATH = '/path/to/your/file'
LOG_DIR = '/path/to/your/folder'
MODEL_DIR = '/path/to/your/folder'
IMAGES_EXT_DIR = '/path/to/your/folder'
FEATURES_EXT_DIR = '/path/to/your/folder'
VIZ_DIR = '/path/to/your/folder'
DATA_PATH = f'/path/to/your/file'


# ============================================
# VIZUALIZATION SETTINGS
# ============================================
POINT_SIZE = 200
TRANSPARENCY = 0.7
FONTSIZE_MAX = 30
FONTSIZE_MIN = 20
