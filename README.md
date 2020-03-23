# terraform-count-to-for-each
Python script to convert Terraform state file from usage of count (index) to usage of for_each (key)

This is a workaround script built for resolving Terraform state's issues in converting resources using `count` to resources using `for_each`.

Known issues:

*  Unable to "state mv" to a for_each resource
https://github.com/hashicorp/terraform/issues/22301
* When I change count to for_each, the resource will rebuild ?
https://github.com/hashicorp/terraform/issues/22375


Run:
```
python3 main.py -i ../default.tfstate -o ../new.tfstate -t google_bigquery_table
```