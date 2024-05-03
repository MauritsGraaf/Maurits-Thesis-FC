##### ------ Importing Packages ------ #####
from datasets import load_dataset
import pandas as pd



##### ------ Loading data from HuggingFace ------ #####
##### ------ All beauty ------ #####
# Load the all_beauty review dataset
reviews_all_beauty = load_dataset("McAuley-Lab/Amazon-Reviews-2023", "raw_review_All_Beauty", trust_remote_code=True)
# Convert to Pandas DataFrame
reviews_all_beauty_df = reviews_all_beauty["full"].to_pandas()

# Load the all_beauty metadata dataset
metadata_all_beauty = load_dataset("McAuley-Lab/Amazon-Reviews-2023", "raw_meta_All_Beauty", split="full", trust_remote_code=True)
# Convert to Pandas DataFrame
metadata_all_beauty_df = metadata_all_beauty.to_pandas()

##### ------ Appliances ------ #####
# Load the Appliances review dataset
reviews_appliances = load_dataset("McAuley-Lab/Amazon-Reviews-2023", "raw_review_Appliances", trust_remote_code=True)
# Convert to Pandas DataFrame
reviews_appliances_df = reviews_appliances["full"].to_pandas()

# Load the Appliances metadata dataset
metadata_appliances = load_dataset("McAuley-Lab/Amazon-Reviews-2023", "raw_meta_Appliances", split="full", trust_remote_code=True)
# Convert to Pandas DataFrame
metadata_appliances_df = metadata_appliances.to_pandas()

##### ------ Amazon Fashion ------ #####
# Load the Amazon Fashion review dataset
reviews_amazon_fashion = load_dataset("McAuley-Lab/Amazon-Reviews-2023", "raw_review_Amazon_Fashion", trust_remote_code=True)
# Convert to Pandas DataFrame
reviews_amazon_fashion_df = reviews_amazon_fashion["full"].to_pandas()

# Load the Amazon Fashion metadata dataset
metadata_amazon_fashion = load_dataset("McAuley-Lab/Amazon-Reviews-2023", "raw_meta_Amazon_Fashion", split="full", trust_remote_code=True)
# Convert to Pandas DataFrame
metadata_amazon_fashion_df = metadata_amazon_fashion.to_pandas()

#Printing the total length of all imported data
print(len(metadata_all_beauty_df) + 
      len(metadata_amazon_fashion_df) + 
      len(metadata_appliances_df) +
      len(reviews_all_beauty_df) +
      len(reviews_amazon_fashion_df) +
      len(reviews_appliances_df))


##### ------ Merging metadata and review ------ #####
# Merge the All Beauty based on the 'parent_asin' column
merged_all_beauty_df = pd.merge(reviews_all_beauty_df, metadata_all_beauty_df, on='parent_asin', how='inner')

# Merge the Appliances DataFrames based on the 'parent_asin' column
merged_appliances_df = pd.merge(reviews_appliances_df, metadata_appliances_df, on='parent_asin', how='inner')

# Merge the Amazon Fashion DataFrames based on the 'parent_asin' column
merged_amazon_fashion_df = pd.merge(reviews_amazon_fashion_df, metadata_amazon_fashion_df, on='parent_asin', how='inner')



##### ------ Keeping random samples of the dataframes ------ #####
# Select a random sample of 150,000 rows from each merged DataFrame, keeping the real-world distriubtuin
# Calculate the proportions of each category in the concatenated DataFrame
total_samples = len(merged_all_beauty_df) + len(merged_appliances_df) + len(merged_amazon_fashion_df)

proportion_all_beauty = len(merged_all_beauty_df) / total_samples
proportion_appliances = len(merged_appliances_df) / total_samples
proportion_amazon_fashion = len(merged_amazon_fashion_df) / total_samples

# Define the desired total sample size
total_sample_size = 150000

# Calculate the sample sizes for each category based on their proportions
sample_size_all_beauty = int(total_sample_size * proportion_all_beauty)
sample_size_appliances = int(total_sample_size * proportion_appliances)
sample_size_amazon_fashion = int(total_sample_size * proportion_amazon_fashion)

# Sample from each category based on the calculated sample sizes
merged_all_beauty_sample = merged_all_beauty_df.sample(n=min(sample_size_all_beauty, len(merged_all_beauty_df)), random_state=6)
merged_appliances_sample = merged_appliances_df.sample(n=min(sample_size_appliances, len(merged_appliances_df)), random_state=6)
merged_amazon_fashion_sample = merged_amazon_fashion_df.sample(n=min(sample_size_amazon_fashion, len(merged_amazon_fashion_df)), random_state=6)

# Concatenate the sampled DataFrames vertically
concatenated_df = pd.concat([merged_all_beauty_sample, merged_appliances_sample, merged_amazon_fashion_sample])

# Reset the index of the concatenated DataFrame
concatenated_df.reset_index(drop=True, inplace=True)


##### ------ Cleaning the concatenated_df ------ #####
#Renaming the columns
concatenated_df.rename(columns={
    'rating': 'Review_Rating',
    'title_x': 'Review_Title',
    'text': 'Review_Text',
    'images_x': 'Review_Images',
    'asin': 'Product_ASIN',
    'parent_asin': 'Parent_Product_ASIN',
    'user_id': 'User_ID',
    'timestamp': 'Review_Timestamp',
    'helpful_vote': 'Helpful_Votes',
    'verified_purchase': 'Verified_Purchase',
    'main_category': 'Main_Category',
    'title_y': 'Product_Title',
    'average_rating': 'Product_Average_Rating',
    'rating_number': 'Product_Rating_Number',
    'features': 'Product_Features',
    'description': 'Product_Description',
    'price': 'Product_Price',
    'images_y': 'Product_Images',
    'videos': 'Product_Videos',
    'store': 'Product_Store',
    'categories': 'Product_Categories',
    'details': 'Product_Details',
    'bought_together': 'Products_Bought_Together',
    'subtitle': 'Product_Subtitle',
    'author': 'Product_Author'
}, inplace=True)

print(concatenated_df.columns)




