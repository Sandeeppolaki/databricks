# Databricks notebook source
print("Hello World")

# COMMAND ----------

# MAGIC %sql
# MAGIC select "Hello World from SQL"

# COMMAND ----------

# MAGIC %md
# MAGIC # Title1
# MAGIC
# MAGIC
# MAGIC 1. Item
# MAGIC 2. List
# MAGIC
# MAGIC
# MAGIC Unorderd list
# MAGIC * happening

# COMMAND ----------

# MAGIC %run ./includes/setup

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets')
print(files)

# COMMAND ----------

display(files)

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------


