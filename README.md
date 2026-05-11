# AML Treatment Resistance — scRNA-seq Transcriptomics Analysis

**Candidate:** Mansi Chandra  
---

## Biological Question

> Which genes and pathways distinguish healthy bone marrow cells from treatment-resistant  
> Acute Myeloid Leukaemia (AML) cells at single-cell resolution?

---

## Dataset

**Paper:** van Galen P, et al. (2019). Single-Cell RNA-Seq Reveals AML Hierarchies Relevant to Disease Progression and Immunity. *Cell*, 176(6), 1265–1281.  
**DOI:** https://doi.org/10.1016/j.cell.2019.01.031  
**GEO Accession:** GSE116256  
**Platform:** Seq-Well (nanowell-based scRNA-seq)  
**Input format:** Raw count matrices — one per sample (genes × cells)

### Sample Groups

| Group | Label | n samples | n cells (approx) | Biological meaning |
|-------|-------|-----------|------------------|-------------------|
| Group A | Healthy donors | 5 | ~7,700 | Normal bone marrow — treatment-sensitive baseline |
| Group B | AML diagnosis | 16 | ~16,000 | Pre-treatment leukaemic state |
| Group B (relapse) | AML relapse | subset | ~7,000 | Post-chemotherapy resistant disease |

**Primary comparison:** Healthy donors (Group A) vs AML relapse samples (Group B)  
**Rationale:** Relapse samples represent cells that survived chemotherapy — the biological definition of treatment resistance. Healthy donors represent the normal haematopoietic baseline that chemotherapy is designed to spare.

### Why This Dataset

- Raw count matrices — full pipeline run from scratch, no preprocessing assumptions inherited
- Small and manageable — ~38,000 cells total, fast to process
- Clinically meaningful groups — diagnosis vs relapse gives direct treatment resistance signal
- Paired samples — some patients have both diagnosis and relapse, removing inter-patient noise
- Highly cited — van Galen 2019 is a landmark AML scRNA-seq paper, findings well validated
- Rich cell type diversity — HSC, GMP, ProMono, Mono, cDC, T cells, B cells all represented

### Limitations

- Seq-Well protocol (not 10x Genomics) — lower sensitivity than modern platforms
- Older dataset (2019) — library sizes smaller than current standards
- Not all patients have paired diagnosis + relapse samples
- Healthy donors are different individuals from AML patients — some inter-individual variability

---

## Workflow Overview

```
GEO Raw Count Matrices (per sample .txt files)
            │
            ▼
┌─────────────────────────┐
│  1. QC & Filtering      │  FastQC metrics, mitochondrial %, gene/UMI thresholds,
│                         │  doublet detection (Scrublet), library size
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  2. Normalisation &     │  Log-normalisation, highly variable gene selection,
│     Integration         │  PCA, Harmony batch correction across samples
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  3. Clustering &        │  UMAP, Leiden clustering, cell type annotation
│     Annotation          │  using canonical haematopoietic marker genes
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  4. Differential        │  Pseudobulk DESeq2: healthy vs AML relapse
│     Expression          │  log2FC, padj, volcano plot, heatmap
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  5. Pathway Enrichment  │  GSEA (MSigDB Hallmark), GO, KEGG,
│     & Interpretation    │  LSC stemness, myeloid differentiation block
└─────────────────────────┘
```

---

## Repository Structure

```
aml-treatment-pipeline/
│
├── data/
│   ├── raw/               # Raw count matrices from GEO (not git tracked)
│   ├── processed/         # AnnData objects after QC and normalisation
│   └── metadata/          # Sample metadata CSV
│
├── notebooks/             # Analysis notebooks — run in order
│   ├── 01_qc_preprocessing.ipynb
│   ├── 02_clustering_annotation.ipynb
│   ├── 03_differential_expression.ipynb
│   └── 04_pathway_enrichment.ipynb
│
├── scripts/
│   └── utils/
│       └── config.py      # All parameters and paths in one place
│
├── results/               # All outputs — figures, tables, objects
│   ├── qc/
│   ├── clustering/
│   ├── de_analysis/
│   ├── pathway/
│   └── figures/
│
├── envs/
│   └── environment.yml    # Conda environment — fully reproducible
│
├── presentation/          # Final slide deck
├── .gitignore
└── README.md
```

---

## Key Tools

| Step | Tool | Reason |
|------|------|--------|
| QC & preprocessing | Scanpy, Scrublet | Standard scRNA-seq QC pipeline |
| Batch correction | Harmony | Correct for per-sample technical variation |
| Clustering | Leiden algorithm | Resolution-flexible, community standard |
| Cell type annotation | Canonical markers | Haematopoietic lineage markers well established |
| Differential expression | DESeq2 (pseudobulk) | Accounts for within-patient correlation, gold standard |
| Pathway enrichment | GSEApy, clusterProfiler | GSEA + ORA on validated gene sets |
| Visualisation | matplotlib, seaborn | Volcano, heatmap, UMAP, dot plots |

---

## Reproducibility — How to Run

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/aml-treatment-pipeline.git
cd aml-treatment-resistance
```

### 2. Set up the environment
```bash
conda env create -f envs/environment.yml
conda activate aml-scrna
```

### 3. Download the data
See `data/raw/README.md` for step-by-step GEO download instructions.  
GEO accession: **GSE116256**

### 4. Run notebooks in order
```
01 → 02 → 03 → 04
```
Each notebook saves its output to `data/processed/` or `results/` for the next step.

---

## Biological Background

Acute Myeloid Leukaemia (AML) is a blood cancer characterised by rapid proliferation of immature myeloid cells (blasts) in the bone marrow. Standard treatment is induction chemotherapy (cytarabine + anthracycline). While ~70% of patients achieve complete remission, ~50% relapse with chemotherapy-resistant disease — the central clinical problem this project addresses.

**Key resistance mechanisms in AML:**
- Leukaemic stem cells (LSCs) — quiescent, evade chemotherapy, drive relapse
- Myeloid differentiation block — blasts fail to mature, remain proliferative
- FLT3, NPM1, DNMT3A mutations — alter stem cell self-renewal and drug response
- Immune evasion — downregulation of MHC and NK ligands in resistant cells

---

## Expected Key Findings

Based on published literature, the analysis is expected to identify:
- Upregulation of LSC stemness genes (CD34, HOXA, MEIS1) in relapse vs healthy
- Enrichment of OXPHOS and metabolic reprogramming pathways in resistant cells
- Downregulation of myeloid differentiation genes (CEBPA, SPI1) in AML
- Immune evasion signatures in the AML tumour microenvironment

---

## References

van Galen P, et al. (2019). Single-Cell RNA-Seq Reveals AML Hierarchies Relevant to Disease Progression and Immunity. *Cell*, 176(6), 1265–1281. https://doi.org/10.1016/j.cell.2019.01.031


