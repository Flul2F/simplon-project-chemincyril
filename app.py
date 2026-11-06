import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

données['ca'] = données['prix'] * données['qte']
données2 = données.groupby('produit')[['qte', 'ca']].sum().reset_index()

figure_regions = px.pie(
    données,
    values='qte',
    names='region',
    title='quantité vendue par région',
)
figure_regions.write_html('ventes-par-region.html') 

figure_ventes = px.pie(
    données2,
    values='qte',
    names='produit',
    title='Quantités vendues par produit',
)
figure_ventes.write_html('ventes-par-produit.html')

figure_ca = px.pie(
    données2,
    values='ca',
    names='produit',
    title="Chiffre d'affaires par produit",
)
figure_ca.write_html('ca-par-produit.html')

print('Graphiques générés avec succès :')