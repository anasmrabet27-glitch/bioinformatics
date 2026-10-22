{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ffa40aa1-2b63-470f-83a4-5c7b2355ac3d",
   "metadata": {},
   "outputs": [],
   "source": [
    "from Bio import SeqIO\n",
    "import pandas as pd\n",
    "\n",
    "filename = r\"C:\\Users\\anasm\\Downloads\\ENSG00000012048.28 (2).fasta\"\n",
    "\n",
    "resultats = {}\n",
    "dernier_transcrit = None\n",
    "\n",
    "for record in SeqIO.parse(filename, \"fasta\"):\n",
    "    seq = record.seq\n",
    "    identifiant = record.id\n",
    "    description = record.description.lower()\n",
    "\n",
    "    if identifiant.startswith(\"ENST\"):\n",
    "        dernier_transcrit = identifiant\n",
    "\n",
    "        if identifiant not in resultats:\n",
    "            resultats[identifiant] = {\"id\": identifiant}\n",
    "\n",
    "        if \"cdna\" in description:\n",
    "            resultats[identifiant].update({\n",
    "                \"length_cdna\": len(seq),\n",
    "                \"cdna_GC%\": (\n",
    "                    (seq.count(\"G\") + seq.count(\"C\")) / len(seq) * 100\n",
    "                    if len(seq) > 0 else 0\n",
    "                )\n",
    "            })\n",
    "\n",
    "        elif \"cds\" in description:\n",
    "            resultats[identifiant].update({\n",
    "                \"length_cds\": len(seq),\n",
    "                \"cds_GC%\": (\n",
    "                    (seq.count(\"G\") + seq.count(\"C\")) / len(seq) * 100\n",
    "                    if len(seq) > 0 else 0\n",
    "                )\n",
    "            })\n",
    "\n",
    "    elif identifiant.startswith(\"ENSP\") and dernier_transcrit is not None:\n",
    "        resultats[dernier_transcrit].update({\n",
    "            \"protein_id\": identifiant,\n",
    "            \"protein_length_aa\": len(seq)\n",
    "        })\n",
    "\n",
    "df = pd.DataFrame(resultats.values())\n",
    "\n",
    "df.to_excel(\n",
    "    r\"C:\\Users\\anasm\\Downloads\\test1.xlsx\",\n",
    "    index=False\n",
    ")\n",
    "\n",
    "print(df)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
