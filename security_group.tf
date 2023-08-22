resource "aws_security_group" "allow" {
  name        = "allow"
  description = "Allow all traffic"
  vpc_id      = aws_vpc.main.id

  ingress {
    description = "All traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_block  = ["0.0.0.0/0"]
  }
  tags = {
    Name = "allow all"
  }
}