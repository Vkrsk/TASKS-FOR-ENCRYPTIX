import pandas as pd

# Sample training data
train_data = {
    'SerialNumber': [1, 2, 3],
    'MOVIE_NAME': ['Movie A', 'Movie B', 'Movie C'],
    'GENRE': ['action, comedy', 'drama, romance', 'horror, thriller'],
    'MOVIE_PLOT': [
        'An action-packed comedy that will leave you in stitches.',
        'A heartwarming drama about love and relationships.',
        'A terrifying horror movie with thrilling moments.'
    ]
}

# Sample test data
test_data = {
    'SerialNumber': [4, 5],
    'MOVIE_NAME': ['Movie D', 'Movie E'],
    'MOVIE_PLOT': [
        'A hilarious comedy that is full of action.',
        'A romantic drama with deep emotional moments.'
    ]
}

# Create DataFrames
train_df = pd.DataFrame(train_data)
test_df = pd.DataFrame(test_data)

# Save to text files with tab delimiter
train_df.to_csv('train_data.txt', sep='\t', index=False, header=False)
test_df.to_csv('test_data.txt', sep='\t', index=False, header=False)
