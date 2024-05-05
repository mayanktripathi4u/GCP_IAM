# variables.tf

variable "project_id" {
  description = "The ID of the GCP project"
}

variable "region" {
  description = "The region where the Cloud Function is deployed"
}

variable "cloud_function_name" {
  description = "The name of the Cloud Function"
}

variable "role" {
  description = "The role to grant access to"
}

variable "user_emails" {
  description = "List of user emails to grant access to the Cloud Function"
  type        = list(string)
}
