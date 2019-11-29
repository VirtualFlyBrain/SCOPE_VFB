#!/usr/bin/env python

from collections import OrderedDict, namedtuple
import pandas as pd

XrefLink = namedtuple('XrefLink', ['subj', 'db', 'acc'])


def gen_template(template_file_name, xref_links):
    """Takes a list od XrefLink.  Writes a Robot template to use for adding xrefs."""

    template_seed = OrderedDict([('ID', 'ID'), ('CLASS_TYPE', 'CLASS_TYPE'),
                                 ('RDF_Type', 'TYPE'), ("Xref", "A oboInOwl:hasDbXref")])

    template = pd.DataFrame.from_records([template_seed])

    # Copied from Clare's code. Probably not needed
    row_od = OrderedDict([])  # new template row as an empty ordered dictionary
    for c in template.columns:  # make columns and blank data for new template row
        row_od.update([(c, "")])

    # populate table
    for xrl in xref_links:
        row_od["CLASS_TYPE"] = "subclass"
        row_od["RDF_Type"] = "owl:Class"
        row_od['ID'] = xrl.subj
        row_od["Xref"] = ':'.join([xrl.db, xrl.acc])

    # Hmm - this is a bit weird again. Seems to work though.
    new_row = pd.DataFrame.from_records([row_od])
    template = pd.concat([template, new_row], ignore_index=True, sort=False)

    # Write to csv
    template.to_csv(template_file_name, sep="\t", header=True, index=False)
