resource "aws_secretsmanager_secret" "aurora_db_credential" {
  name = "aurora-db-credentials"
}

resource "aws_secretsmanager_secret_version" "aurora_db_credentials_version" {
  secret_id     = aws_secretsmanager_secret.aurora_db_credential.id
  secret_string = jsonencode({
    username = "${var.user_name}",
    password = "${var.password}",
    engine   = "aurora-mysql"
  })
}
