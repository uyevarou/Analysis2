import FWCore.ParameterSet.Config as cms
pileupMap = {
#pileupCalc.py -i Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/PileUp/pileup_latest.txt --calcMode true --minBiasXsec 69000 --maxPileupBin 50 --numPileupBins 50 PileUpData.root 
"Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON":cms.vdouble(
1.220587e+05,5.831995e+05,8.283072e+05,1.195209e+06,2.112880e+06,
4.961396e+06,1.551333e+07,6.006134e+07,1.649140e+08,2.803063e+08,
3.620212e+08,3.869629e+08,3.411577e+08,2.426751e+08,1.388794e+08,
6.531371e+07,2.692979e+07,1.135401e+07,5.679176e+06,3.030398e+06,
1.402960e+06,5.120442e+05,1.467754e+05,3.530236e+04,8.271279e+03,
2.235610e+03,7.213805e+02,2.588496e+02,9.727087e+01,3.687161e+01,
1.372748e+01,4.931712e+00,1.692408e+00,5.518936e-01,1.706013e-01,
4.993580e-02,1.383391e-02,3.626617e-03,8.996063e-04,2.111484e-04,
4.689276e-05,9.853920e-06,1.959294e-06,3.686198e-07,6.562482e-08,
1.105342e-08,1.762478e-09,2.614969e-10,4.768003e-11,0.000000e+00,
),
#pileupCalc.py -i Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/PileUp/pileup_latest.txt --calcMode true --minBiasXsec 72450 --maxPileupBin 50 --numPileupBins 50 PileUpData_Up.root 
"Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_Up":cms.vdouble(
1.029516e+05,5.286883e+05,7.668740e+05,1.061053e+06,1.735315e+06,
3.657311e+06,9.973390e+06,3.526300e+07,1.114776e+08,2.196883e+08,
3.115377e+08,3.636366e+08,3.592381e+08,2.952095e+08,1.988841e+08,
1.103235e+08,5.170482e+07,2.197805e+07,9.831562e+06,5.166228e+06,
2.836901e+06,1.361640e+06,5.264128e+05,1.630398e+05,4.259070e+04,
1.058456e+04,2.923748e+03,9.556848e+02,3.513003e+02,1.367717e+02,
5.431361e+01,2.142533e+01,8.238738e+00,3.051831e+00,1.081840e+00,
3.657705e-01,1.177607e-01,3.607632e-02,1.051327e-02,2.914007e-03,
7.681742e-04,1.925918e-04,4.592234e-05,1.041407e-05,2.246101e-06,
4.607372e-07,8.988719e-08,1.667630e-08,2.942386e-09,4.960389e-10,
),
#pileupCalc.py -i Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/PileUp/pileup_latest.txt --calcMode true --minBiasXsec 68827 --maxPileupBin 50 --numPileupBins 50 PileUpData_Dn.root 
"Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_Dn":cms.vdouble(
1.230562e+05,5.861159e+05,8.317676e+05,1.202910e+06,2.135561e+06,
5.044260e+06,1.589329e+07,6.168769e+07,1.679286e+08,2.834574e+08,
3.644021e+08,3.876037e+08,3.394957e+08,2.395611e+08,1.358982e+08,
6.337816e+07,2.600405e+07,1.099952e+07,5.532071e+06,2.939116e+06,
1.343685e+06,4.827610e+05,1.362991e+05,3.246134e+04,7.612338e+03,
2.075276e+03,6.739759e+02,2.423396e+02,9.099397e+01,3.439010e+01,
1.274402e+01,4.551673e+00,1.551656e+00,5.023785e-01,1.541240e-01,
4.475778e-02,1.229815e-02,3.196763e-03,7.860559e-04,1.828352e-04,
4.022806e-05,8.372651e-06,1.648401e-06,3.070010e-07,5.408534e-08,
9.014751e-09,1.417573e-09,2.107582e-10,3.776435e-11,0.000000e+00,
),
}