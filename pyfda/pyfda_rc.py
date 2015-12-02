# -*- coding: utf-8 -*-
"""
pyfda_rc.py

This file contains layout definitions for Qt and matplotlib widgets
A dark and a light theme can be selected via a constant but this more a demonstration
on how to set things than a finished layout yet.

Default parameters, paths etc. are also defined at the end of the file.

Importing pyfda_rc runs the module once, defining all module variables
which are global (similar to class variables).

See
http://stackoverflow.com/questions/13034496/using-global-variables-between-files-in-python
http://pymotw.com/2/articles/data_persistence.html
for information on passing/storing data between files

See
http://doc.qt.io/qt-4.8/stylesheet-examples.html
http://www.informit.com/articles/article.aspx?p=1405556
for qss styling

Author: Christian Muenker
"""

from __future__ import division, unicode_literals
import os, logging


logging.basicConfig(format='%(levelname)s: %(name)s: \n\t%(message)s', 
                    level=logging.DEBUG)
handler = logging.FileHandler('logging.log')

logger = logging.getLogger(__name__)
logger.addHandler(handler)

THEME = 'light'

# -----------------------------
# Layout for matplotlib widgets
# -----------------------------

# dark theme
mpl_dark = {'axes.facecolor':'black',
            'axes.labelcolor':'white',
            'axes.edgecolor':'white',
            'axes.color_cycle': ['r', 'g', 'c', 'm', 'y', 'w'],
            'figure.facecolor':'#202020',
            'figure.edgecolor':'#808080', # also color for hatched specs in |H(f)|
            'savefig.facecolor':'black',
            'savefig.edgecolor':'black', 
            'xtick.color':'white',
            'ytick.color':'white',
            'text.color':'white',
            'grid.color':'#CCCCCC'
            }
            
# light theme
mpl_light = {'axes.facecolor':'white',
             'axes.labelcolor':'black',
            'axes.edgecolor':'black',
            'axes.color_cycle': ['r', 'b', 'c', 'm', 'k'],
            'figure.facecolor':'white',
            'figure.edgecolor':'#808080', # also color for hatched specs in |H(f)|
            'savefig.facecolor':'white',
            'savefig.edgecolor':'white', 
            'xtick.color':'black',
            'ytick.color':'black',
            'text.color':'black',
            'grid.color':'#222222'
            }
            
# common layout settings
mpl_rc = {'lines.linewidth': 1.5,
            'font.size':12, 'legend.fontsize':12, 
            'axes.labelsize':12, 'axes.titlesize':14, 'axes.linewidth':1,
            'axes.formatter.use_mathtext': True,
            'figure.figsize':(5,4), 'figure.dpi' : 100}
            
# ---------------------
# Layout for Qt widgets
# ---------------------
            
            


# dark theme            
css_dark = """
                QWidget{color:white;background: #222222;}
                
                QLineEdit{background: #222222; color:white;}
                QLineEdit:disabled{background-color:darkgrey;}
                
                QTabWidget#plot_tabs::pane{border-left: 2px dashed grey;}
                
                QPushButton{background-color:grey; color:white;}
                
                QTableView{alternate-background-color:#222222;
                    background-color:black; gridline-color: white;}
                QHeaderView::section{background-color:rgb(190,1,1);color:white}
                
            """
          
          
# light theme /* 
css_light = """ .QWidget{color:black; background: white;}

                QLineEdit{background: white; color:black;}
                QLineEdit:disabled{background-color:lightgrey;}
                
                QTabWidget#plot_tabs::pane{border-left: 2px dashed grey;}
                        
                QPushButton{background-color:lightgrey; color:black;}
                
                QHeaderView::section{background-color:rgb(190,1,1); color:white;}
                
                QGridLayout#plotSpecSelect{border: 3px solid red;}
                QGridLayout{border: 3px solid blue;}
            """




# common layout settings
TabBarCss = """
 QTabWidget::pane { /* The tab widget frame */
     border-top: 2px solid #C2C7CB;
 }
 QTabWidget::tab-bar {
     left: 1px; /* move to the right by 1px */
 }
 
 /* Style the TAB using the tab sub-control. Note that
     it reads QTabBar _not_ QTabWidget */
 QTabBar::tab{color:black;font-size:13px; font-weight:bold;}
 QTabBar::tab {
     background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                        stop: 0 white, stop: 0.5 lightgray, stop: 1.0 #C2C7CB);
     border: 1px solid #C4C4C3;
     border-bottom-color: #C2C7CB; /* same as the pane color */
     border-top-left-radius: 4px;
     border-top-right-radius: 4px;
     min-width: 8ex;
     padding: 2px;
 }
 QTabBar::tab:selected, QTabBar::tab:hover {background:lightblue;}

 QTabBar::tab:selected {
     border-color: #9B9B9B;
     border-bottom-color: #C2C7CB; /* same as pane color */
 }
 QTabBar::tab:!selected {
     margin-top: 2px; /* make non-selected tabs look smaller */
 }
 /* make use of negative margins for overlapping tabs */
 QTabBar::tab:selected {
     /* expand/overlap to the left and right by 4px */
     margin-left: -4px;
     margin-right: -4px;
 }
 QTabBar::tab:first:selected {
     margin-left: 0; /* the first selected tab has nothing to overlap with on the left */
 }
 QTabBar::tab:last:selected {
     margin-right: 0; /* the last selected tab has nothing to overlap with on the right */
 }
 QTabBar::tab:only-one {
     margin: 0; /* if there is only one tab, we don't want overlapping margins */
 }
"""
css_common = """
                *[state="changed"]{background-color:yellow; color:black}
                *[state="error"]{background-color:red; color:white}
                *[state="failed"]{background-color:orange; color:white}
                *[state="ok"]{background-color:green; color:white}
                QPushButton:pressed {background-color:black; color:white}
                
                QWidget{font-size:12px; font-family: Tahoma;}
                QLineEdit{background-color:lightblue;}
            """\
            + TabBarCss


if THEME == 'dark':

    mpl_rc.update(mpl_dark)
    css_rc = css_common + css_dark
else:
    mpl_rc.update(mpl_light)
    css_rc = css_common + css_light
    

# Various parameters for calculation and plotting
params = {'N_FFT':  2048, # number of FFT points for plot commands (freqz etc.)
          'P_Marker': [12, 'r'], # size and color for poles' marker
          'Z_Marker': [12, 'b']} # size and color for zeros' marker

# Dictionary with translations between short method names and long names for
# response types
rt_names = {"LP":"Lowpass", "HP":"Highpass", "BP":"Bandpass",
            "BS":"Bandstop", "AP":"Allpass", "MB":"Multiband",
            "HIL":"Hilbert", "DIFF":"Differentiator"}
            
# Dictionary with translations between short method names and long names for
# response types
ft_names = {"IIR":"IIR", "FIR":"FIR"}

# Dictionary dm_names is created dynamically by FilterTreeBuilder and stored
# in filterbroker.py


# the basedir can be stored and referenced by all files
base_dir = os.path.dirname(os.path.abspath(__file__))
save_dir = "D:/Daten1"

if not os.path.exists(save_dir):
    logger.warning('Specified save_dir "%s" doesn\'t exist, using "%s" instead.'
        %(save_dir, base_dir ))
    save_dir = base_dir

            
################## Some layout ideas ##########################################

#self.em = QtGui.QFontMetricsF(QtGui.QLineEdit.font()).width('m')

#          'QWidget':('QWidget{Background: #CCCCCC; color:black; font-size:14px;'
#                     'font-weight:bold; border-radius: 1px;}')
#                /* all QWidget instances that are direct children of QTabWidget: */
#                /* QTabWidget>QWidget{border-left: } */
#                /* only QTabWidget with object name "plot_tabs" */
#                QTabWidget#plot_tabs::pane{border-left: 2px dashed grey;}
#                /* only match QWidget, not subclasses: */
#                .QWidget{color:black; background: white;}



""" QTabBar::tab:selected, QTabBar::tab:hover {
     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                 stop: 0 #fafafa, stop: 0.4 #f4f4f4,
                                 stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);
 QTabBar::tab {
     background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
 }
"""
css = """
/*height: 14px;*/
/*
QDialog{
Background-image:url('img/xxx.png');
font-size:14px;
color: black;
}
*/


QToolButton:hover{
Background: #DDEEFF;
}
"""
