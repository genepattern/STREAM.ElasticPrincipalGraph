#!/usr/bin/env python
# -*- coding: utf-8 -*-

import warnings

warnings.filterwarnings('ignore')

__tool_name__='STREAM'
print('''
   _____ _______ _____  ______          __  __ 
  / ____|__   __|  __ \|  ____|   /\   |  \/  |
 | (___    | |  | |__) | |__     /  \  | \  / |
  \___ \   | |  |  _  /|  __|   / /\ \ | |\/| |
  ____) |  | |  | | \ \| |____ / ____ \| |  | |
 |_____/   |_|  |_|  \_\______/_/    \_\_|  |_|
... Elastic Principal Graph                                               
''',flush=True)

import stream as st
import argparse
import multiprocessing
import os
from slugify import slugify
import networkx as nx
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import sys

mpl.use('Agg')
mpl.rc('pdf', fonttype=42)

os.environ['KMP_DUPLICATE_LIB_OK']='True'


print('- STREAM Single-cell Trajectory Reconstruction And Mapping -',flush=True)
print('Version %s\n' % st.__version__,flush=True)
    

def main():
    sns.set_style('white')
    sns.set_context('poster')
    parser = argparse.ArgumentParser(description='%s Parameters' % __tool_name__ ,formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-m", "--data-file", dest="input_filename",default = None, help="input file name, pkl format from Stream preprocessing module", metavar="FILE")
    parser.add_argument("-of","--of",dest="output_filename_prefix", default="StreamiFSOutput",  help="output file name prefix")


    parser.add_argument("-epg_n_nodes",dest="epg_n_nodes", type=int, default=50, help="")
    parser.add_argument("-incr_n_nodes",dest="incr_n_nodes", type=int, default=30, help="")
    parser.add_argument("-epg_trimmingradius",dest="epg_trimmingradius",  default='Inf', help="")
    parser.add_argument("-epg_alpha",dest="epg_alpha", type=float, default=0.02, help="")
    parser.add_argument("-epg_beta",dest="epg_beta", type=float, default=0.0, help="")
    parser.add_argument("-epg_n_processes",dest="epg_n_processes", type=int, default=1, help="")
    parser.add_argument("-epg_lambda",dest="epg_lambda", type=float, default=0.02, help="")
    parser.add_argument("-epg_mu",dest="epg_mu", type=float, default=0.1, help="")
    parser.add_argument("-epg_finalenergy",dest="epg_finalenergy",  default='Penalized', help="")
   
 
    parser.add_argument("-comp1",dest="comp1", type = int, default=0,  help="")   
    parser.add_argument("-comp2",dest="comp2", type = int, default=1,  help="")      
    parser.add_argument("-n_comp",dest="n_comp", type = int, default=3,  help="")      
    parser.add_argument("-fig_name",dest="fig_name",  default=None, help="")
    parser.add_argument("-fig_width",dest="fig_width", type=int, default=8, help="")        
    parser.add_argument("-fig_height",dest="fig_height", type=int, default=8, help="")
    parser.add_argument("-fig_legend_ncol",dest="fig_legend_ncol", type=int, default=None, help="")                                   


    args = parser.parse_args()
    
    workdir = "./"

    adata = st.read(file_name=args.input_filename, file_format='pkl', experiment='rna-seq', workdir=workdir)

    st.elastic_principal_graph(adata,epg_n_nodes=args.epg_n_nodes,incr_n_nodes=args.incr_n_nodes,epg_trimmingradius=args.epg_trimmingradius,epg_alpha=args.epg_alpha, epg_n_processes=args.epg_n_processes, epg_lambda=args.epg_lambda,epg_mu=args.epg_mu, epg_beta=args.epg_beta, epg_finalenergy=args.epg_finalenergy)
    
    st.plot_branches(adata, n_components=args.n_comp, comp1=args.comp1, comp2=args.comp2, save_fig=True, fig_name=(args.output_filename_prefix +'branches.png'), fig_path=None,fig_size=(args.fig_width, args.fig_height))
    st.plot_branches_with_cells(adata,n_components=args.n_comp,comp1=args.comp1,comp2=args.comp2, save_fig=True,fig_name=(args.output_filename_prefix +'branches_with_cells.png'),fig_path=None,fig_size=(args.fig_width, args.fig_height),fig_legend_ncol=args.fig_legend_ncol)

    st.write(adata,file_name=(args.output_filename_prefix + '_stream_result.pkl'),file_path='./',file_format='pkl') 

    print('Finished computation.')

if __name__ == "__main__":
    main()
