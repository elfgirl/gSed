gSed
====

| A project inspired the 'Jailbreak the Patriarchy' Chrome extension that switches gendered nouns inside the browser's HTML page. gSed is an attempt to exapand on that idea to any text medium such as ebooks, documetns, and text files.

Stream Usage
------------

| In keeping with the unix philiosphy of small tools chained together to produce big results, and its namesake `sed`. gSed accepts STDIN/STDOUT redirecting

::

    cat TheColorsOfSpace.txt | gSed > TheColorsOfSpace.swapped.txt


File Usage
----------

::

    gSed -i TheColorsOfSpace.txt

    will produce an output of TheColorsOfSpace.gswap.txt

    gSed -i TheColorsOfSpace.txt -o TheColorsOfSpace.swapped.txt --context TCOS.contexts.json --swaps TCOS.swaps.json

    will produce three files as output.

    TheColorsOfSpace.swapped.txt  : This is the swapped text.
    TCOS.swaps.json : This is a json blob of what words were substituted. Academically interesting but not required for usage.
    TCOS.contexts.json : This is a json blob of all lines that had substitutions, and what words were substituted. Academically interesting and useful for debugging

Build
-----

| Building utilizes a docker python image to keep things as clean as possible. `cd` into the build directory and execute `./build_python_packages.sh`. This will do the following

* Create a container on the local docker host from python 2.7 image
* Add in the project listed requirements via pip
* Map the container volumes to the local directory and another volume to the output directory
* Build the python package.






