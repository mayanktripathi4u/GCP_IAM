# Define the provider
provider "google" {
  project = var.project_id
  region  = var.region
}

# Define the IAM binding to grant access to the Cloud Function
resource "google_cloudfunctions_function_iam_binding" "function_iam_binding" {
  project      = var.project_id
  region       = var.region
  cloudfunction = var.cloud_function_name
  role         = var.role

  members = var.user_emails
}