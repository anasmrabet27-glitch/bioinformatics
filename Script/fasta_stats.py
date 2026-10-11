#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Bio.Seq import Seq
from Bio import SeqIO
from pathlib import Path
import pandas as pd
filename = Path(r"")
results = []

for record in SeqIO.parse(filename, "fasta"):
    seq = record.seq
    results.append({
    "ID": record.id,
    "length": len(seq),
    "A": seq.count("A"),
    "G": seq.count("G"),
    "T": seq.count("T"),
    "C": seq.count("C"),
    "GC%": ((seq.count("G") + seq.count("C"))/ len(seq)) * 100
    })


df = pd.DataFrame(results)
df

