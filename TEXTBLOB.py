
from textblob import TextBlob

df = pd.read_csv("C:/Users/paul3/Desktop/wiki_data_new.csv")
df.shape
def senti(x):
    return TextBlob(x).sentiment  
 
df['senti_score'] = df['comment_text'].apply(senti)
 
df.senti_score.head()

df.to_csv("C:/Users/paul3/Desktop/wiki_data_new_senti.csv")