# AML Treatment Resistance — scRNA-seq Transcriptomics Analysis

**Candidate:** Mansi Chandra  
**Organisation:** MultiOmics Intelligence — Interview Practical Task  
**Date:** May 2026  
**GitHub:** https://github.com/codeby-MansiChandra/aml-resistance-pipeline

---

## Biological Question

> Which genes and pathways distinguish chemotherapy-sensitive from  
> chemotherapy-resistant Acute Myeloid Leukaemia (AML) cells  
> at single-cell resolution?

---

## Dataset

**Paper:** van Galen P, et al. (2019). Single-Cell RNA-Seq Reveals AML Hierarchies Relevant to Disease Progression and Immunity. *Cell*, 176(6), 1265–1281.  
**DOI:** https://doi.org/10.1016/j.cell.2019.01.031  
**GEO Accession:** GSE116256  
**Platform:** Seq-Well (nanowell-based scRNA-seq)  
**Input format:** Raw count matrices — one per sample (genes × cells)

### Sample Groups

| Group | Label | n samples | n cells | Biological meaning |
|-------|-------|-----------|---------|-------------------|
| Group A | AML_Diagnosis | 16 | 15,667 | Day 0 — pre-treatment — chemotherapy-naive |
| Group B | AML_Treated | 19 | 14,988 | Day 14–171 — post-chemotherapy — resistant |
| Reference | Healthy | 6 | 7,661 | Normal bone marrow |

**Key strength:** 11 patients have paired samples at both timepoints — same patient before and after chemotherapy — removing inter-patient variability from the comparison.

**Resistance definition:** Cells still present weeks after chemotherapy started — resistance defined by biological survival, not a clinical label.

### Limitations
- No clinical response scores or survival data linked to individual samples
- Early timepoints (Day 14) may not represent true resistance
- Five samples have fewer than 100 cells — reduced statistical reliability
- No mutation data (FLT3, NPM1) linked at single-cell level

---

## Repository Structure

```
aml-resistance-pipeline/
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

## Workflow Overview

```
Raw count matrices (GEO: GSE116256)
            │
            ▼
┌─────────────────────────┐
│  1. QC & Filtering      │  Mitochondrial %, gene count thresholds,
│  notebook 01            │  gene filtering — 38,316 cells retained
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  2. Normalisation &     │  Log-normalisation, 2000 HVGs,
│     Integration         │  PCA, Harmony batch correction
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  3. Clustering &        │  UMAP, Leiden clustering,
│     Annotation          │  8 cell types annotated, LSC score
│  notebook 02            │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  4. Differential        │  Pseudobulk DESeq2 — 691 significant DEGs
│     Expression          │  HOXA cluster lost, immune checkpoints gained
│  notebook 03            │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  5. Pathway Enrichment  │  GSEA Hallmark, GO, KEGG —
│  notebook 04            │  32 significant pathways
│                         │  Immune evasion signature identified
└─────────────────────────┘
```

---

## Key Findings

| Analysis | Finding |
|----------|---------|
| Cell types | 8 cell types: ProMono-like, GMP-like, Mono-like, T cell, NK cell, Erythroid, cDC, B cell |
| Top DEGs upregulated | KCNH2, SLC25A21, HCN3 — metabolic and ion channel reprogramming |
| Top DEGs downregulated | HOXA3, HOXA4, HOXA6, HOXA-AS3 — entire HOXA cluster lost in resistance |
| Immune checkpoints | CD274 (PD-L1) and TIGIT upregulated — immune evasion |
| GSEA pathways | Interferon response, Hedgehog signalling, EMT enriched in resistant cells |
| Biological story | Resistant cells activate immune evasion while losing normal haematopoietic identity |

---

## Tools & Packages

| Step | Tool | Reason |
|------|------|--------|
| QC & preprocessing | Scanpy | Standard scRNA-seq pipeline |
| Batch correction | Harmony | Correct per-sample technical variation |
| Clustering | Leiden algorithm | Resolution-flexible community detection |
| Differential expression | PyDESeq2 (pseudobulk) | Gold standard for scRNA-seq DE |
| Pathway enrichment | GSEApy | GSEA + ORA on validated gene sets |
| Visualisation | matplotlib, seaborn | Volcano, heatmap, UMAP, dot plots |

---

## Reproducibility — How to Run

### 1. Clone the repository
```bash
git clone https://github.com/codeby-MansiChandra/aml-resistance-pipeline.git
cd aml-resistance-pipeline
```

### 2. Set up the environment
```bash
conda env create -f envs/environment.yml
conda activate aml-scrna
```

### 3. Download the data
Download raw count matrices from GEO accession **GSE116256**:
```bash
# Go to: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE116256
# Download GSE116256_RAW.tar and extract into data/raw/
```

### 4. Run notebooks in order
```
01_qc_preprocessing → 02_clustering_annotation → 03_differential_expression → 04_pathway_enrichment
```

---

## References

van Galen P, et al. (2019). Single-Cell RNA-Seq Reveals AML Hierarchies Relevant to Disease Progression and Immunity. *Cell*, 176(6), 1265–1281. https://doi.org/10.1016/j.cell.2019.01.031

---

## License

This project is for interview assessment purposes — MultiOmics Intelligence candidate practical task, May 2026.
