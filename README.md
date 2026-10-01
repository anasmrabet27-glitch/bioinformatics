# BRCA1 Isoform Analysis

A bioinformatics learning project: analysing the RefSeq transcripts of the
human *BRCA1* gene with Python (Biopython and Pandas), as a step towards
NGS data analysis.

## Question

How do the RefSeq transcripts of *BRCA1* differ in length, GC content and
coding sequence, and how many distinct proteins do they encode?

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
git clone https://github.com/<your-username>/bioinformatics.git
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

Sequence files are not stored in this repository. The *BRCA1* transcripts
come from NCBI RefSeq (Gene ID 672), downloaded on `YYYY-MM-DD`. Place the
files in `data/` and adapt the paths at the top of each notebook.

## Methods

1. Parse the transcripts with `Bio.SeqIO`.
2. Compute length, A/T/G/C counts and GC% for each transcript.
3. Extract each CDS from GenBank records and validate it
   (`translate(cds=True)`), then compare it with the annotated protein.
4. Summarise and plot the results.

## Results

To be added.

## Other notebooks

Earlier exercises are kept in `archive/`: DNA manipulation with `Bio.Seq`,
reading FASTA files with `SeqIO`, and basic FASTQ statistics
(reads, N bases, GC%, mean Phred quality).

## Tools

- Python 3
- Biopython
- Pandas
- Matplotlib

## Author

Learning bioinformatics and genomics. Feedback is welcome.
