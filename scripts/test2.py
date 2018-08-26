#!/usr/bin/env python

#Load model:
import cobra
model = cobra.io.read_sbml_model('../model.xml')

#Make changes:
model.metabolites[1].formula = 'C3H4O7P'
model.metabolites[2].formula = 'C3H4O7P'
model.metabolites[3].formula = 'C6H10O10P'

#Save model:
cobra.io.write_sbml_model(model,'../model.xml')
