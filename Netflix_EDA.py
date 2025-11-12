import pandas as pd
import kagglehub
import matplotlib.pyplot as plt


# Download latest version
path = kagglehub.dataset_download("shivamb/netflix-shows")

print("Path to dataset files:", path)



# convert it into data frame

df=pd.read_csv('netflix_titles.csv')
print(df.head())

#Startted cleaning
#print(df.info())
#print(df.isnull().sum())

#print(df.describe())

#print(df['director'])

#print(df['director'].fillna('Unknown',inplace=False))

#print(df['director'].fillna('unknown'))
#print(df.fillna({'director':'Unknown'},inplace=True))


print(df['country'])

print("Before dropping:", len(df))
df.dropna(subset=['country'], inplace=True)
print("After dropping:", len(df))
print(df['country'])



print(len(df))

print(df.columns)

print(df.shape)

row, cols=df.shape
print("Totals rows {rows} amd columns {cols}")

print("//////dublicates///////")

df.drop_duplicates(inplace=True)

print(df['show_id'])

#Data cleaned recheck if that been done or not

print(df.isnull().sum())

#Director 

print(df['director'])

df['director'].fillna('unknown',inplace=True)
print(df['director'])


print(df.isnull().sum())


print(df['director'].count())

#cast


print(df['cast'])

print(df['cast'].isnull().sum())

df['cast'].fillna('Unknown',inplace=True)
print(df['cast'].isnull().sum())

print(df.isnull().sum())

#Date
print(df['date_added'])
df['date_added'].fillna(df['date_added'].mode()[0],inplace=True)
print(df['date_added'])

print(df.isnull().sum())

#rating

df['rating'].fillna('Not rated',inplace=True)

df['duration'].fillna('None',inplace=True)

print(df.isnull().sum())



#Matplotlib


print(df.columns)


df=df.dropna(subset=['type','release_year','rating','country','duration'])


type_counts=df['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index, type_counts.values, color=['lightgreen','skyblue'])
plt.title('Number of Tv Shows VS Movies')
plt.xlabel('Types')
plt.ylabel('COunt')

plt.savefig('TV V Movies.png', dpi=300, bbox_inches='tight')

#plt.show()
#save fig


#Rating

rate_counts=df['rating'].value_counts()
plt.figure(figsize=(7,5))
plt.pie(rate_counts, labels=rate_counts.index, autopct='1.1f%%', startangle=90)
plt.title('Percentage of content rating')
plt.tight_layout()
plt.savefig('rating.png', dpi=300, bbox_inches='tight')
#plt.show()



# Movie duration using Histogram

print(df['duration'])

movie_df=df[df['type'] == 'Movie'].copy()

movie_df=movie_df[movie_df['duration'].str.contains("mi",regex=False)]

movie_df['duration_int']=movie_df['duration'].str.replace(' min','',regex=False).astype(int)
# Plot the histogram
plt.figure(figsize=(6,5))
plt.hist(movie_df['duration_int'],color='purple')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.title('Distribution of Movie Durations on Netflix')

plt.savefig('duration.png',dpi=300,bbox_inches='tight')
#plt.show()


#realeas Year And number of shows
print(df.columns)

realease_counts=df['release_year'].value_counts().sort_index()

plt.figure(figsize=(6,4))
plt.scatter(realease_counts.index, realease_counts.values, color='red')
plt.xlabel('year')
plt.ylabel('total movies released')
plt.title('Total released Per Year')
plt.savefig('Released per year',dpi=300,bbox_inches='tight')
plt.show()


# 10 country

country_counts=df['country'].value_counts().head(10)
plt.figure(figsize=(6,4))
plt.barh(country_counts.index,country_counts.values,color='violet')
plt.title('Top 10 countries')
plt.xlabel('Number of shows')
plt.savefig('10 most Shows by country')
plt.ylabel('Coutnry')
plt.show()


print(df.columns)
# Subplot Movies V Tv shows Per year


content_by_year=df.groupby(['release_year','type']).size().unstack().fillna(0)
fig, ax=plt.subplots(1,2, figsize=(12, 5))
ax[0].plot(content_by_year.index,content_by_year['Movie'],color='blue')
ax[0].set_title('Movie released by year')
fig.suptitle("Comparison of Tv shows and Released Year")

ax[0].plot(content_by_year.index, content_by_year['TV Show'],color='green')
ax[0].set_title('Tv shgows released over year')
plt.savefig('Comparison betn Tv And movies',dpi=300)
plt.show()



