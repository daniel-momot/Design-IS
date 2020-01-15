import io  # needed because of weird encoding of u.item file

from surprise import KNNWithMeans
from surprise import Dataset
from surprise import get_dataset_dir

from collections import defaultdict



def read_item_names():
    """Read the u.item file from MovieLens 100-k dataset and return two
    mappings to convert raw ids into movie names and movie names into raw ids.
    """

    file_name = get_dataset_dir() + '/ml-100k/ml-100k/u.item'
    rawid_to_name = {}
    with io.open(file_name, 'r', encoding='ISO-8859-1') as f:
        for line in f:
            line = line.split('|')
            rawid_to_name[line[0]] = (line[1], line[2])

    return rawid_to_name

# Input user number
input_user_id = input('Enter user number: ')

# First, train the algortihm to compute the similarities between users
data = Dataset.load_builtin('ml-100k')
trainset = data.build_full_trainset()
sim_options = {'name': 'cosine', 'user_based': True, 'min_support': 5}
algo = kNNWithMeans(k=4, min_k=4, sim_options=sim_options)
algo.fit(trainset)

# Drop out the missing ratings and make predictions
testset = trainset.build_anti_testset()
testset = filter(lambda x: x[0] == input_user_id, testset)
predictions = algo.test(testset)


# Create for each iser list of predictions for items
top_n = defaultdict(list)
for uid, iid, _, est, _ in predictions:
    top_n[uid].append((iid, round(est, 3)))

# For each user sort items and leave only 5 most valid
for uid, user_ratings in top_n.items():
    user_ratings.sort(key=lambda x: x[1], reverse=True)
    top_n[uid] = user_ratings[:5]

# Get item names
item_names = read_item_names()

# Print results
print(f'User {input_user_id}:')
for movie_rid, rating in top_n[input_user_id]:
    print('{:4s} {:<60s} {}'.format(movie_rid, str(item_names[movie_rid]), rating))



