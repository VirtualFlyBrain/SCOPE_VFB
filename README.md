# SCOPE_VFB [![Build Status](https://travis-ci.org/VirtualFlyBrain/SCOPE_VFB.svg?branch=master)](https://travis-ci.org/VirtualFlyBrain/SCOPE_VFB)

A repo for scripting integration between [SCOPE](http://scope.aertslab.org/) and VFB.  Status: In USE FOR VFB LINKOUT GENERATION

Code here was the result of a brief hackathon to being the process of linking VFB and SCope  Work is needed to make it more stable.  It is likely to be superceded in the near future.

Current workflow (to be superceded at some point by representation of clusters in VFB KB)

1. VFB adds Site node to KB for each DataSet.  Site.short_form = DataSet name on SCope.
1. [matrix semantic map](https://github.com/HumanCellAtlas/matrix_semantic_map/blob/master/README.md) (mmm) curated to map contents SCope Loom file to FBbt (e.g. by VFB curator), loaded to SCope.  [Example](https://github.com/HumanCellAtlas/matrix_semantic_map/blob/master/src/matrix_semantic_map/test/resources/Desplan_Fly_AdultOpticLobe_map.tsv)
2. ScOPE use mmm to generate a table of permalinks for each cluster  + mapped FBbt term. Table should have headers: dataset_name	fbbt	permalink - ([Example](https://github.com/VirtualFlyBrain/SCOPE_VFB/blob/master/data/Konstantinides_et_al_2018_OpticLobe_semantic_permalinks.tsv)).  Table should be deposited in [data/](https://github.com/VirtualFlyBrain/SCOPE_VFB/tree/master/templates)
3. [src/robot_template_runner.py](https://github.com/VirtualFlyBrain/SCOPE_VFB/blob/master/src/robot_template_runner.py) used to generate robot template deposited in [templates/](https://github.com/VirtualFlyBrain/SCOPE_VFB/tree/master/templates).
4. VFB.owl Jenkins build uses templates to generate xres in OWL and merges thse into into VFB.owl, which the VFB build pipeline combines withe Site Nodes to generate linkouts turns into linkouts.

Note - we could cut out step 3 and just have SCope generate the Robot template directly (step 4).
