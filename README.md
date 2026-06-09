Phylogenomics-Cytochrome-C-Pipeline

Overview

This project performs an evolutionary analysis of the **Cytochrome c gene** across multiple species. The pipeline uses sequence retrieval, multiple sequence alignment, and phylogenetic analysis to investigate evolutionary relationships and identify conserved regions.

Species Included

* Human
* Chimpanzee
* Gorilla
* Mouse
* Chicken
* Zebrafish


Project Workflow

```text id="wf1"
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
```



Project Contents

```text id="wf2"
Phylogenomics-Cytochrome-C-Pipeline/
│
├── cytochrome_c_sequences.fasta   # Raw sequence data
├── alignment.fas                  # Multiple sequence alignment output
├── analysis.py                    # Alignment analysis script
├── pipeline.py                    # Main pipeline script
├── phylogenetic_tree.png          # Phylogenetic tree image
└── README.md                      # Project documentation
```



Requirements

* Python 3.x
* Biopython

Install dependencies:

```bash id="req1"
pip install biopython
```



How to Run

Run the full pipeline:

```bash id="run1"
python pipeline.py
```

Run alignment analysis separately:

```bash id="run2"
python analysis.py
```



Results

The analysis focuses on:

* Comparison of Cytochrome c sequences among species
* Identification of conserved regions
* Evolutionary relationship analysis
* Phylogenetic inference based on sequence similarity

Alignment Statistics

* Number of sequences: 6
* Alignment length: 5565



Phylogenetic Tree

![Phylogenetic Tree](phylogenetic_tree.png)

The phylogenetic tree illustrates the evolutionary relationships among Human, Chimpanzee, Gorilla, Mouse, Chicken, and Zebrafish based on Cytochrome c sequence alignment.


Expected Findings

* Human and Chimpanzee show the highest sequence similarity.
* Gorilla clusters closely with Human and Chimpanzee.
* Mouse is more evolutionarily distant.
* Chicken and Zebrafish show greater evolutionary divergence.
* Conserved regions indicate functionally important portions of the Cytochrome c gene.


Data Source

Sequences were obtained from the National Center for Biotechnology Information database.


Tools Used

* NCBI GenBank
* Clustal Omega
* Biopython
* MEGA
* Visual Studio Code

Author

Maham Taqi
