Phylogenomics-Cytochrome-C-Pipeline

Overview

This project performs an evolutionary analysis of the "Cytochrome c gene" across multiple species. The pipeline uses sequence retrieval, multiple sequence alignment, and phylogenetic analysis to investigate evolutionary relationships and identify conserved regions.

Species Included

Human
Chimpanzee
Gorilla
Mouse
Chicken
Zebrafish

Project Workflow

```text
Sequence Retrieval (NCBI)
            ↓
FASTA File Preparation
            ↓
Multiple Sequence Alignment (Clustal Omega)
            ↓
Alignment Analysis (Biopython)
            ↓
Phylogenetic Tree Construction (MEGA)
            ↓
Evolutionary Interpretation
            ↓
Report Writing

Project Contents

```text
Phylogenomics-Cytochrome-C-Pipeline/
│
├── cytochrome_c_sequences.fasta   # Raw sequence data
├── alignment.fas                  # Multiple sequence alignment output
├── analysis.py                    # Alignment analysis script
├── pipeline.py                    # Main pipeline script
└── README.md                      # Project documentation
```

Requirements

Python 3.x
Biopython

Install dependencies:

```bash
pip install biopython
```

How to Run

Run the pipeline using:

```bash
python pipeline.py
```

To analyze the alignment separately:

```bash
python analysis.py
```

Results
The analysis aims to:
Compare Cytochrome c sequences among species.
Identify conserved regions.
Examine evolutionary relationships.
Support phylogenetic inference using sequence similarity.

Expected Findings

Human and Chimpanzee are expected to show the highest sequence similarity.
Gorilla is expected to cluster closely with Human and Chimpanzee.
Mouse is expected to be more distant.
Chicken and Zebrafish are expected to show greater evolutionary divergence.

Data Source

Sequences were obtained from the National Center for Biotechnology Information database.

Author
Maham Taqi

