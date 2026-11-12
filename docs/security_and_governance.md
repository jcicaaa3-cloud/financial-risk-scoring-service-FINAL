# Security and Governance Notes

This is a personal project. The notes below describe how the service would need to be handled if it were used as an internal tool.

## Not allowed uses

- Investment recommendation
- Automated lending decision
- Credit screening
- Corporate rating
- Trading signal generation

## Human review

Every decision packet includes a disclaimer. The project is designed as a decision-support artifact, not an automated decision system.

## Data handling

Real financial data should not be committed to a public repository. The repository provides:

- CSV schema templates
- adapter templates for OpenDART/KRX-style ingestion
- synthetic sample data
- artifact directories ignored by git

## Model risk management ideas for a real deployment

- Store model bundles in a registry, not GitHub.
- Version training data and feature pipelines.
- Add calibration monitoring and threshold review.
- Add access control and audit logging.
- Require compliance review before external use.
- Replace synthetic data with audited real data and document data lineage.
