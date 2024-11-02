from functions import *
import time

start_time = time.time()

# read in data
print("Reading in data...")
dataset = "../data/sample_testset.json.gz"

# Preprocess the data
print("Preprocessing data...")
df = parse_features(dataset) # Parse the features
combined_df = df.groupby(['transcript_id', 'position', 'flanking_nucleotide']).mean().reset_index() # Combine the transcripts
processed_df = preprocessing(combined_df) # Perform feature engineering and scaling
encoded_df = encode_nucleotide(processed_df) # Encode the nucleotides
X_test = encoded_df.drop(columns=['transcript_id', 'position']) # Drop the columns that are not features

input_data = torch.tensor(X_test.values, dtype=torch.float32)

# Load the model
print("Loading model...")
model = NeuralNetwork()
model.load_state_dict(torch.load('../data/model_checkpoint.pth', weights_only=True))

# Make predictions
print("Making predictions...")
model.eval()
with torch.no_grad():
    predictions = model(input_data).squeeze()

# Save the predictions (optional)
results = encoded_df[['transcript_id', 'position']].copy()
results['score'] = predictions
results.columns = ['transcript_id', 'transcript_position', 'score']
# results.to_csv('../data/sample_predictions.csv', index=False)

# View the results
print("############################# Results #############################")
print(results.head())
print("###################################################################")
print("Execution time: %.2f seconds" % (time.time() - start_time))
