resource "aws_s3_bucket" "datalake" {
  for_each = local.environments
  bucket   = each.value
  tags = {
    Environment = each.key
  }
}