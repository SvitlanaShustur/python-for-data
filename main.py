import pandas as pd 

ukl = "data/movies_metadata.csv"

df = pd.read_csv(ukl)

# print(df.head())

# df.info()

# print(df.describe())

# print(df.isnull().sum())

# print(df[["belongs_to_collection", "homepage", "tagline"]])


# Старий спосіб заповнення пропусків
# df["tagline"].fillna("without tagline", inplace=True)

# Новий спосіб заповнення пропусків
# df.fillna({"tagline": "without tagline"}, inplace=True)
df["tagline"] = df["tagline"].fillna("without tagline")

print(df.tagline) # виводить стовпець tagline
print(df.homepage) # виводить стовпець homepage
df.homepage = df.homepage.fillna("no homepage") # заповнює пропуски в стовпці homepage
print(df.homepage)

print(df["belongs_to_collection"])
df.fillna({"belongs_to_collection": "{}"}, inplace=True) # заповнює пропуски в стовпці belongs_to_collection
print(df["belongs_to_collection"])
df.info()

df.dropna(inplace=True) # видаляє всі рядки з пропусками
print(df.isnull().sum()) # перевіряє наявність пропусків
df.info() # виводить інформацію про датафрейм