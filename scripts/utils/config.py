"""
config.py — all parameters and paths for the AML scRNA-seq pipeline.
Import this at the top of every notebook.

Usage:
    import sys, os
    sys.path.insert(0, os.path.dirname(os.getcwd()))
    from scripts.utils.config import *
"""

import os

# ── Repo root (set dynamically — no hardcoded paths) ──────────────────────────
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ── Paths ─────────────────────────────────────────────────────────────────────
DATA_RAW      = os.path.join(ROOT_DIR, "data", "raw")
DATA_PROC     = os.path.join(ROOT_DIR, "data", "processed")
DATA_META     = os.path.join(ROOT_DIR, "data", "metadata")
RESULTS_QC    = os.path.join(ROOT_DIR, "results", "qc")
RESULTS_CLUST = os.path.join(ROOT_DIR, "results", "clustering")
RESULTS_DE    = os.path.join(ROOT_DIR, "results", "de_analysis")
RESULTS_PATH  = os.path.join(ROOT_DIR, "results", "pathway")
RESULTS_FIG   = os.path.join(ROOT_DIR, "results", "figures")

# ── Dataset ───────────────────────────────────────────────────────────────────
GEO_ACCESSION  = "GSE116256"
DATASET_PAPER  = "van Galen et al. (2019) Cell"
DATASET_DOI    = "https://doi.org/10.1016/j.cell.2019.01.031"

# ── Sample groups ─────────────────────────────────────────────────────────────
# Primary comparison: healthy bone marrow vs AML relapse
GROUP_COL      = "group"             # column we create in metadata
GROUP_A_LABEL  = "AML_Diagnosis"     # treatment-sensitive (pre-treatment)     
GROUP_B_LABEL  = "AML_Treated"       # treatment-resistant (survived chemo)
SAMPLE_COL     = "sample_id"
PATIENT_COL    = "patient_id"


# All condition labels in the dataset
CONDITIONS = {
    "H"  : "Healthy",        # healthy donor
    "D"  : "AML_Diagnosis",  # AML at diagnosis (pre-treatment)
    "R"  : "AML_Relapse",    # AML at relapse (post-chemotherapy, resistant)
}

# ── QC thresholds ─────────────────────────────────────────────────────────────
MIN_GENES      = 200     # minimum genes detected per cell
MAX_GENES      = 5000    # maximum genes (above = likely doublet)
MIN_COUNTS     = 300     # minimum UMI counts per cell
MAX_PCT_MITO   = 20      # maximum mitochondrial gene %
MIN_CELLS      = 3       # minimum cells a gene must appear in

# ── Normalisation ─────────────────────────────────────────────────────────────
NORM_TARGET    = 1e4     # normalise to 10,000 counts per cell
N_HVG          = 2000    # number of highly variable genes

# ── Dimensionality reduction ──────────────────────────────────────────────────
N_PCS          = 30
N_NEIGHBORS    = 15
UMAP_MIN_DIST  = 0.3

# ── Clustering ────────────────────────────────────────────────────────────────
RESOLUTION     = 0.5     # Leiden resolution — adjust after inspecting UMAP

# ── Differential expression ───────────────────────────────────────────────────
DE_METHOD      = "DESeq2_pseudobulk"
PADJ_THRESH    = 0.05
LOG2FC_THRESH  = 1.0      # |log2FC| > 1 means 2-fold change

# ── Pathway enrichment ────────────────────────────────────────────────────────
GENE_SETS      = [
    "MSigDB_Hallmark_2020",
    "KEGG_2021_Human",
    "GO_Biological_Process_2021"
]
GSEA_PVAL      = 0.05

# ── Known AML marker genes for cell type annotation ───────────────────────────
CELL_TYPE_MARKERS = {
    "HSC"           : ["CD34", "SPINK2", "HOPX", "CRHBP"],
    "Progenitor"    : ["CD34", "AVP", "CYTL1"],
    "GMP"           : ["MPO", "ELANE", "AZU1", "PRTN3"],
    "ProMono"       : ["LYZ", "S100A8", "S100A9", "VCAN"],
    "Mono"          : ["CD14", "LYZ", "CST3", "FCN1"],
    "cDC"           : ["FCER1A", "CLEC9A", "CD1C"],
    "T_cell"        : ["CD3D", "CD3E", "CD3G", "TRAC"],
    "NK_cell"       : ["GNLY", "NKG7", "KLRD1"],
    "B_cell"        : ["MS4A1", "CD79A", "CD19"],
    "Erythroid"     : ["HBB", "HBA1", "HBA2", "GYPA"],
}

# ── LSC stemness signature (key for resistance interpretation) ─────────────────
LSC_SIGNATURE = [
    "CD34", "HOXA9", "HOXA10", "MEIS1", "MEF2C",
    "DNMT3B", "GPR56", "CD96", "ADGRG1"
]

# ── Reproducibility ───────────────────────────────────────────────────────────
RANDOM_SEED    = 42
