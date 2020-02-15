import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


## Initialization

user_input = input("Please enter the name of the file you want to open\n")

print("Printing from " + user_input + "file")

try:
        with open(user_input) as f:
               data = list(csv.reader(f))
                #do something with the file
except IOError:
        print("ERROR. " + user_input + " does not exist or has not been found in the specified path. Please make sure the file is located in the same folder or directory.")


f.close()

#unzip data into two 1d arrays

x, y = zip(*data)
x = list(x)
y = list(y)

df ={'x':x,'y':y}

np.random.seed(200)
k=3 #number of iterations
# centroids[i] = [x,y]
centroids = {
	i+1: [np.random.randint(0,80), np.random.randint(0,80)]		#numbers lie between 1 and 80
	for i in range(k)
}

fig = plt.figure(figsize=(5,5))
plt.scatter(df['x'], df['y'], color='k')
colmap = {1: 'r', 2: 'g', 3: 'b'}
for i in centroids.keys():
	plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 80)
plt.ylim(0, 80)
plt.show()
f.close()

## Assignment Stage

def assignment(df, centroids):
	for i in centroids.keys():
		# sqrt((x1 - x2)^2 - (y1 - y2)^2)
		df["distance_from_{}".format(i)] = (
			np.sqrt(
				(df['x'] - centroids[i][0] ** 2
				+ (df['y'] - centroids[i][1] ** 2
			))
		))
	centroid_distance_cols = ["distance_from_{}".format(i) for i in centroids.keys()]
	df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)
	df['closest'] = df['closest'].map(lambda x: int(x.lstrip("distance_from_")))   #  'float' object has no attribute 'lstrip'
	df['color'] = df['closest'].map(lambda x: colmap[x])
	return df

df = assignment(df, centroids)
print(df.head())

fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x'], df['y'], color=df['color'], alpha = 0.5, edgecolor = 'k')
for i in centroids.keys():
	plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0,80)
plt.ylim(0,80)
plt.show()

## Next Stage
