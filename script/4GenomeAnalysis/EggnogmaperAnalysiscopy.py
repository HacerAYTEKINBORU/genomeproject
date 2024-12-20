import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')

df=pd.read_csv("/output/Eggnogmapper/out.emapper-1.annotationsserratia1",
               sep="\t", header="infer", skiprows=4)
#df=pd.read_csv("/Users/hacer/PycharmProjects/yenienv/genomeproject/output/out.emapper-2.annotationsserratia2",
               #sep="\t",header="infer", skiprows=4)
#df=pd.read_csv("/Users/hacer/PycharmProjects/yenienv/genomeproject/output/out.emapper-3.annotationsserratia3",
               #sep="\t" ,header="infer", skiprows=4)
#df=pd.read_csv("/Users/hacer/PycharmProjects/yenienv/genomeproject/output/out.emapper-4.annotationsserratia4",
               #sep="\t", header="infer", skiprows=4)
#df=pd.read_csv( "/Users/hacer/PycharmProjects/yenienv/genomeproject/output/out.emapper-5.annotationsserratia5",
                #sep="\t",header="infer", skiprows=4)
"""
COG fonksiyonel kategorisini çekme
COG kolonu nerde?
Bu kategori içinde tüm kolonu mu seçmeliyim yoksa bir seçme yapmalı mıyım? örn ilk 100 satır
COG ile birlikte karşılatırma yapma istiyor musun COG VE KEGG kıyasla fitreleme gibi
COG Category fonksiyonları:
A	RNA -
,

# COG_category'ye göre gruplandırma..
#df_grouped = df_exploded.groupby('COG_category')['Gen'].apply(list).reset_index()

# Sonuçları görüntüleme
#print("COG kategorilerine göre gruplandırılmış genler:")
#print(df_grouped)


# Count the occurrences of each COG category directly from the DataFrame
cog_counts = df_COG['COG_category'].value_counts()

# Plot the barplot directly from the Series
plt.figure(figsize=(12, 6))
cog_counts.plot(kind='bar')
plt.title("COG Categories Distribution", fontsize=16)
plt.xlabel("COG Categories", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
