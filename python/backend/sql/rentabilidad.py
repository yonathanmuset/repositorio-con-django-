import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("nothwind.db")
query = """"
SELECT ProductName,sum(Price * Quantity) as revenue 
FROM OrderDetails od
JOIN Products p on p.ProductID = od.ProductID
GROUP by od.ProductID
ORDER by revenue DESC
LIMIT 10
"""
top_products = pd.read_sql_query(query, conn)
top_products.plot(
    x="Productname", y="Revenue", kind="bar", figsize=(10, 5), legend=False
)

plt.title("10 productos mas rentables")
plt.xkcd("productos")
plt.ylabel("revenue")
plt.xticks(rotation=90)
plt.show
