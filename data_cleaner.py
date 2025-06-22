import io
import os

import pandas as pd


def clean_csv(file_path, output_path=None, dropna=False, fillna_method="mean", skip_head=0, skip_tail=0, encoding="utf-8-sig"):
    # 0. Prepare default output file name if not provided
    if output_path is None:
        # Ensure the output directory exists
        output_dir = os.path.join(".", "CLEANED_DATA")
        os.makedirs(output_dir, exist_ok=True)

        # Extract filename and create new filename with prefix
        base_name = os.path.basename(file_path)
        cleaned_name = "CLEANED_" + base_name
        output_path = os.path.join(output_dir, cleaned_name)

    # 1. Read the CSV file
    # Read file as text, skip metadata at top and foot
    with open(file_path, encoding=encoding) as f:
        lines = f.readlines()
        # Keep only the rows between skip_head and -skip_tail
        data_lines = lines[skip_head:len(lines) - skip_tail if skip_tail > 0 else None]
        cleaned_text = "".join(data_lines)

    # Parse the cleaned content into a DataFrame
    df = pd.read_csv(io.StringIO(cleaned_text))

    print(f"Original data shape: {df.shape}")

    # 2. Standardize column names: lowercase and replace spaces with underscores
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # 3. Drop duplicate rows
    df = df.drop_duplicates()
    print(f"Shape after removing duplicates: {df.shape}")

    # 4. Strip leading/trailing whitespace from string columns
    str_cols = df.select_dtypes(include="object").columns
    df[str_cols] = df[str_cols].apply(lambda x: x.str.strip())

    # 5. Handle missing values
    if dropna:
        df = df.dropna()
        print("Dropped all rows with missing values")
    else:
        for col in df.columns:
            if df[col].isnull().sum() > 0:
                if fillna_method == "mean" and df[col].dtype in ["int64", "float64"]:
                    df[col] = df[col].fillna(df[col].mean())
                elif fillna_method == "median" and df[col].dtype in ["int64", "float64"]:
                    df[col] = df[col].fillna(df[col].median())
                else:
                    df[col] = df[col].fillna("unknown")
        print("Missing values filled")

    # 6. Convert column data types automatically (e.g., from object to int, float, etc.)
    df = df.convert_dtypes()

    # 7. Save the cleaned dataset to a new CSV file
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to: {output_path}")

    return df

if __name__ == '__main__':
    # clean_csv("Data  Collection/1410028701-canada_stat.csv", skip_head=8, skip_tail=10)
    # clean_csv("Data  Collection/linkedin_canada.csv")
    pass
