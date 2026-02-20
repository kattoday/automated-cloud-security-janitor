# automated-cloud-security-janitor
​🛡️ Automated security compliance tool using AWS Config, EventBridge, and Lambda to enforce S3 public access blocks in real-time. ISO27001 aligned.

## 📌 Project Overview
An event-driven security tool designed to enforce **ISO27001** compliance controls within an AWS environment. This project automatically detects S3 buckets that have "Block Public Access" disabled and programmatically remediates them to a private state within seconds.

##The Mermaid Architecture Code
graph LR
    A[S3 Bucket] -- "State Change" --> B(AWS Config)
    B -- "Non-Compliant" --> C{EventBridge}
    C -- "Trigger" --> D[Lambda Function]
    D -- "Fix" --> A
    D -- "Alert" --> E[SNS Topic]
    E -- "Email" --> F[Security Admin]

    style A fill:#f96,stroke:#333,stroke-width:2px
    style D fill:#69f,stroke:#333,stroke-width:2px
    style B fill:#fff,stroke:#333


## 🛠 Tech Stack
* **AWS Config**: Monitoring and compliance evaluation.
* **Amazon EventBridge**: Real-time event routing (Nerve Center).
* **AWS Lambda**: Python-based (Boto3) automated remediation logic.
* **Amazon SNS**: Instant security team notification via email.

## 🚀 How it Works
1. **Detection**: AWS Config evaluates the `s3-bucket-level-public-access-prohibited` rule.
2. **Trigger**: Upon a `NON_COMPLIANT` state change, an EventBridge Rule captures the event.
3. **Remediation**: A Python Lambda function parses the event, identifies the bucket, and applies a `PutPublicAccessBlock` API call.
4. **Notification**: The system publishes an alert to an SNS Topic, notifying administrators of the breach and successful fix.

## 🔒 Security Principles Applied
* **Least Privilege**: The Lambda execution role is restricted to specific S3 and SNS actions.
* **Continuous Monitoring**: Shift-left security approach by ensuring zero-drift in bucket permissions.
* **Auditability**: All actions are logged via Amazon CloudWatch and AWS Config history.

## 📖 Lessons Learned
* Handled API Throttling ("Rate Exceeded") by implementing manual re-evaluation delays.
* Managed Event Propagation lag between AWS Config and EventBridge.
