import os
from src.preprocessing import check_preprocessed_data
from src.eda import check_eda_images
from src.feature_engineering import check_feature_engineering

def main():
    print("🚀 Starting V2X Collision Avoidance Pipeline...")

    # Step 1: Ensure Preprocessed Data Exists
    check_preprocessed_data()

    # Step 2: Check and Generate EDA (if needed)
    check_eda_images()

    # Step 3: Perform Feature Engineering (if not done already)
    check_feature_engineering()

    print("✅ All preprocessing, EDA, and Feature Engineering steps completed!")

if __name__ == "__main__":
    main()
