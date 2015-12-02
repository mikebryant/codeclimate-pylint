# Code Climate Pylint Engine

`codeclimate-pylint` is a Code Climate engine that wraps [Pylint](http://www.pylint.org/). You can run it on your command line using the Code Climate CLI, or on our hosted analysis platform.

### Installation

1. If you haven't already, [install the Code Climate CLI](https://github.com/codeclimate/codeclimate).
2. Run `codeclimate engines:enable pylint`. This command both installs the engine and enables it in your `.codeclimate.yml` file.
3. You're ready to analyze! Browse into your project's folder and run `codeclimate analyze`.

### Configuration

Like running pylint locally, you can configure it by including a `pylintrc` file in your repository.
Consult the [pylint documentation](http://docs.pylint.org/run.html#command-line-options) for more details.

### Building

In order to build the docker image, run

```console
docker build -t codeclimate/codeclimate-pylint .
```

### Limitations

CodeClimate currently disallows internet access from engines. Consequently, getting
the dependencies for the project being analysed is impossible.

The checks disabled due to this are:
* `import-error`

### Need help?

For help with Pylint, [check out their documentation](http://docs.pylint.org/).

If you're running into a Code Climate issue, first look over this project's [GitHub Issues](https://github.com/mikebryant/codeclimate-pylint/issues), as your question may have already been covered. If not, [go ahead and open a support ticket with us](https://codeclimate.com/help).
