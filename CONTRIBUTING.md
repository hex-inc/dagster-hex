## Contributing

- This repo uses pre-commit hooks. Run `pip install pre-commit` and
`precommit install` to install the hooks.


### Deploying

If you have permissions to deploy a package here's what you need to do:

- Increment the `VERSION.txt` file, following [Semantic Versioning](https://semver.org/)
- Update the Changelog following [Keep A Changelog](https://keepachangelog.com/en/1.0.0/) formatting.
- Push your changes, have the PR reviewed. CircleCI will test and lint your package
- If everything looks good, merge to main.
- Tag the main branch. For example, `git tag 1.1.2 && git push --tags origin'
- CircleCI will upload the latest release to pypi
