import pandas as pd
import torch

l1 = torch.load(('./cora_semi_gcn.pt'))
l2 = torch.load(('./cora_full_gcn.pt'))
l3 = torch.load(('./citeseer_semi_gcn.pt'))
l4 = torch.load(('./citeseer_full_gcn.pt'))
l5 = torch.load(('./pubmed_semi_gcn.pt'))
l6 = torch.load(('./pubmed_full_gcn.pt'))

d1 = pd.DataFrame({'cora_semi':l1,
                    'cora_full':l2,
                    'citeseer_semi':l3,
                    'citeseer_full':l4,
                    'pubmed_semi':l5,
                    'pubmed_full':l6})

#l could be list or array

writer = pd.ExcelWriter('./gcn_results.xlsx')
d1.to_excel(writer)
writer.save()
