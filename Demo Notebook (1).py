# Databricks notebook source
print("hjelklo databricks")

# COMMAND ----------

# MAGIC %run /test/setup

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

files=dbutils.fs.ls('/databricks-datasets')
print(files)
display(files)

# COMMAND ----------


