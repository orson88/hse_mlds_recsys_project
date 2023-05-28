import pandas as pd


df_test = pd.read_csv('test.csv.zip', usecols=['song'])
df_train = pd.read_csv('train.csv.zip', usecols=['song'])
df = pd.concat([df_test, df_train])
del df_test
del df_train
best_songs = df.value_counts().rename_axis('unique_songs').to_frame('counts').reset_index()

best_songs.to_csv("popular_songs.csv")

print("Done")
print(best_songs)
