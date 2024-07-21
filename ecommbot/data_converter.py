
import pandas as pd
from langchain_core.documents import Document


def dataconveter():
    product_data = pd.read_excel("../data/product_review.xlsx")

    data =product_data[["product_title" ,"review"]]

    product_data_docs = []

    # Iterate over the rows of the DataFrame
    for index, row in data.iterrows():
        product_data_docs.append(
            Document(
                page_content=row['review'],
                metadata={"product_name": row['product_title']}
            )
        )
    return product_data_docs
