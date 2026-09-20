# Contributing

Thank you for helping improve this deep-learning learning laboratory.

## Before opening a pull request

1. Explain what you changed and why.
2. Keep notebook demonstrations focused on one concept or experiment.
3. Prefer clear, reproducible code over unnecessary abstraction.
4. Avoid committing secrets, credentials, generated caches, or large unrelated files.
5. Update documentation when a change affects the learning path or repository structure.

## Notebook standard

New or substantially revised notebooks should aim to contain:

1. Objective
2. Dataset or inputs
3. Concept or theory
4. Implementation
5. Visualization
6. Training or experiment
7. Evaluation
8. Key observations
9. Possible improvements

## Validation

Run the repository validator before submitting:

```bash
python scripts/validate_repository.py
```

## Pull requests

A useful pull request should include:

- a concise title;
- a short explanation of the change;
- screenshots or notebook outputs when visuals materially change;
- any dependency changes;
- confirmation that validation passes.

Keep unrelated changes in separate pull requests.
