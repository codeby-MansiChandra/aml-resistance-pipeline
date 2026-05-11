# Data Download Instructions

Raw data files are in the raw file (file size was small).
Follow the steps below to download GSE116256.

---

## Dataset

**van Galen et al. (2019), Cell**  
**GEO Accession:** GSE116256  
**URL:** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE116256

---

## What to Download

Download the supplementary count matrix files.
Each file corresponds to one sample (one patient, one timepoint).

File naming convention:
- `GSE116256_RAW.tar` — archive containing all per-sample count matrices

### Steps

1. Go to: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE116256
2. Scroll to **Supplementary file** section at the bottom
3. Download `GSE116256_RAW.tar` via the (http) link
4. Extract the archive into this folder: `data/raw/`

### Command line download (Windows)
```bash
curl -o GSE116256_RAW.tar "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE116nnn/GSE116256/suppl/GSE116256_RAW.tar"
tar -xf GSE116256_RAW.tar
```

---

## Sample Key

After extraction you will see files named by sample ID.
Use this key to map sample IDs to conditions:

| Sample prefix | Condition | Group |
|--------------|-----------|-------|
| BM1, BM2, BM3, BM4, BM5 | Healthy donor | Group A |
| AML_D (diagnosis) | AML pre-treatment | — |
| AML_R (relapse) | AML post-chemotherapy | Group B |

Exact sample IDs and their conditions are recorded in:
`data/metadata/sample_metadata.csv` — created in notebook 01.

---

## Expected folder structure after download

```
data/raw/
├── GSE116256_RAW.tar          # original archive (can delete after extraction)
├── BM1_matrix.txt.gz          # healthy donor 1
├── BM2_matrix.txt.gz          # healthy donor 2
├── ...
├── AML314D_matrix.txt.gz      # AML patient 314, diagnosis
├── AML314R_matrix.txt.gz      # AML patient 314, relapse
├── ...
└── README.md                  # this file
```

---

> Note: File sizes are small (a few MB each) — total download ~200 MB.
> This is raw data — no preprocessing has been applied by the authors.
