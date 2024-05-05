# GCP_IAM
Maintaining the IAM using Terraform and GH.

# Steps to follow
1. Create a GitHub Repo
2. Colne Repo to Local workstation
3. Cretae TF Configuration files
4. Create Service Account in GCP
5. Cretae GH secret with SA Keys
6. Create GH Action workflow 
7. Push Code
8. Test Pipeline

When running Terraform commands, pass this variables file using the -var-file flag:

terraform apply -var-file=var_file.tfvars


