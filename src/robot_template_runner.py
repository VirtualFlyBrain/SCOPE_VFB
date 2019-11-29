#!/usr/bin/env python

import pandas as pd
from gen_robot_template import gen_template, XrefLink


semantic_maps = ["Konstantinides_et_al_2018_OpticLobe"]
data_path = "../data/"
templates_path = "../templates/"

for s in semantic_maps:
    sm = pd.read_csv(data_path + s + "_semantic_permalinks.tsv", sep="\t")
    xrefs = []
    for i, r in sm.iterrows():
        xrefs.append(XrefLink(subj=r['fbbt'],
                              acc=r['permalink'],
                              db=r['dataset_name']))

    gen_template(template_file_name=templates_path + s + "_map.tsv",
                 xref_links=xrefs)




