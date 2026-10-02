# BRCA1 Isoform Analysis

A bioinformatics learning project: analysing the RefSeq transcripts of the
human *BRCA1* gene with Python (Biopython and Pandas), as a step towards
NGS data analysis.

## Question

How do human BRCA1 RefSeq transcripts differ in sequence length and GC content, and how can the coding sequence (CDS) and encoded protein be characterized using a representative GenBank record?

## Status

- [x] Length, base counts and GC% of the transcripts (FASTA)
- [ ] CDS extraction and validation from GenBank records
- [ ] Plots (length distribution, GC%)
- [ ] Conclusions
- [ ] Reusable command-line script

## Repository structure

```text
bioinformatics/
├── notebooks/
│   ├── 01_fasta_stats.ipynb      # FASTA parsing, base counts, GC% (Pandas)
│   ├── 02_genbank_cds.ipynb      # CDS extraction and validation
│   ├── 03_visualisation.ipynb    # Plots
│   └── 04_conclusions.ipynb      # Interpretation of the results
├── scripts/
│   └── fasta_stats.py            # Command-line version of the FASTA statistics
├── data/
│   └── README.md                 # Data sources and download date
├── results/
│   └── figures/
├── requirements.txt
└── README.md
```

Folders are added as the project progresses.

## Installation

```bash
git clone https://github.com/anasmrabet27-glitch/bioinformatics.git
cd bioinformatics
pip install -r requirements.txt
```

`requirements.txt`:

```text
biopython
pandas
matplotlib
```

## Data

The BRCA1 transcript sequences used in this project were obtained from the NCBI RefSeq database.

  -Gene: BRCA1 (Breast Cancer 1)
  -NCBI Gene ID: 672
  -Database: NCBI RefSeq
  -Source: NCBI Gene
  -Data page: https://www.ncbi.nlm.nih.gov/datasets/gene/672/
  -Download date: 2026-10-02

The sequence files are not included in this repository. They should be downloaded from the NCBI database and placed in this directory.
The exact RefSeq accession numbers used in the analysis are documented here to ensure reproducibility.

## Analysis Workflow

1) RefSeq transcripts      
2) FASTA parsing
3) Length + nucleotide counts + GC%
4) Pandas DataFrame
5) GenBank records
6) CDS extraction and validation
7) Protein translation
8) Comparison of transcripts
9)Visualization
11)Biological interpretation

## Results

The analysis will compare:

-Transcript length
-A, T, G and C nucleotide counts
-GC percentage
-CDS length
-Protein length
-Protein sequences
-Number of distinct protein products

## Figures will be stored in:

results/figures/



## Tools

- Python 3
- Biopython
- Pandas
- Matplotlib
- Jupyter Notebook

## Limitations

This project is intended as a bioinformatics learning project. The analysis is based on publicly available RefSeq annotations and should not be interpreted as an experimental validation of transcript or protein function.

## Author

Learning bioinformatics and genomics. Feedback is welcome.
