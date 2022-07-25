import pandas as pd

if __name__ == "__main__":

    df = pd.read_csv("../dataset/CPA/marketing_campaign.csv", delimiter="\t")

    # Write Customer Details
    df_customers = df[
        ["ID", "Year_Birth", "Education", "Marital_Status", "Income", "Kidhome", "Teenhome", "Dt_Customer", "Recency",
         "Complain"]]
    df_customers.to_csv("D:\\Github\\PYTHON-TRAINING\\dataset\\CPA\\output\\customer_details.csv", index=False)

    # Write Products Details
    df_products = df[
        ["ID", "MntWines", "MntFruits", "MntMeatProducts", "MntFishProducts", "MntSweetProducts", "MntGoldProds"]]
    df_products.to_csv("D:\\Github\\PYTHON-TRAINING\\dataset\\CPA\\output\\product_details.csv", index=False)

    # Write Promotion Details
    df_promotions = df[
        ["ID", "NumDealsPurchases", "AcceptedCmp1", "AcceptedCmp2", "AcceptedCmp3", "AcceptedCmp4", "AcceptedCmp5",
         "Response"]]
    df_promotions.to_csv("D:\\Github\\PYTHON-TRAINING\\dataset\\CPA\\output\\promotions_details.csv", index=False)

    # Write Places Details
    df_places = df[
        ["ID", "NumWebPurchases", "NumCatalogPurchases", "NumStorePurchases", "NumWebVisitsMonth"]]
    df_places.to_csv("D:\\Github\\PYTHON-TRAINING\\dataset\\CPA\\output\\places_details.csv", index=False)