from dash import Dash, html, dcc, Output, Input, callback
import pandas as pd
import numpy as np
import plotly.express as px
import dash_bootstrap_components as dbc

candidates = pd.read_csv("C:/Users/niluf/OneDrive/Desktop/ETH/Semester 4/Thesis/Data/candidates.csv")
candidates = candidates.loc[candidates['elected'] == 1]

voting_data = pd.read_excel("C:/Users/niluf/OneDrive/Desktop/ETH/Semester 4/Thesis/Data/State People.xlsx")
voting_data = voting_data.drop(columns=['Member of', 'Smart Map X', 'Smart Map Y'])
voting_data.columns = ['vote_' + str(col) for col in voting_data.columns]
voting_data = voting_data.rename(columns={'vote_Name': 'full_name'})

for col in ['vote_22.476', 'vote_22.486', 'vote_23.420', 'vote_22.4447', 'vote_22.466', 'vote_22.469', 'vote_22.472',
            'vote_22.2011', 'vote_21.474', 'vote_21.521', 'vote_21.531', 'vote_22.043', 'vote_22.3606']:
    voting_data[col] = voting_data[col].map({'Yes':'No', 'No':'Yes'})

required_columns = ['full_name', 'age', 'cleavage_1', 'cleavage_2', 'cleavage_3', 'cleavage_4', 
                    'cleavage_5', 'cleavage_6', 'cleavage_7', 'cleavage_8', 'smartmap_x', 'smartmap_y',]

final_data = pd.merge(candidates[required_columns], voting_data, on='full_name')

referendums = ['vote_22.476', 'vote_22.486', 'vote_22.4447', 'vote_22.4497',
'vote_23.3101', 'vote_23.3300', 'vote_23.3346', 'vote_23.3501', 'vote_23.3850', 'vote_22.466', 'vote_22.469', 'vote_22.472',
'vote_22.3329', 'vote_22.4208', 'vote_23.3017', 'vote_22.3248', 'vote_21.4283', 'vote_21.4660', 'vote_22.3456', 'vote_22.4270', 
'vote_22.4275', 'vote_21.531', 'vote_22.043', 'vote_22.404', 'vote_22.3606', 'vote_22.3610', 'vote_22.3889', 'vote_21.4606', 
'vote_22.3055', 'vote_22.3870', 'vote_22.3793', 'vote_22.3577', 'vote_22.3202', 'vote_22.3872']

inaccurates_agent = {
    '21.531': ['Barbara Schaffner', 'Beat Flach', 'Benjamin Roduit', 'Christian Lohr', 'Christine Bulliard-Marbach', 'Gerhard Pfister', 'Jean-Luc Addor', 'Jürg Grossen', 'Kathrin Bertschy', 'Katja Christ', 'Laurent Wehrli', 'Leo Müller', 'Marc Jost', 'Marie-France Roth Pasquier', 'Markus Ritter', 'Priska Wismer-Felder', 'Sidney Kamerzin', 'Simon Stadler', 'Stefan Müller-Altermatt', 'Vincent Maitre'],
    '21.4283': ['Andreas Glarner', 'Barbara Schaffner', 'Beat Flach', 'Céline Weber', 'Christian Wasserfallen', 'Christine Bulliard-Marbach', 'Martin Bäumle', 'Martina Bircher', 'Priska Wismer-Felder', 'Stefanie Heimgartner', 'Vincent Maitre'],
    '21.4405': ['Barbara Schaffner', 'Beat Flach', 'Benjamin Roduit', 'Christian Lohr', 'Christine Bulliard-Marbach', 'Corina Gredig', 'Gerhard Pfister', 'Kathrin Bertschy', 'Lorenz Hess', 'Lukas Reimann', 'Marc Jost', 'Marie-France Roth Pasquier', 'Nik Gugger', 'Priska Wismer-Felder'],
    '21.4426': [],
    '21.4533': [],
    '21.4549': [],
    '21.4606': ['Alex Farinelli', 'Andri Silberschmidt', 'Anna Giacometti', 'Beat Walti', 'Benjamin Roduit', 'Bruno Walliser', 'Céline Amaudruz', 'Christian Lohr', 'Christian Wasserfallen', 'Christine Bulliard-Marbach', 'Damien Cottier', 'Daniela Schneeberger', 'Diana Gutjahr', 'Franz Grüter', 'Jacques Nicolet', 'Jean-Luc Addor', 'Laurent Wehrli', 'Leo Müller', 'Lorenzo Quadri', 'Maja Riniker', 'Markus Ritter', 'Nicolò Paganini', 'Patricia von Falkenstein', 'Peter Schilliger', 'Philipp Matthias Bregy', 'Philippe Nantermod', 'Piero Marchesi', 'Regine Sauter', 'Sidney Kamerzin', 'Simon Stadler', 'Simone de Montmollin', 'Susanne Vincenz-Stauffacher'],
    '21.4660': ['Alex Farinelli', 'Andreas Gafner', 'Andreas Glarner', 'Andri Silberschmidt', 'Anna Giacometti', 'Beat Walti', 'Benjamin "Beni" Fischer', 'Benjamin Giezendanner', 'Bruno Walliser', 'Céline Amaudruz', 'Christian Imark', 'Damien Cottier', 'Daniela Schneeberger','Erich Hess', 'Franz Grüter', 'Gregor Rutz', 'Jacques Nicolet', 'Jean-Luc Addor', 'Lars Guggisberg', 'Lorenz Hess', 'Lukas Reimann', 'Maja Riniker', 'Manuel Strupler', 'Marcel Dettling', 'Michael Graber', 'Mike Egger', 'Monika Rüegger-Hurschler', 'Nik Gugger', 'Patricia von Falkenstein', 'Peter Schilliger', 'Philippe Nantermod', 'Piero Marchesi', 'Pierre-André Page', 'Regine Sauter', 'Sandra Sollberger', 'Stefanie Heimgartner', 'Susanne Vincenz-Stauffacher', 'Thomas Burgherr', 'Thomas de Courten'],
    '22.043': ['Benjamin Roduit', 'Christian Lohr', 'Gerhard Pfister', 'Jean-Luc Addor', 'Jon Pult', 'Kathrin Bertschy', 'Katja Christ', 'Laurent Wehrli', 'Leo Müller', 'Lorenz Hess', 'Marc Jost', 'Marie-France Roth Pasquier', 'Markus Ritter', 'Sidney Kamerzin', 'Simon Stadler', 'Simone de Montmollin', 'Stefan Müller-Altermatt', 'Vincent Maitre'],
    '22.404': ['Alex Farinelli', 'Céline Amaudruz', 'Christine Bulliard-Marbach', 'Daniela Schneeberger', 'Elisabeth Schneider-Schneiter', 'Gerhard Pfister', 'Hans-Peter Portmann', 'Jean-Luc Addor', 'Laurent Wehrli', 'Maja Riniker', 'Markus Ritter', 'Matthias Samuel Jauslin', 'Peter Schilliger', 'Susanne Vincenz-Stauffacher'],
    '22.466': ['Andri Silberschmidt', 'Anna Giacometti', 'Barbara Schaffner', 'Beat Flach', 'Céline Weber', 'Corina Gredig', 'Damien Cottier', 'Elisabeth Schneider-Schneiter', 'Kathrin Bertschy', 'Katja Christ', 'Laurent Wehrli', 'Maja Riniker', 'Marc Jost', 'Marie-France Roth Pasquier', 'Matthias Samuel Jauslin', 'Melanie Mettler', 'Nicolò Paganini', 'Nik Gugger', 'Patricia von Falkenstein', 'Philipp Matthias Bregy', 'Philippe Nantermod', 'Priska Wismer-Felder', 'Regine Sauter', 'Simon Stadler', 'Simone de Montmollin', 'Stefan Müller-Altermatt', 'Susanne Vincenz-Stauffacher', 'Vincent Maitre'],
    '22.469': ['Barbara Schaffner', 'Beat Flach', 'Benjamin Roduit', 'Céline Weber', 'Christian Lohr', 'Corina Gredig', 'Elisabeth Schneider-Schneiter', 'Gerhard Pfister', 'Katja Christ', 'Markus Ritter', 'Melanie Mettler', 'Nicolò Paganini', 'Philipp Matthias Bregy', 'Priska Wismer-Felder', 'Simon Stadler', 'Stefan Müller-Altermatt', 'Thomas Rechsteiner'],
    '22.472': ['Benjamin Roduit', 'Bruno Walliser', 'Christine Bulliard-Marbach', 'Jacques Nicolet', 'Jean-Luc Addor', 'Jon Pult', 'Laurent Wehrli', 'Marie-France Roth Pasquier', 'Markus Ritter', 'Melanie Mettler', 'Philipp Matthias Bregy', 'Priska Wismer-Felder', 'Sidney Kamerzin', 'Simon Stadler', 'Stefan Müller-Altermatt', 'Vincent Maitre'],
    '22.476': ['Alex Farinelli', 'Barbara Schaffner', 'Beat Flach', 'Benjamin Roduit', 'Christian Lohr', 'Christine Bulliard-Marbach', 'Katja Christ', 'Leo Müller', 'Marc Jost', 'Marie-France Roth Pasquier', 'Markus Ritter', 'Melanie Mettler', 'Priska Wismer-Felder', 'Sidney Kamerzin', 'Stefan Müller-Altermatt'], 
    '22.486': ['Alex Farinelli', 'Alfred "Fredi" Heer', 'Andreas Gafner', 'Andri Silberschmidt', 'Anna Giacometti', 'Barbara Steinemann', 'Beat Walti', 'Benjamin "Beni" Fischer', 'Benjamin Giezendanner', 'Benjamin Roduit', 'Bruno Walliser', 'Céline Weber', 'Christian Lohr', 'Christian Wasserfallen', 'Christine Bulliard-Marbach', 'Damien Cottier', 'Daniela Schneeberger', 'Diana Gutjahr', 'Elisabeth Schneider-Schneiter', 'Laurent Wehrli', 'Lorenz Hess',  'Marie-France Roth Pasquier', 'Priska Wismer-Felder', 'Susanne Vincenz-Stauffacher'],
    '22.3055': ['Anna Giacometti', 'Céline Weber', 'Corina Gredig', 'Jürg Grossen', 'Katja Christ', 'Marie-France Roth Pasquier', 'Martin Bäumle', 'Simon Stadler'],
    '22.3202': ['Alex Farinelli', 'Andri Silberschmidt', 'Anna Giacometti', 'Barbara Schaffner', 'Beat Flach', 'Beat Walti', 'Benjamin Roduit', 'Céline Weber',  'Christian Lohr', 'Christian Wasserfallen', 'Corina Gredig', 'Damien Cottier', 'Daniela Schneeberger', 'Hans-Peter Portmann', 'Kathrin Bertschy', 'Katja Christ', 'Laurent Wehrli', 'Leo Müller', 'Lorenz Hess', 'Maja Riniker', 'Markus Ritter', 'Martin Bäumle', 'Matthias Samuel Jauslin', 'Nicolò Paganini', 'Patricia von Falkenstein', 'Peter Schilliger', 'Philipp Matthias Bregy', 'Philippe Nantermod', 'Simon Stadler', 'Simone de Montmollin', 'Susanne Vincenz-Stauffacher',  'Thomas "Tommy" Matter', 'Thomas Rechsteiner', 'Vincent Maitre'],
    '22.3248': ['Benjamin Roduit', 'Christian Imark', 'Christine Bulliard-Marbach', 'Corina Gredig', 'Gerhard Pfister', 'Jean-Luc Addor', 'Kathrin Bertschy', 'Katja Christ', 'Laurent Wehrli', 'Leo Müller', 'Lorenz Hess', 'Lorenzo Quadri', 'Lukas Reimann', 'Marie-France Roth Pasquier', 'Markus Ritter', 'Melanie Mettler', 'Nicolò Paganini', 'Nik Gugger', 'Priska Wismer-Felder', 'Sidney Kamerzin', 'Simon Stadler', 'Stefan Müller-Altermatt', 'Vincent Maitre'],
    '22.3329': ['Andreas Glarner', 'Andri Silberschmidt', 'Beat Walti', 'Christian Wasserfallen', 'Damien Cottier', 'Elisabeth Schneider-Schneiter',  'Lorenz Hess', 'Maja Riniker', 'Marc Jost', 'Marie-France Roth Pasquier', 'Matthias Samuel Jauslin', 'Patricia von Falkenstein', 'Peter Schilliger', 'Philippe Nantermod', 'Regine Sauter', 'Simone de Montmollin', 'Susanne Vincenz-Stauffacher', 'Vincent Maitre'],
    '22.3456': ['Alex Farinelli', 'Andri Silberschmidt', 'Anna Giacometti', 'Beat Walti', 'Benjamin Giezendanner', 'Christian Wasserfallen', 'Christine Bulliard-Marbach', 'Damien Cottier', 'Daniela Schneeberger', 'Hans-Peter Portmann', 'Laurent Wehrli', 'Leo Müller', 'Lorenz Hess', 'Maja Riniker', 'Matthias Samuel Jauslin', 'Markus Ritter', 'Nicolò Paganini', 'Patricia von Falkenstein', 'Peter Schilliger', 'Philippe Nantermod', 'Regine Sauter', 'Sidney Kamerzin', 'Simone de Montmollin', 'Susanne Vincenz-Stauffacher', 'Thomas Rechsteiner'],
    '22.3577': ['Alex Farinelli', 'Andri Silberschmidt', 'Anna Giacometti', 'Beat Walti', 'Benjamin Roduit', 'Céline Weber', 'Christian Lohr', 'Christian Wasserfallen', 'Christine Bulliard-Marbach', 'Damien Cottier', 'Daniela Schneeberger', 'Hans-Peter Portmann', 'Leo Müller', 'Maja Riniker', 'Markus Ritter', 'Martina Bircher', 'Matthias Samuel Jauslin', 'Patricia von Falkenstein', 'Peter Schilliger', 'Philippe Nantermod', 'Regine Sauter', 'Susanne Vincenz-Stauffacher'],
    '22.3606': ['Andri Silberschmidt', 'Anna Giacometti', 'Beat Walti', 'Benjamin Roduit', 'Christine Bulliard-Marbach', 'Damien Cottier', 'Daniela Schneeberger', 'Gerhard Pfister', 'Jacques Nicolet', 'Lorenz Hess', 'Maja Riniker', 'Markus Ritter', 'Martin Bäumle', 'Martina Bircher', 'Matthias Samuel Jauslin', 'Patricia von Falkenstein', 'Peter Schilliger', 'Priska Wismer-Felder', 'Regine Sauter', 'Susanne Vincenz-Stauffacher', 'Vincent Maitre'],
    '22.3610': ['Alex Farinelli', 'Andri Silberschmidt', 'Anna Giacometti', 'Beat Walti', 'Hans-Peter Portmann', 'Lorenz Hess', 'Martin Bäumle', 'Martina Bircher', 'Matthias Samuel Jauslin', 'Patricia von Falkenstein', 'Regine Sauter'],
    '22.3793': ['Barbara Schaffner', 'Beat Flach', 'Elisabeth Schneider-Schneiter', 'Jean-Luc Addor', 'Kathrin Bertschy', 'Katja Christ', 'Laurent Wehrli', 'Nicolò Paganini', 'Philipp Matthias Bregy', 'Pierre-André Page', 'Thomas Rechsteiner'],
    '22.3870': ['Alex Farinelli', 'Andreas Gafner', 'Andri Silberschmidt', 'Bruno Walliser', 'Céline Amaudruz', 'Damien Cottier', 'Jean-Luc Addor', 'Jon Pult', 'Jürg Grossen', 'Katja Christ', 'Laurent Wehrli', 'Leo Müller', 'Markus Ritter', 'Nicolò Paganini', 'Philipp Matthias Bregy', 'Sidney Kamerzin', 'Simon Stadler', 'Simone de Montmollin'],
    '22.3872': ['Alex Farinelli', 'Aline Trede', 'Andri Silberschmidt', 'Anna Giacometti', 'Bastien Girod', 'Beat Walti', 'Benjamin Roduit', 'Christian Dandrès', 'Christian Lohr', 'Christian Wasserfallen', 'Christine Badertscher', 'Christophe Clivaz', 'Damien Cottier', 'Daniela Schneeberger', 'Delphine Klopfenstein Broggini', 'Diana Gutjahr', 'Emmanuel Amoos', 'Fabien Fivaz', 'Felix Wettstein', 'Florence Brenzikofer', 'Gerhard Andrey', 'Greta Gysin', 'Hans-Peter Portmann', 'Katharina Prelicz-Huber', 'Laurent Wehrli', 'Leo Müller', 'Léonore Porchet', 'Maja Riniker', 'Manuela Weichelt', 'Marionna Schlatter', 'Markus Ritter', 'Matthias Samuel Jauslin', 'Nicolò Paganini', 'Patricia von Falkenstein', 'Peter Schilliger', 'Philippe Nantermod', 'Regine Sauter', 'Sidney Kamerzin', 'Simone de Montmollin'],
    '22.3884': [],
    '22.3889': ['Céline Weber', 'Christian Imark', 'Christian Wasserfallen', 'Diana Gutjahr', 'Franz Grüter', 'Hans-Peter Portmann', 'Jacques Nicolet', 'Nadja Umbricht Pieren', 'Nicolò Paganini', 'Peter Schilliger', 'Philipp Matthias Bregy', 'Philippe Nantermod', 'Priska Wismer-Felder', 'Sidney Kamerzin', 'Simon Stadler', 'Simone de Montmollin', 'Stefanie Heimgartner', 'Thomas Burgherr', 'Thomas Hurter', 'Thomas Rechsteiner'],
    '22.3931': [],
    '22.4208': ['Barbara Schaffner', 'Beat Flach', 'Florence Brenzikofer', 'Jean-Luc Addor', 'Jürg Grossen', 'Katja Christ', 'Laurent Wehrli', 'Lukas Reimann', 'Marc Jost', 'Marie-France Roth Pasquier', 'Markus Ritter', 'Martin Bäumle', 'Simon Stadler', 'Stefan Müller-Altermatt', 'Vincent Maitre'],
    '22.4220': [],
    '22.4258': [],
    '22.4270': ['Aline Trede', 'Andreas Gafner', 'Benjamin Roduit', 'Céline Amaudruz', 'Christian Lohr', 'Christine Bulliard-Marbach', 'Diana Gutjahr', 'Elisabeth Schneider-Schneiter', 'Gerhard Pfister', 'Hans-Peter Portmann', 'Jacques Nicolet', 'Jean-Luc Addor', 'Leo Müller', 'Lorenz Hess', 'Marie-France Roth Pasquier', 'Markus Ritter', 'Michael Graber', 'Nicolò Paganini', 'Nik Gugger', 'Peter Schilliger', 'Philipp Matthias Bregy', 'Pierre-Alain Fridez', 'Pierre-André Page', 'Priska Wismer-Felder', 'Sidney Kamerzin', 'Simon Stadler', 'Thomas "Tommy" Matter', 'Valérie Piller Carrard'],
    '22.4275': ['Christian Lohr', 'Christine Bulliard-Marbach', 'Gerhard Pfister', 'Hans-Peter Portmann', 'Markus Ritter', 'Matthias Samuel Jauslin', 'Philipp Matthias Bregy', 'Sidney Kamerzin', 'Simon Stadler', 'Thomas Rechsteiner'],
    '22.4447': ['Alex Farinelli', 'Andreas Glarner', 'Barbara Schaffner', 'Barbara Steinemann', 'Beat Flach', 'Beat Walti', 'Bruno Walliser', 'Céline Weber', 'Christian Imark', 'Corina Gredig', 'Damien Cottier', 'Diana Gutjahr', 'Franz Grüter', 'Gregor Rutz', 'Hans-Peter Portmann', 'Jacques Nicolet', 'Jean-Luc Addor', 'Jürg Grossen', 'Kathrin Bertschy', 'Lars Guggisberg', 'Laurent Wehrli', 'Lorenzo Quadri', 'Maja Riniker', 'Markus Ritter', 'Martin Bäumle', 'Matthias Samuel Jauslin', 'Mauro Tuena', 'Melanie Mettler', 'Michael Graber', 'Nicolò Paganini', 'Patricia von Falkenstein', 'Peter Schilliger', 'Piero Marchesi', 'Sidney Kamerzin', 'Simon Stadler', 'Stefanie Heimgartner', 'Susanne Vincenz-Stauffacher', 'Thomas Rechsteiner'],
    '22.4497': ['Alex Farinelli', 'Benjamin Giezendanner', 'Benjamin Roduit', 'Céline Weber', 'Céline Widmer', 'Christian Wasserfallen', 'Corina Gredig', 'Damien Cottier', 'Elisabeth Schneider-Schneiter', 'Eric Nussbaumer', 'Hans-Peter Portmann', 'Laurent Wehrli', 'Leo Müller', 'Lorenz Hess', 'Maja Riniker', 'Marie-France Roth Pasquier', 'Markus Ritter', 'Matthias Samuel Jauslin', 'Nicolas Walder', 'Nicolò Paganini', 'Patricia von Falkenstein', 'Peter Schilliger', 'Philipp Matthias Bregy', 'Philippe Nantermod', 'Raphaël Mahaim', 'Sibel Arslan', 'Sidney Kamerzin', 'Simone de Montmollin', 'Sophie Michaud Gigon', 'Stefan Müller-Altermatt', 'Susanne Vincenz-Stauffacher', 'Thomas Hurter', 'Thomas Rechsteiner', 'Vincent Maitre'],
    '23.3017': ['Céline Weber', 'Jean-Luc Addor', 'Jürg Grossen', 'Lorenzo Quadri', 'Marie-France Roth Pasquier', 'Simon Stadler', 'Vincent Maitre'],
    '23.3025': [],
    '23.3070': ['Benjamin Roduit', 'Céline Amaudruz', 'Céline Weber', 'Christine Bulliard-Marbach', 'Corina Gredig', 'Marie-France Roth Pasquier', 'Markus Ritter', 'Melanie Mettler', 'Nik Gugger', 'Priska Wismer-Felder', 'Stefan Müller-Altermatt', 'Vincent Maitre'],
    '23.3101': ['Alex Farinelli', 'Anna Giacometti', 'Barbara Schaffner', 'Beat Flach', 'Benjamin Roduit', 'Céline Weber', 'Christine Bulliard-Marbach', 'Corina Gredig', 'Gerhard Pfister', 'Hans-Peter Portmann', 'Jürg Grossen', 'Katja Christ', 'Laurent Wehrli', 'Lorenz Hess', 'Marie-France Roth Pasquier', 'Martin Bäumle', 'Matthias Samuel Jauslin', 'Melanie Mettler', 'Nicolò Paganini', 'Patricia von Falkenstein', 'Priska Wismer-Felder', 'Simon Stadler', 'Stefan Müller-Altermatt', 'Susanne Vincenz-Stauffacher', 'Thomas Rechsteiner', 'Vincent Maitre'],
    '23.3136': [],
    '23.3300': ['Alex Farinelli', 'Andreas Gafner', 'Anna Giacometti', 'Barbara Schaffner', 'Beat Flach', 'Benjamin Roduit', 'Bruno Walliser', 'Céline Amaudruz', 'Christian Lohr', 'Christine Bulliard-Marbach', 'Gerhard Pfister', 'Hans-Peter Portmann', 'Jacques Nicolet', 'Jean-Luc Addor', 'Jürg Grossen', 'Katja Christ', 'Lorenz Hess', 'Marie-France Roth Pasquier', 'Priska Wismer-Felder'],
    '23.3346': ['Alex Farinelli', 'Anna Giacometti', 'Benjamin Roduit', 'Christine Bulliard-Marbach', 'Vincent Maitre'],
    '23.3501': ['Alex Farinelli', 'Andreas Gafner', 'Benjamin Giezendanner', 'Christian Lohr', 'Jean-Luc Addor', 'Lukas Reimann', 'Markus Ritter', 'Matthias Samuel Jauslin', 'Philippe Nantermod', 'Sidney Kamerzin'],
    '23.3850': ['Barbara Schaffner', 'Beat Flach', 'Benjamin Roduit', 'Céline Amaudruz', 'Céline Weber', 'Christine Bulliard-Marbach', 'Corina Gredig', 'Damien Cottier', 'Elisabeth Schneider-Schneiter', 'Gerhard Pfister', 'Jean-Luc Addor', 'Jürg Grossen', 'Katja Christ', 'Lorenz Hess', 'Marc Jost', 'Marie-France Roth Pasquier', 'Markus Ritter', 'Melanie Mettler', 'Nik Gugger', 'Priska Wismer-Felder', 'Sidney Kamerzin', 'Simon Stadler', 'Thomas Burgherr', 'Vincent Maitre'],
    '23.3969': []
}

relevances = {
'21.531': [8, 7, 3],
'21.4283': [7, 8],
'21.4405': [4, 3, 2],
'21.4426': [4, 8, 3],
'21.4533': [4, 7],
'21.4549': [4, 3, 2],
'21.4606': [6, 2],
'21.4660': [8, 4],
'22.043': [7, 3],
'22.404': [5, 7, 8],
'22.466': [5, 8, 7],
'22.469': [3, 2],
'22.472': [7, 2, 3],
'22.476': [2, 4, 7],
'22.486': [2, 4, 8],
'22.3055': [4, 2, 3],
'22.3202': [3, 2],
'22.3248': [7, 2, 3],
'22.3329': [5, 8],
'22.3456': [1, 4, 3],
'22.3577': [2, 6, 3],
'22.3606': [2, 3, 6],
'22.3610': [6, 2],
'22.3793': [7, 3],
'22.3870': [2, 7, 4],
'22.3872': [1, 2],
'22.3884': [2, 4, 6],
'22.3889': [2, 4, 7],
'22.3931': [3, 2, 7],
'22.4208': [7, 8, 2],
'22.4220': [8, 4, 3],
'22.4258': [2, 3, 7],
'22.4270': [4, 3, 1],
'22.4275': [6],
'22.4447': [1, 6, 2],
'22.4497': [1, 3, 2],
'23.420': [4, 8],
'23.3017': [7, 8, 3],
'23.3025': [3, 4],
'23.3070': [2, 3, 7],
'23.3101': [6, 3],
'23.3136': [4, 8, 1],
'23.3300': [2],
'23.3346': [5, 2, 6],
'23.3501': [8, 7],
'23.3850': [3, 2, 7],
'23.3969': [4, 1, 8]
}

inaccurates_knn = {
    '21.531': ['Melanie Mettler'],
    '21.4283': ['Céline Weber', 'Andreas Glarner', 'Nik Gugger', 'Martina Bircher', 'Stefanie Heimgartner', 'Christian Wasserfallen', 'Martin Bäumle'],
    '21.4405': [],
    '21.4426': ['Andreas Gafner', 'Monika Rüegger-Hurschler', 'Lukas Reimann', 'Christian Wasserfallen', 'Thomas Rechsteiner'],
    '21.4461': ['Nik Gugger'],
    '21.4533': ['Alex Farinelli', 'Céline Amaudruz', 'Benjamin "Beni" Fischer', 'Vincent Maitre', 'Laurent Wehrli', 'Lorenz Hess', 'Simon Stadler', 'Beat Flach', 'Jean-Luc Addor', 'Nik Gugger', 'Simone de Montmollin', 'Nicolò Paganini', 'Benjamin Roduit', 'Marc Jost', 'Christian Wasserfallen'],
    '21.4549': ['Melanie Mettler'],
    '21.4606': ['Michael Graber', 'Manuel Strupler', 'Alfred "Fredi" Heer', 'Philippe Nantermod', 'Pierre-André Page', 'Andreas Gafner', 'Diana Gutjahr', 'Lukas Reimann', 'Martina Bircher', 'Franz Grüter', 'Piero Marchesi'],
    '21.4660': ['Thomas Hurter', 'Benjamin "Beni" Fischer', 'Vincent Maitre', 'Andreas Gafner', 'Diana Gutjahr', 'Barbara Steinemann', 'Gregor Rutz', 'Lukas Reimann', 'Nadja Umbricht Pieren', 'Lorenzo Quadri', 'Benjamin Roduit', 'Stefanie Heimgartner', 'Christian Wasserfallen', 'Thomas Rechsteiner'],
    '22.043': [],
    '22.404': ['Céline Amaudruz', 'Philippe Nantermod', 'Elisabeth Schneider-Schneiter', 'Lorenz Hess', 'Simon Stadler', 'Hans-Peter Portmann', 'Nicolò Paganini', 'Marc Jost', 'Damien Cottier'],
    '22.466': [],
    '22.469': ['Christian Lohr', 'Markus Ritter', 'Vincent Maitre', 'Céline Weber', 'Laurent Wehrli', 'Elisabeth Schneider-Schneiter', 'Sidney Kamerzin', 'Jean-Luc Addor', 'Benjamin Roduit', 'Thomas Rechsteiner'],
    '22.472': ['Kathrin Bertschy', 'Nik Gugger', 'Marc Jost'],
    '22.476': [], 
    '22.486': [],
    '22.3055': ['Vincent Maitre', 'Lorenz Hess', 'Simon Stadler', 'Marie-France Roth Pasquier', 'Priska Wismer-Felder', 'Martin Bäumle'],
    '22.3202': ['Alex Farinelli', 'Patricia von Falkenstein', 'Benjamin Giezendanner', 'Philippe Nantermod', 'Jacques Nicolet', 'Beat Walti', 'Andri Silberschmidt', 'Gerhard Pfister', 'Mauro Tuena', 'Thomas Burgherr', 'Andreas Gafner', 'Lars Guggisberg', 'Sidney Kamerzin', 'Maja Riniker', 'Andreas Glarner', 'Gregor Rutz', 'Thomas "Tommy" Matter', 'Lukas Reimann', 'Nadja Umbricht Pieren', 'Jean-Luc Addor', 'Anna Giacometti', 'Daniela Schneeberger', 'Simone de Montmollin', 'Mike Egger', 'Hans-Peter Portmann', 'Sandra Sollberger', 'Regine Sauter', 'Benjamin Roduit', 'Cyril Aellen', 'Matthias Samuel Jauslin', 'Franz Grüter', 'Damien Cottier', 'Stefanie Heimgartner', 'Christian Wasserfallen', 'Thomas Rechsteiner', 'Martin Bäumle'],
    '22.3248': ['Christian Imark'],
    '22.3329': ['Céline Weber', 'Lorenz Hess', 'Andreas Glarner', 'Nik Gugger', 'Marc Jost', 'Martin Bäumle'],
    '22.3337': ['Martin Bäumle'],
    '22.3394': ['Markus Ritter', 'Elisabeth Schneider-Schneiter', 'Sidney Kamerzin', 'Nicolò Paganini', 'Martin Bäumle'],
    '22.3456': ['Christian Lohr', 'Markus Ritter', 'Laurent Wehrli', 'Gerhard Pfister', 'Simon Stadler', 'Leo Müller', 'Priska Wismer-Felder', 'Philipp Matthias Bregy', 'Benjamin Roduit', 'Christine Bulliard-Marbach'],
    '22.3577': ['Michael Graber', 'Alex Farinelli', 'Thomas Hurter', 'Alfred "Fredi" Heer', 'Philippe Nantermod', 'Beat Walti', 'Jean-Luc Addor', 'Anna Giacometti', 'Martina Bircher', 'Damien Cottier'],
    '22.3606': ['Michael Graber', 'Alex Farinelli', 'Beat Walti', 'Laurent Wehrli', 'Elisabeth Schneider-Schneiter', 'Maja Riniker', 'Anna Giacometti', 'Daniela Schneeberger', 'Damien Cottier'],
    '22.3610': ['Alex Farinelli', 'Patricia von Falkenstein', 'Peter Schilliger', 'Beat Walti', 'Andri Silberschmidt', 'Lorenz Hess', 'Anna Giacometti'],
    '22.3793': ['Céline Amaudruz', 'Kathrin Bertschy', 'Laurent Wehrli', 'Elisabeth Schneider-Schneiter', 'Beat Flach', 'Jean-Luc Addor', 'Barbara Schaffner', 'Nicolò Paganini', 'Philipp Matthias Bregy', 'Thomas Rechsteiner'],
    '22.3870': ['Andreas Gafner', 'Elisabeth Schneider-Schneiter', 'Simone de Montmollin', 'Hans-Peter Portmann', 'Nicolò Paganini'],
    '22.3872': ['Elisabeth Schneider-Schneiter', 'Anna Giacometti', 'Philipp Matthias Bregy'],
    '22.3884': ['Markus Ritter', 'Vincent Maitre', 'Gerhard Pfister', 'Lorenz Hess', 'Simon Stadler', 'Philipp Matthias Bregy', 'Benjamin Roduit', 'Christine Bulliard-Marbach'],
    '22.3889': ['Philippe Nantermod', 'Benjamin "Beni" Fischer', 'Mauro Tuena', 'Thomas Burgherr', 'Andreas Gafner', 'Lars Guggisberg', 'Erich Hess', 'Andreas Glarner', 'Monika Rüegger-Hurschler', 'Gregor Rutz', 'Thomas "Tommy" Matter', 'Nadja Umbricht Pieren', 'Thomas de Courten', 'Benjamin Roduit', 'Marc Jost', 'Stefanie Heimgartner', 'Christian Wasserfallen', 'Thomas Rechsteiner'],
    '22.3931': ['Michael Graber', 'Bruno Walliser', 'Brigitte Crottaz', 'Benjamin "Beni" Fischer', 'Jacques Nicolet', 'Christine Badertscher', 'Céline Weber', 'Sophie Michaud Gigon', 'Lars Guggisberg', 'Kilian Baumann', 'Christian Dandrès', 'Laurence Fehlmann Rielle', 'Claudia Friedl', 'Lukas Reimann', 'Felix Wettstein', 'Jean-Luc Addor', 'Nik Gugger', 'Emmanuel Amoos', 'Christophe Clivaz', 'Mike Egger', 'Roger Nordmann', 'Hans-Peter Portmann', 'Bastien Girod', 'Franziska Ryser', 'Marc Jost', 'Jacqueline Badran', 'Stefanie Heimgartner'],
    '22.4208': ['Florence Brenzikofer', 'Martin Bäumle'],
    '22.4220': ['Céline Weber', 'Nik Gugger', 'Marc Jost', 'Martin Bäumle'],
    '22.4258': ['Tamara Funiciello', 'Michael Graber', 'Christian Imark', 'Bruno Walliser', 'Patricia von Falkenstein', 'Peter Schilliger', 'Brigitte Crottaz', 'Benjamin Giezendanner', 'Alfred "Fredi" Heer', 'Benjamin "Beni" Fischer', 'Christine Badertscher', 'Florence Brenzikofer', 'Pierre-André Page', 'Mauro Tuena', 'Greta Gysin', 'Thomas Burgherr', 'Lars Guggisberg', 'Christian Dandrès', 'Elisabeth Schneider-Schneiter', 'Laurence Fehlmann Rielle', 'Erich Hess', 'Andreas Glarner', 'Monika Rüegger-Hurschler', 'Claudia Friedl', 'Thomas "Tommy" Matter', 'Leo Müller', 'Emmanuel Amoos', 'Christophe Clivaz', 'Mike Egger', 'Roger Nordmann', 'Irène Kälin', 'Regine Sauter', 'Bastien Girod', 'Franziska Ryser', 'Matthias Samuel Jauslin', 'Franz Grüter', 'Marionna Schlatter', 'Damien Cottier', 'Stefanie Heimgartner', 'Marcel Dettling', 'Piero Marchesi', 'Thomas Rechsteiner'],
    '22.4270': ['Michael Graber', 'Céline Amaudruz', 'Peter Schilliger', 'Vincent Maitre', 'Jacques Nicolet', 'Pierre-André Page', 'Laurent Wehrli', 'Andreas Gafner', 'Elisabeth Schneider-Schneiter', 'Lukas Reimann', 'Jean-Luc Addor', 'Simone de Montmollin', 'Pierre-Alain Fridez', 'Hans-Peter Portmann', 'Thomas Rechsteiner'],
    '22.4275': ['Alex Farinelli', 'Patricia von Falkenstein', 'Markus Ritter', 'Vincent Maitre', 'Laurent Wehrli', 'Gerhard Pfister', 'Simon Stadler', 'Anna Giacometti', 'Hans-Peter Portmann', 'Priska Wismer-Felder', 'Philipp Matthias Bregy', 'Matthias Samuel Jauslin', 'Thomas Rechsteiner'],
    '22.4447': ['Christian Imark', 'Patricia von Falkenstein', 'Céline Amaudruz', 'Benjamin Giezendanner', 'Alfred "Fredi" Heer', 'Philippe Nantermod', 'Beat Walti', 'Gerhard Pfister', 'Mauro Tuena', 'Thomas Burgherr', 'Andreas Gafner', 'Lars Guggisberg', 'Elisabeth Schneider-Schneiter', 'Sidney Kamerzin', 'Barbara Steinemann', 'Maja Riniker', 'Simon Stadler', 'Andreas Glarner', 'Sandra Sollberger', 'Philipp Matthias Bregy', 'Susanne Vincenz-Stauffacher', 'Damien Cottier', 'Marcel Dettling'],
    '22.4497': ['Kathrin Bertschy', 'Stefan Müller-Altermatt', 'Jürg Grossen', 'Corina Gredig', 'Beat Flach', 'Marie-France Roth Pasquier', 'Nik Gugger', 'Marc Jost'],
    '23.420': ['Brigitte Crottaz', 'Jürg Grossen', 'Katja Christ', 'Melanie Mettler', 'Corina Gredig', 'Priska Seiler Graf', 'Barbara Schaffner', 'Christophe Clivaz', 'Matthias Aebischer', 'Martin Bäumle'],
    '23.3017': ['Christian Lohr', 'Vincent Maitre', 'Céline Weber', 'Stefan Müller-Altermatt', 'Jürg Grossen', 'Simon Stadler', 'Marie-France Roth Pasquier', 'Nik Gugger', 'Lorenzo Quadri', 'Priska Wismer-Felder'],
    '23.3025': ['Céline Weber', 'Nik Gugger', 'Marc Jost'],
    '23.3070': [],
    '23.3101': ['Stefan Müller-Altermatt', 'Melanie Mettler', 'Nik Gugger', 'Marc Jost'],
    '23.3136': ['Christian Lohr', 'Vincent Maitre', 'Lorenz Hess', 'Marie-France Roth Pasquier', 'Nik Gugger', 'Christian Wasserfallen', 'Thomas Rechsteiner'],
    '23.3300': ['Corina Gredig', 'Marie-France Roth Pasquier'],
    '23.3346': ['Martin Bäumle'],
    '23.3501': ['Peter Schilliger', 'Jacques Nicolet', 'Sidney Kamerzin', 'Simon Stadler', 'Lukas Reimann'],
    '23.3850': [],
    '23.3969': ['Christian Lohr', 'Lorenz Hess', 'Marie-France Roth Pasquier', 'Nik Gugger', 'Hans-Peter Portmann', 'Christian Wasserfallen', 'Thomas Rechsteiner']
}

names_inprompted = {
    '21.531': [],
    '21.4283': [],
    '21.4405': [],
    '21.4426': [],
    '21.4533': [],
    '21.4549': [],
    '21.4606': [],
    '21.4660': ['Martina Munz', 'Mattea Meyer', 'Matthias Aebischer', 'Matthias Samuel Jauslin', 'Mauro Tuena'],
    '22.043': ['Matthias Aebischer', 'Matthias Samuel Jauslin', 'Mauro Tuena', 'Melanie Mettler', 'Michael Graber', 'Mike Egger', 'Min Li Marti', 'Monika Rüegger-Hurschler', 'Nadine Masshardt', 'Nadja Umbricht Pieren', 'Nicolas Walder', 'Nicolò Paganini', 'Nik Gugger', 'Patricia von Falkenstein', 'Peter Schilliger', 'Philipp Matthias Bregy', 'Philippe Nantermod', 'Piero Marchesi', 'Pierre-Alain Fridez', 'Pierre-André Page', 'Priska Seiler Graf'],
    '22.404': [],
    '22.466': ['Cédric Wermuth', 'Erich Hess', 'Fabian Molina'],
    '22.469': [],
    '22.472': [],
    '22.476': [], 
    '22.486': ['Thomas "Tommy" Matter', 'Thomas Rechsteiner', 'Valérie Piller Carrard', 'Vincent Maitre'],
    '22.3055': [],
    '22.3202': ['Regine Sauter', 'Roger Nordmann', 'Samira Marti', 'Samuel Bendahan'],
    '22.3248': [],
    '22.3329': [],
    '22.3456': [],
    '22.3577': [],
    '22.3606': [],
    '22.3610': ['Priska Seiler Graf', 'Priska Wismer-Felder', 'Raphaël Mahaim'],
    '22.3793': [],
    '22.3870': [],
    '22.3872': [],
    '22.3884': [],
    '22.3889': [],
    '22.3931': ['Matthias Aebischer', 'Matthias Samuel Jauslin', 'Mauro Tuena', 'Melanie Mettler', 'Michael Graber', 'Mike Egger', 'Min Li Marti', 'Monika Rüegger-Hurschler', 'Nadine Masshardt', 'Nadja Umbricht Pieren', 'Nicolas Walder', 'Nicolò Paganini', 'Nik Gugger', 'Patricia von Falkenstein', 'Peter Schilliger', 'Philipp Matthias Bregy', 'Philippe Nantermod', 'Piero Marchesi', 'Pierre-Alain Fridez', 'Pierre-André Page'],
    '22.4208': ['Michael Graber', 'Mike Egger', 'Min Li Marti', 'Monika Rüegger-Hurschler', 'Nadine Masshardt', 'Nadja Umbricht Pieren', 'Nicolas Walder'],
    '22.4220': [],
    '22.4258': [],
    '22.4270': [],
    '22.4275': [],
    '22.4447': ['Katja Christ'],
    '22.4497': [],
    '23.420': [],
    '23.3017': [],
    '23.3025': [],
    '23.3070': [],
    '23.3101': [],
    '23.3136': [],
    '23.3300': [],
    '23.3346': [],
    '23.3501': [],
    '23.3850': [],
    '23.3969': []
}

axes_translation = {
    'cleavage_1': 'Open Foreign Pol',
    'cleavage_2': 'Liberal Econ',
    'cleavage_3': 'Rest Finances',
    'cleavage_4': 'Law and Order',
    'cleavage_5': 'Rest Immigration',
    'cleavage_6': 'Env Protection',
    'cleavage_7': 'Welfare State',
    'cleavage_8': 'Liberal Soc'
}

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = [
    dbc.Card(
        children=[
            dbc.CardHeader('Comparison of Decision-boundaries between KNN, Agent and Actual'),
            dbc.CardBody(
                children = [
                    dbc.Row(
                        dbc.Col(
                            dcc.Dropdown(referendums, referendums[0], id='dropdown'),
                            width = 4
                        )
                    ),
                    dbc.Row(
                        children=[
                            dbc.Col(
                                children=[
                                    html.H5('Actual Decision Boundary'),
                                    #dcc.Graph(figure={}, id='graph-ground'),
                                ],
                                width = 4
                            ),
                            dbc.Col(
                                children=[
                                    html.H5('Agent Decision Boundary'),
                                    #dcc.Graph(figure={}, id='graph-agent'),
                                ],
                                width = 4
                            ),
                            dbc.Col(
                                children=[
                                    html.H5('KNN Decision Boundary'),
                                    #dcc.Graph(figure={}, id='graph-knn'),
                                ],
                                width = 4
                            ),
                        ],
                    ),
                    dbc.Row(
                        children=[
                            dbc.Col(
                                children=[
                                    #html.H5('Actual Decision Boundary'),
                                    dcc.Graph(figure={}, id='graph-ground'),
                                ],
                                width = 4
                            ),
                            dbc.Col(
                                children=[
                                    #html.H5('Agent Decision Boundary'),
                                    dcc.Graph(figure={}, id='graph-agent'),
                                ],
                                width = 4
                            ),
                            dbc.Col(
                                children=[
                                    #html.H5('KNN Decision Boundary'),
                                    dcc.Graph(figure={}, id='graph-knn'),
                                ],
                                width = 4
                            ),
                        ]
                    ),
                    dbc.Row(
                        children=[
                            dbc.Col(
                                children=[
                                    #html.H5('Actual Decision Boundary'),
                                    html.Div(id='ground-acc'),
                                ],
                                width = 4
                            ),
                            dbc.Col(
                                children=[
                                    #html.H5('Agent Decision Boundary'),
                                    html.Div(id='agent-acc'),
                                ],
                                width = 4
                            ),
                            dbc.Col(
                                children=[
                                    #html.H5('KNN Decision Boundary'),
                                    html.Div(id='knn-acc'),
                                ],
                                width = 4
                            ),
                        ]
                    )
                ]
            )
        ]
    ),
]

@callback(
    Output(component_id='graph-ground', component_property='figure'),
    Output(component_id='graph-agent', component_property='figure'),
    Output(component_id='graph-knn', component_property='figure'),
    Output(component_id='agent-acc', component_property='children'),
    Output(component_id='knn-acc', component_property='children'),
    Input(component_id='dropdown', component_property='value')
)
def update_graph(vote_chosen):
    final_data_copied = final_data.copy()
    final_data_copied[vote_chosen] = final_data_copied[vote_chosen].map(dict({'Yes':1, 'No':0}))
    final_data_copied['agent_recom'] = final_data_copied[vote_chosen]
    final_data_copied['knn_recom'] = final_data_copied[vote_chosen]

    wo_vote = vote_chosen.replace('vote_', '', 1)
    relevant_axes_1 = 'cleavage_' + str(relevances[wo_vote][0])
    relevant_axes_2 = 'cleavage_' + str(relevances[wo_vote][1])
    to_be_cropped = names_inprompted[wo_vote]

    knn_inacc = inaccurates_knn[wo_vote]
    algo_inacc = inaccurates_agent[wo_vote]

    final_data_copied = final_data_copied[['full_name', relevant_axes_1, relevant_axes_2, vote_chosen, 'agent_recom', 'knn_recom']]

    basic_data = final_data_copied.rename(columns={relevant_axes_1: axes_translation[relevant_axes_1], relevant_axes_2: axes_translation[relevant_axes_2]}).dropna()
    basic_data = basic_data.loc[~(basic_data['full_name'].isin(to_be_cropped))]
    basic_data.loc[(basic_data['full_name'].isin(algo_inacc)), 'agent_recom'] = 1 - basic_data.loc[(basic_data['full_name'].isin(algo_inacc)), 'agent_recom']
    basic_data.loc[(basic_data['full_name'].isin(knn_inacc)), 'knn_recom'] = 1 - basic_data.loc[(basic_data['full_name'].isin(knn_inacc)), 'knn_recom']

    basic_data[axes_translation[relevant_axes_1]] = 4 * basic_data[axes_translation[relevant_axes_1]] + 1
    basic_data[axes_translation[relevant_axes_2]] = 4 * basic_data[axes_translation[relevant_axes_2]] + 1

    fig_ground = px.scatter(basic_data, x=axes_translation[relevant_axes_1], y=axes_translation[relevant_axes_2], color=vote_chosen,
                hover_data=['full_name'])
    fig_agent = px.scatter(basic_data, x=axes_translation[relevant_axes_1], y=axes_translation[relevant_axes_2], color='agent_recom',
                hover_data=['full_name'])
    fig_knn = px.scatter(basic_data, x=axes_translation[relevant_axes_1], y=axes_translation[relevant_axes_2], color='knn_recom',
                hover_data=['full_name'])
    
    number_voters = len(basic_data)
    acc_agent = f'Accuracy: {1 - np.round(len(algo_inacc)/number_voters, 3)}'
    acc_knn = f'Accuracy: {1 - np.round(len(knn_inacc)/number_voters, 3)}'

    return fig_ground, fig_agent, fig_knn, acc_agent, acc_knn

if __name__ == '__main__':
    app.run(debug=True)
