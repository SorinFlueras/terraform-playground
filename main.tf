resource "aws_s3_bucket" "b" {
  count  = var.create_bucket ? 1 : 0
  bucket = "my-tf-test-bucket"
  acl    = "private"

  tags = {
    Name        = var.bucket_name
    Environment = "Dev"
  }
}
