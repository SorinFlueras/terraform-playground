resource "aws_s3_bucket" "b" {
  count  = var.test != null && true ? 1 : 0
  bucket = "my-tf-test-bucket"
  acl    = "private"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}