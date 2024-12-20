import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
#matplotlib.use('TkAgg')
""" 
 input:eggnogmapper
 output:COG barplot,df_COG
 """
#fonksiyon
def COGplot(x,y,z):
    input_path = "output/Eggnogmapper/out.emapper-1.annotationsserratia1"
    output_path_csv = "output/COG_analysis/df_COG.csv"
    output_path_excel = "output/COG_analysis/df_COG.xlsx"

    df = pd.read_csv(input_path, sep="\t", header="infer", skiprows=4)

    # Sadece '#query' ve 'COG_category' sütunlarını seçme
    df_COG = df[['#query', 'COG_category']]
    df_COG.to_csv(output_path_csv, sep="\t", header=True, index=False)
    df_COG.to_excel(output_path_excel, header=True, index=False)

    df_COG = df_COG[df_COG['COG_category'] != "-"]
    # explode fonksiyonunu kullanarak her kategoriye ayrı satır olarak ayırma
    df_exploded = df_COG.explode('COG_category')
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
    return




x=10
y="Hacer"
z=['karpuz', 'çilek', 'kavun']
i={"karpuz":1, "çilek":10, "kavun":2}
j={"karpuz":[1, "pazartesi"], "çilek":[10, "salı"], "kavun":[2, "çarşamba"]}
def marketfonksiyon(x,y,z,i,j):
    x = 10
    y = "Hacer"
    z = ['karpuz', 'çilek', 'kavun']
    i = {"karpuz": 1, "çilek": 10, "kavun": 2}
    j = {"karpuz": [1, "pazartesi"], "çilek": [10, "salı"], "kavun": [2, "çarşamba"]}
    cumle=print("Hacer 10 kere markete gitti ve marketten: kavun, karpuz, çilek aldı.")


    return cumle
marketfonksiyon(x,y,z,i,j)