import pandas as pd
import glob

files =glob.glob("data/*.csv")

all_data=[]

for file in files:
    df = pd.read_csv(file)
    df=df[df["product"]=="pink morsel"]
    df["price"]=df["price"].replace("[$]","",regex=True).astype(float)
    df["sales"]=df["quantity"]*df["price"]
    df=df[["sales","date","region"]]
    all_data.append(df)

final_df=pd.concat(all_data)
final_df.to_csv("formatted_output.csv",index=False)
print("all files are processed successfully!")


