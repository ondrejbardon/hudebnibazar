data "archive_file" "dummy_code" {
  type = "zip"
  source_file = "${path.module}/files/dummy_code.py"
  output_path = "${path.module}/files/dummy_code.zip"
}

resource "aws_lambda_function" "hudebnibazar" {
  function_name = "${var.name}"

  filename         = "${data.archive_file.dummy_code.output_path}"
  source_code_hash = "${data.archive_file.dummy_code.output_base64sha256}"
  role             = "${aws_iam_role.hudebnibazar.arn}"

  runtime     = "python3.8"
  handler     = "hudebnibazar.lambda_handler"
  timeout     = "${var.lambda_timeout}"
  memory_size = "${var.lambda_memory_size}"

  lifecycle {
    ignore_changes = ["source_code_hash", "last_modified", "filename"]
  }
}
