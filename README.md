# SCOPE_VFB
A repo for scripting integration between SCOPE and VFB.  Status: experimental

Current workflow (to be superceded at some point by representation of clusters in VFB KB)

1. VFB adds Site node to KB for each DataSet.  The short_form = DataSet name on SCope.
1. matrix semantic map (mmm) curated to map contents SCope Loom file to FBbt (e.g. by VFB curator), loaded to SCope
2. ScOPE use mmm to generate a table of permalinks for each cluster  + mapped FBbt term. Table should have headers: dataset_name	fbbt	permalink - ([Example](https://github.com/VirtualFlyBrain/SCOPE_VFB/blob/master/data/Konstantinides_et_al_2018_OpticLobe_semantic_permalinks.tsv)).  Table should be deposited in [data/](https://github.com/VirtualFlyBrain/SCOPE_VFB/tree/master/templates)
3. [src/robot_template_runner.py](https://github.com/VirtualFlyBrain/SCOPE_VFB/blob/master/src/robot_template_runner.py) used to generate robot template deposited in [templates/](https://github.com/VirtualFlyBrain/SCOPE_VFB/tree/master/templates).
4. VFB.owl Jenkins build uses templates to generate xres in OWL and merges thse into into VFB.owl, which the VFB build pipeline combines withe Site Nodes to generate linkouts turns into linkouts.

Note - we could cut out step 3 and just have SCope generate the Robot template directly (step 4).
