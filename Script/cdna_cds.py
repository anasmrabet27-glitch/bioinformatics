#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Bio import SeqIO
import pandas as pd

filename = r"C:\Users\anasm\Downloads\ENSG00000012048.28 (2).fasta"

resultats = {}
dernier_transcrit = None

for record in SeqIO.parse(filename, "fasta"):
    seq = record.seq
    identifiant = record.id
    description = record.description.lower()

    if identifiant.startswith("ENST"):
        dernier_transcrit = identifiant

        if identifiant not in resultats:
            resultats[identifiant] = {"id": identifiant}

        if "cdna" in description:
            resultats[identifiant].update({
                "length_cdna": len(seq),
                "cdna_GC%": (
                    (seq.count("G") + seq.count("C")) / len(seq) * 100
                    if len(seq) > 0 else 0
                )
            })

        elif "cds" in description:
            resultats[identifiant].update({
                "length_cds": len(seq),
                "cds_GC%": (
                    (seq.count("G") + seq.count("C")) / len(seq) * 100
                    if len(seq) > 0 else 0
                )
            })

    elif identifiant.startswith("ENSP") and dernier_transcrit is not None:
        resultats[dernier_transcrit].update({
            "protein_id": identifiant,
            "protein_length_aa": len(seq)
        })

df = pd.DataFrame(resultats.values())

df.to_excel(
    r"C:\Users\anasm\Downloads\test1.xlsx",
    index=False
)

print(df)

