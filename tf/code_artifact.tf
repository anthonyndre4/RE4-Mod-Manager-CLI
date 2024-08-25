resource "aws_codeartifact_domain" "artifact-domain" {
  domain = "code-artifact-domain"
  tags = {
    "use-case" = "re4cli"
  }
}


resource "aws_codeartifact_repository" "cli-repository" {
  repository = "cli-repository"
  domain     = aws_codeartifact_domain.artifact-domain.domain
}

resource "aws_iam_policy" "codeartifact_policy_iam" {
  name        = "ArtifactAccessPolicy"
  description = "IAM policy for accessing CodeArtifact"

  policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Effect" : "Allow",
        "Action" : [
          "codeartifact:GetAuthorizationToken",
          "codeartifact:ReadFromRepository",
          "codeartifact:PublishPackageVersion",
          "codeartifact:CreateRepository",
          "codeartifact:Describe*",
          "codeartifact:List*",
          "codeartifact:*"
        ],
        "Resource" : "*"
      }
    ]
  })
  tags = {
    "use-case" = "re4cli"
  }
}

resource "aws_iam_role" "codeartifact_role" {
  name = "codeartifact-role-actions"

  assume_role_policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Effect" : "Allow",
        "Principal" : {
          "AWS" : "arn:aws:iam::682033465466:user/github-actions"
        },
        "Action" : "sts:AssumeRole"
      }
    ]
  })

  inline_policy {
    name   = "codeartifact-access"
    policy = aws_iam_policy.codeartifact_policy_iam.policy
  }

  tags = {
    "use-case" = "re4cli"
  }
}
