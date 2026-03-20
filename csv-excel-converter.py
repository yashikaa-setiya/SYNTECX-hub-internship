import pandas as pd
import argparse as ap
import logging 

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

parser = ap.ArgumentParser(description="CSV to Excel Converter")

parser.add_argument("--input", required=True, help="Path to input CSV file")
parser.add_argument("--output", required=True, help="Path to output Excel file")

args = parser.parse_args()
    
    
try:
    #reading csv
    logging.info(f"Reading file: {args.input}")
    df = pd.read_csv(args.input)
    #clean data
    df = df.fillna("Unknown")
    
    # parse date column
    df["OrderDate"] = pd.to_datetime(df["OrderDate"])
    
    # rename columns to snake_case
    df = df.rename(columns={
        "OrderID": "order_id",
        "CustomerName": "customer_name",
        "Product": "product",
        "Category": "category",
        "Quantity": "quantity",
        "Price": "price",
        "OrderDate": "order_date",
        "Shipped": "shipped",
        "Country": "country"
    })
    
    df.to_excel(args.output, index=False)
    logging.info(f"File saved successfully: {args.output}")

except FileNotFoundError:
    logging.error(f"File not found: {args.input}")
except Exception as e:
    logging.error(f"Something went wrong: {e}")



