resource "aws_cloudwatch_event_rule" "every_10_minutes" {
  name        = "${var.name}-every-10-minutes"
  description = "Event triggering every day at 8AM"

  schedule_expression = "cron(*/10 * * * ? *)"
}

resource "aws_cloudwatch_event_target" "lambda_every_10_minutes" {
  rule      = "${aws_cloudwatch_event_rule.every_10_minutes.name}"
  target_id = "${var.name}"
  arn       = "${aws_lambda_function.hudebnibazar.arn}"
}

resource "aws_lambda_permission" "allow_cloudwatch" {
  statement_id  = "AllowExecutionFromCloudWatch"
  action        = "lambda:InvokeFunction"
  function_name = "${aws_lambda_function.hudebnibazar.function_name}"
  principal     = "events.amazonaws.com"
  source_arn    = "${aws_cloudwatch_event_rule.every_10_minutes.arn}"
}