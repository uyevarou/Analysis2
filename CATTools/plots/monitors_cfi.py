
monitors = [
  { "name":"Stat",         "unit":"Stat ",                         "var":"met",       "xbin_set":[1,0,10000]  },
  { "name":"nGoodPV",      "unit":"# of vertex ",             "var":"nvertex",   "xbin_set":[30,0,30]    },
#]
#fff=[
  { "name":"Weight",         "unit":"Weight",             "var":"weight",      "xbin_set":[50,0,10]    },
  { "name":"PuWeight",       "unit":"PuWeight",             "var":"puweight",    "xbin_set":[50,0,10]    },
  { "name":"LepWeight",      "unit":"LepWeight",             "var":"lepweight",   "xbin_set":[50,0,10]    },
  { "name":"CsvWeight",      "unit":"CSVWeight",             "var":"csvweight",   "xbin_set":[50,0,10]    },

#]
#fff=[
  { "name":"MET",          "unit":"Missing E_{T} (GeV)","var":"met",   "xbin_set":[30,0,300]  },
#  { "name":"METpf",        "unit":"Missing E_{T}  (GeV)",          "var":"met",       "xbin_set":[60,0,300]  },
  { "name":"ZMass",        "unit":"Dilepton mass (GeV/c^{2}) ",    "var":"ll_m",  "xbin_set":[60,0,300]  },


  { "name":"METPHI",       "unit":"Missing E_{T} without HF #phi", "var":"metphi","xbin_set":[20,-4,4]    },
#  { "name":"METmva",       "unit":"MVA Missing E_{T}  (GeV)",      "var":"metPfMva",  "xbin_set":[60,0,300]  },
#  { "name":"METPuppi",     "unit":"Puppi Missing E_{T}  (GeV)",    "var":"metPuppi",   "xbin_set":[60,0,300]  },
#  { "name":"nBJet20L",       "unit":"b-Jet20 multiplicity loose ",     "var":"nBJet20L",    "xbin_set":[8,0,8]      },
#  { "name":"nBJet20M",       "unit":"b-Jet20 multiplicity medium ",    "var":"nBJet20M",    "xbin_set":[6,0,6]      },
#  { "name":"NJet20",         "unit":"Jet20 multiplicity ",             "var":"nJet20",      "xbin_set":[10,0,10]    },
#  { "name":"nBJet20T",       "unit":"b-Jet20 multiplicity tight ",     "var":"nBJet20T",    "xbin_set":[6,0,6]      },
  { "name":"nBJet30L",       "unit":"b-Jet30 multiplicity loose ",     "var":"nbjetL30",    "xbin_set":[8,0,8]      },
  { "name":"nBJet30M",       "unit":"b-Jet30 multiplicity medium ",    "var":"nbjetM30",    "xbin_set":[6,0,6]      },
  { "name":"NJet30",         "unit":"Jet30 multiplicity ",             "var":"njet30",      "xbin_set":[10,0,10]    },
  { "name":"nBJet30T",       "unit":"b-Jet30 multiplicity tight ",     "var":"nbjetT30",    "xbin_set":[6,0,6]      },
  { "name":"lep1Pt",       "unit":"Leading lepton p_{T} (GeV/c) ", "var":"lep1_pt", "xbin_set":[20,0,200] },
  { "name":"lep2Pt",       "unit":"Sceond  lepton p_{T} (GeV/c) ", "var":"lep2_pt", "xbin_set":[20,0,200] },
  { "name":"lep1Eta",      "unit":"Leading lepton #eta ",          "var":"lep1_eta", "xbin_set":[10,-3,3] },
  { "name":"lep2Eta",      "unit":"Sceond  lepton #eta ",          "var":"lep2_eta", "xbin_set":[10,-3,3] },
#  { "name":"lep1Phi",      "unit":"Leading lepton #phi ",          "var":"lep1_phi", "xbin_set":[40,-4,4] },
#  { "name":"lep2Phi",      "unit":"Sceond  lepton #phi ",          "var":"lep2_phi", "xbin_set":[40,-4,4] },
  { "name":"lep1Iso",      "unit":"Leading lepton Iso_{rel} ",     "var":"lep1_RelIso", "xbin_set":[20,0,1] },
  { "name":"lep2Iso",      "unit":"Sceond  lepton Iso_{rel} ",     "var":"lep2_RelIso", "xbin_set":[20,0,1] },
  { "name":"jet1Pt",      "unit":"p_T of 1st leading Jet ",      "var":"jets_pt[csvd_jetid[0]]",    "xbin_set":[40,0,400]   },
  { "name":"jet2Pt",      "unit":"p_T of 2nd leading Jet ",      "var":"jets_pt[csvd_jetid[1]]",    "xbin_set":[40,0,400]   },
  { "name":"jet3Pt",      "unit":"p_T of 3rd leading Jet ",      "var":"jets_pt[csvd_jetid[2]]",    "xbin_set":[40,0,400]   },
  { "name":"jet4Pt",      "unit":"p_T of 4th leading Jet ",      "var":"jets_pt[csvd_jetid[3]]",    "xbin_set":[40,0,400]   },
  { "name":"jet1Eta",      "unit":"#eta of 1st leading Jet ",      "var":"jets_eta[csvd_jetid[0]]",    "xbin_set":[10,-3,3]   },
  { "name":"jet2Eta",      "unit":"#eta of 2nd leading Jet ",      "var":"jets_eta[csvd_jetid[1]]",    "xbin_set":[10,-3,3]   },
  { "name":"jet3Eta",      "unit":"#eta of 3rd leading Jet ",      "var":"jets_eta[csvd_jetid[2]]",    "xbin_set":[10,-3,3]   },
  { "name":"jet4Eta",      "unit":"#eta of 4th leading Jet ",      "var":"jets_eta[csvd_jetid[3]]",    "xbin_set":[10,-3,3]   },
  { "name":"jet1Phi",      "unit":"#phi of 1st leading Jet ",      "var":"jets_phi[csvd_jetid[0]]",    "xbin_set":[10,-4,4]   },
  { "name":"jet2Phi",      "unit":"#phi of 2nd leading Jet ",      "var":"jets_phi[csvd_jetid[1]]",    "xbin_set":[10,-4,4]   },
  { "name":"jet3Phi",      "unit":"#phi of 3rd leading Jet ",      "var":"jets_phi[csvd_jetid[2]]",    "xbin_set":[10,-4,4]   },
  { "name":"jet4Phi",      "unit":"#phi of 4th leading Jet ",      "var":"jets_phi[csvd_jetid[3]]",    "xbin_set":[10,-4,4]   },

  { "name":"jet1CSV",     "unit":"CSVv2 of 1st leading Jet ",     "var":"jets_bDiscriminatorCSV[csvd_jetid[0]]",   "xbin_set":[10,0,1]     },
  { "name":"jet2CSV",     "unit":"CSVv2 of 2nd leading Jet ",     "var":"jets_bDiscriminatorCSV[csvd_jetid[1]]",   "xbin_set":[10,0,1]     },
  { "name":"jet3CSV",     "unit":"CSVv2 of 3rd leading Jet ",     "var":"jets_bDiscriminatorCSV[csvd_jetid[2]]",   "xbin_set":[10,0,1]     },
  { "name":"jet4CSV",     "unit":"CSVv2 of 4th leading Jet ",     "var":"jets_bDiscriminatorCSV[csvd_jetid[3]]",   "xbin_set":[10,0,1]     },

  { "name":"jet1Ptpt",      "unit":"p_T of 1st leading Jet ",      "var":"jets_pt[0]",    "xbin_set":[40,0,400]   },
  { "name":"jet2Ptpt",      "unit":"p_T of 2nd leading Jet ",      "var":"jets_pt[1]",    "xbin_set":[40,0,400]   },
  { "name":"jet3Ptpt",      "unit":"p_T of 3rd leading Jet ",      "var":"jets_pt[2]",    "xbin_set":[40,0,400]   },
  { "name":"jet4Ptpt",      "unit":"p_T of 4th leading Jet ",      "var":"jets_pt[3]",    "xbin_set":[40,0,400]   },
 
  { "name":"jet1CSVpt",     "unit":"CSVv2 of 1st leading Jet ",     "var":"jets_bDiscriminatorCSV[0]",   "xbin_set":[10,0,1]     },
  { "name":"jet2CSVpt",     "unit":"CSVv2 of 2nd leading Jet ",     "var":"jets_bDiscriminatorCSV[1]",   "xbin_set":[10,0,1]     },
  { "name":"jet3CSVpt",     "unit":"CSVv2 of 3rd leading Jet ",     "var":"jets_bDiscriminatorCSV[2]",   "xbin_set":[10,0,1]     },
  { "name":"jet4CSVpt",     "unit":"CSVv2 of 4th leading Jet ",     "var":"jets_bDiscriminatorCSV[3]",   "xbin_set":[10,0,1]     },


#  { "name":"jetPP1CSV",   "unit":"CSV2 of 1st leading JetPuppi ",     "var":"jetPuppi_csv[0]",   "xbin_set":[20,0,1]     },
#  { "name":"jetPP2CSV",   "unit":"CSV2 of 2nd leading JetPuppi ",     "var":"jetPuppi_csv[1]",   "xbin_set":[20,0,1]     },
#  { "name":"jetPP3CSV",   "unit":"CSV2 of 3rd leading JetPuppi ",     "var":"jetPuppi_csv[2]",   "xbin_set":[20,0,1]     },
#  { "name":"jetPP4CSV",   "unit":"CSV2 of 4th leading JetPuppi ",     "var":"jetPuppi_csv[3]",   "xbin_set":[20,0,1]     },
#  { "name":"jetPP1Pt",      "unit":"p_T of 1st leading JetPuppi ",      "var":"jetPuppi_pt[0]",    "xbin_set":[40,0,400]   },
#  { "name":"jetPP2Pt",      "unit":"p_T of 2nd leading JetPuppi ",      "var":"jetPuppi_pt[1]",    "xbin_set":[40,0,400]   },
#  { "name":"jetPP3Pt",      "unit":"p_T of 3rd leading JetPuppi ",      "var":"jetPuppi_pt[2]",    "xbin_set":[40,0,400]   },
#  { "name":"jetPP4Pt",      "unit":"p_T of 4th leading JetPuppi ",      "var":"jetPuppi_pt[3]",    "xbin_set":[40,0,400]   },
#  { "name":"nBJet20LPuppi",       "unit":"b-Jet20Puppi multiplicity loose ",     "var":"nBJet20LPuppi",    "xbin_set":[8,0,8]      },
#  { "name":"nBJet20MPuppi",       "unit":"b-Jet20Puppi multiplicity medium ",    "var":"nBJet20MPuppi",    "xbin_set":[6,0,6]      },
#  { "name":"NJet20Puppi",         "unit":"Jet20Puppi multiplicity ",             "var":"nJet20Puppi",      "xbin_set":[10,0,10]    },
#  { "name":"nBJet20TPuppi",       "unit":"b-Jet20Puppi multiplicity tight ",     "var":"nBJet20TPuppi",    "xbin_set":[6,0,6]      },
#  { "name":"nBJet30LPuppi",       "unit":"b-Jet30Puppi multiplicity loose ",     "var":"nBJet30LPuppi",    "xbin_set":[8,0,8]      },
#  { "name":"nBJet30MPuppi",       "unit":"b-Jet30Puppi multiplicity medium ",    "var":"nBJet30MPuppi",    "xbin_set":[6,0,6]      },
#  { "name":"NJet30Puppi",         "unit":"Jet30Puppi multiplicity ",             "var":"nJet30Puppi",      "xbin_set":[10,0,10]    },
#  { "name":"nBJet30TPuppi",       "unit":"b-Jet30Puppi multiplicity tight ",     "var":"nBJet30TPuppi",    "xbin_set":[6,0,6]      },
#  { "name":"Nlep",        "unit":"number of lepton ",            "var":"lepton_N",     "xbin_set":[5,0,5]    },
#  { "name":"Nmu",         "unit":"number of muon ",              "var":"Nmu",          "xbin_set":[5,0,5]    },
#  { "name":"NmuIso",      "unit":"number of muon ",              "var":"NmuIso",       "xbin_set":[5,0,5]    },
#  { "name":"Nel",         "unit":"number of electron ",          "var":"Nel",          "xbin_set":[5,0,5]    },
#  { "name":"NelIso",      "unit":"number of electron ",          "var":"NelIso",       "xbin_set":[5,0,5]    },
]
#"""
MN2 = len(monitors)
monitors2d = {
#"Mon1" : [
#  { "name":"jet1CSV",     "unit":"CSV2 of 1st leading Jet ",     "var":"jets_bDiscriminatorCSV[0]",   "xbin_set":[20,0,1]     },
#  { "name":"jet2CSV",     "unit":"CSV2 of 2nd leading Jet ",     "var":"jets_bDiscriminatorCSV[1]",   "xbin_set":[20,0,1]     },
#],
("Mon%d"%MN2) : [
  { "name":"jet3CSV",     "unit":"CSV2 of 3rd leading Jet ",     "var":"jets_bDiscriminatorCSV[csvd_jetid[2]]",   "xbin_set":[10,0,1]     },
  { "name":"jet4CSV",     "unit":"CSV2 of 4th leading Jet ",     "var":"jets_bDiscriminatorCSV[csvd_jetid[3]]",   "xbin_set":[10,0,1]     },
],
#"Mon27" : [
#  { "name":"NJet",        "unit":"Jet multiplicity ",             "var":"nJet",     "xbin_set":[10,0,10]    },
#  { "name":"nBJetL",      "unit":"b-Jet multiplicity loose ",     "var":"nBJetL",   "xbin_set":[8,0,8]      },
#  { "name":"nBJetM",      "unit":"b-Jet multiplicity medium ",    "var":"nBJetM",   "xbin_set":[8,0,8]      },
#  { "name":"nBJetT",      "unit":"b-Jet multiplicity tight ",     "var":"nBJetT",   "xbin_set":[8,0,8]      },
#],
#"Mon27" : [
#  { "name":"NJet",        "unit":"Jet multiplicity ",            "var":"nJet",         "xbin_set":[10,0,10]    },
#  { "name":"genNJet",     "unit":"genJet multiplicity ",         "var":"NgenJet",      "xbin_set":[10,0,10]    },
#  { "name":"Category",    "unit":"Category ",                    "var":"Category",     "xbin_set":[5,0,5]      },
#],
#"Mon28" : [
##  { "name":"Nmu",         "unit":"number of muon ",              "var":"Nmu",          "xbin_set":[5,0,5]    },
#  { "name":"NmuIso",      "unit":"number of muon ",              "var":"NmuIso",       "xbin_set":[5,0,5]    },
##  { "name":"Nel",         "unit":"number of electron ",          "var":"Nel",          "xbin_set":[5,0,5]    },
#  { "name":"NelIso",      "unit":"number of electron ",          "var":"NelIso",       "xbin_set":[5,0,5]    },
#],
}
