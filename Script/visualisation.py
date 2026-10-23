#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r"")

print(df.head())


# In[ ]:


import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))

plt.barh(df.iloc[:, 0].astype(str), df.iloc[:, 1])

plt.xlabel("length_cdna")
plt.ylabel("id")
plt.title("Longueur_cdna")
plt.tight_layout()
plt.show()


# In[ ]:


plt.figure(figsize=(12, 8))

plt.barh(df.iloc[:, 0].astype(str), df.iloc[:, 3])

plt.xlabel("length_cds")
plt.ylabel("id")
plt.title("Longueur_cds")
plt.tight_layout()
plt.show()


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel(r"")

x = np.arange(len(df))
largeur = 0.4

plt.figure(figsize=(14, 6))

plt.bar(x - largeur/2, df["cdna_GC%"],
        largeur, label="cDNA")

plt.bar(x + largeur/2, df["cds_GC%"],
        largeur, label="CDS")

plt.xlabel("Transcrits")
plt.ylabel("GC (%)")
plt.title("Comparaison du GC % des cDNA et des CDS")
plt.xticks(x, df["id"], rotation=90)
plt.legend()
plt.tight_layout()
plt.show()

