variable "environments" {
  description = "Map of environment names and their S3 bucket names"
  type        = map(string)
  default = {
    production  = "robert-data-lake-production"
    development = "robert-data-lake-development"
  }
}
