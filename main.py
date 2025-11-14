import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
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

# print(df.tagline) # виводить стовпець tagline
# print(df.homepage) # виводить стовпець homepage
df.homepage = df.homepage.fillna("no homepage") # заповнює пропуски в стовпці homepage
# print(df.homepage)

# print(df["belongs_to_collection"])
df.fillna({"belongs_to_collection": "{}"}, inplace=True) # заповнює пропуски в стовпці belongs_to_collection
# print(df["belongs_to_collection"])
df.info()

df.dropna(inplace=True) # видаляє всі рядки з пропусками
# print(df.isnull().sum()) # перевіряє наявність пропусків
df.info() # виводить інформацію про датафрейм

# print(df.head())

# print(df.genres) # виводить стовпець genre
genres_count = df["genres"].value_counts() # рахує кількість унікальних значень в стовпці genre  
# print(genres_count)

# print(genres_count.index) # виводить унікальні значення в стовпці genre
# print(genres_count.values) # виводить кількість унікальних значень в стовпці genre

plt.figure(figsize=(6, 4)) # створює фігуру розміром 6 на 4 дюйми

sns.barplot(x=genres_count.index, y=genres_count.values)

plt.title("Count filf for genres") # додає заголовок до графіку
plt.xlabel("Genres") # додає підпис до осі x
plt.ylabel("Genres_count") # додає підпис до осі y

plt.xticks(rotation=45) # повертає підписи осі x на 45 градусів для кращої читабельності

plt.show()
