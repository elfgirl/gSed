[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.me/gSed)

# gSed

A project inspired the 'Jailbreak the Patriarchy' Chrome extension that switches gendered nouns inside the browser's HTML page. gSed is an attempt to expand on that idea to any text medium such as e-books, documents, and text files.

## Getting Started

### Usage

In keeping with the unix philosophy of small tools chained together to produce big results, and its namesake `sed`. gSed accepts STDIN/STDOUT redirection

```
cat TheColorsOfSpace.txt | gSed > TheColorsOfSpace.swapped.txt
```

File based re-writing is also possible. The following will produce an output of TheColorsOfSpace.gswap.txt

```
gSed -i TheColorsOfSpace.txt
```

Sometimes, especially during debugging a text or just looking, one wants to see what words were swapped for appropriateness or the sentence context in which they were swapped. The following allows that data to be dumped to file. 

```
gSed -i TheColorsOfSpace.txt -o TheColorsOfSpace.swapped.txt --context TCOS.contexts.json --swaps TCOS.swaps.json
```

This will produce three files as output.

* `TheColorsOfSpace.swapped.txt`  : This is the swapped text.

* `TCOS.swaps.json` : This is a json blob of what words were substituted. Academically interesting but not required for usage.

* `TCOS.contexts.json` : This is a json blob of all lines that had substitutions, and what words were substituted. Academically interesting and useful for debugging


### Example Output

`Pride & Prejudice (Jane Austen)`

The original text 

> It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",

becomes

> It is a truth universally acknowledged, that a single woman in possession of a good fortune must be in want of a husband. However little known the feelings or views of such a woman may be on her first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that she is considered as the rightful property of some one or other of their sons."),


### Installation

Use pip to install from a PyPi repository or from a local wheel file  
```
pip install gSed
or
pip install gSed-0.5.0-py2-none-any.whl
```


### Building

Docker is required to build as we do the wheel building inside a container for cross compiling and isolation. Everything requires is under the build directory. The gSed directory is mapped into the container as a source volume, and the gSed/output directory is mapped to a destination volume of the container.

```
cd gSed/build
./build_python_packages.sh
```


## Deployment

No special instructions for deplpyment other than `pip install gSed`


## Built With

* [Docker](https://www.docker.com/) - Python Docker container used to compile wheels


## Contributing

Please read [CONTRIBUTING](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.


## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/elfgirl/gSed/tags).


## Authors

* **Adrianne Mulvaney** - *Initial work* - [Adrianne](https://github.com/elfgirl)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details


## Acknowledgments

* Inspired by the `Jailbreak the Patriarchy` Chrome extension by [DanielleSucher](https://github.com/DanielleSucher/Jailbreak-the-Patriarchy)

