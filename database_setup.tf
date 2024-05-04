resource "aws_db_subnet_group" "my_db_subnet_group" {
  name       = "my-db-subnet-group"
  subnet_ids = [aws_subnet.private_subnet.id,aws_subnet.public_subnet.id]
  
}

resource "aws_rds_cluster" "aurora_severless" {
 cluster_identifier           = "aurora-serverless-cluster"
  engine                       = "aurora-mysql"
  engine_mode                  = "serverless"
  database_name                = "${var.environment}_database"
  master_username              = "${var.user_name}"
  master_password              = "${var.password}"
  skip_final_snapshot          = true
  deletion_protection          = false
  db_subnet_group_name         = aws_db_subnet_group.my_db_subnet_group.name
  vpc_security_group_ids = [ aws_security_group.dev-sg.id ]
}